from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
RENDERS = ROOT / "renders"
RENDERS.mkdir(exist_ok=True)
URL = (ROOT / "candidate" / "index.html").resolve().as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page = context.new_page()
    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda err: console_errors.append(str(err)))
    page.goto(URL, wait_until="networkidle")
    assert page.locator(".moment.is-active").count() == 1
    assert page.locator(".moment.is-active h1").inner_text().startswith("El promedio")
    assert page.locator("img.registration-image").evaluate("img => img.complete && img.naturalWidth > 0")
    assert page.locator("button.position-button").count() == 7

    # Full-viewport evidence: direct position through visible controls.
    showcase_steps = {1: 1, 2: 3, 3: 2, 4: 3}
    for i in range(1, 8):
        page.locator(f"button[data-go='{i}']").click()
        for _ in range(showcase_steps.get(i, 0)):
            page.keyboard.press("Space")
        page.wait_for_timeout(650)
        assert page.locator(f".moment[data-moment='{i}'].is-active").count() == 1
        page.screenshot(path=str(RENDERS / f"{i:02d}.png"), full_page=False)

    # Arrow navigation and boundary behavior.
    page.locator("button[data-go='1']").click()
    page.keyboard.press("ArrowRight")
    assert page.locator(".moment[data-moment='2'].is-active").count() == 1
    page.keyboard.press("ArrowLeft")
    assert page.locator(".moment[data-moment='1'].is-active").count() == 1
    page.keyboard.press("Home")
    page.keyboard.press("End")
    assert page.locator(".moment[data-moment='7'].is-active").count() == 1

    # Inner-state keyboard operation and deterministic reset.
    page.locator("button[data-go='1']").click(); page.keyboard.press("r"); page.keyboard.press("Space")
    page.wait_for_timeout(30)
    reveal = page.locator(".region-window").evaluate("el => ({opacity:getComputedStyle(el).opacity, animation:getComputedStyle(el).animationName})")
    assert float(reveal["opacity"]) >= 0.94 and reveal["animation"] == "none"
    page.locator("button[data-go='2']").click(); page.keyboard.press("r"); page.keyboard.press("Space")
    assert page.locator(".lens-route[data-lens='1'].is-focus").count() == 1
    page.keyboard.press("Space"); page.keyboard.press("Space")
    assert page.locator(".lens-route[data-lens='3'].is-focus").count() == 1
    page.keyboard.press("r")
    assert page.locator(".lens-route[data-lens='0'].is-focus").count() == 1
    page.locator("button[data-go='3']").click(); page.keyboard.press("r"); page.keyboard.press("Space")
    assert page.locator(".registered-stack").get_attribute("data-inner") == "1"
    page.keyboard.press("r")
    assert page.locator(".registered-stack").get_attribute("data-inner") == "0"
    page.locator("button[data-go='4']").click(); page.keyboard.press("r"); page.keyboard.press("Space")
    assert page.locator("#demo-step").inner_text().startswith("02")
    assert page.locator(".baseline-strip").evaluate("el => getComputedStyle(el).visibility") == "visible"
    assert page.locator(".rule-reveal").evaluate("el => getComputedStyle(el).visibility") == "hidden"
    page.keyboard.press("Space"); page.keyboard.press("Space")
    assert page.locator(".holdout-strip").evaluate("el => getComputedStyle(el).visibility") == "visible"
    assert "baseline 4.08%" in page.locator(".holdout-strip").inner_text()
    page.keyboard.press("r")
    assert page.locator("#demo-step").inner_text().startswith("01")
    assert page.locator(".baseline-strip").evaluate("el => getComputedStyle(el).visibility") == "hidden"

    # Semantics, overflow, focus and fullscreen availability.
    metrics = page.evaluate("""() => ({
      overflowX: document.documentElement.scrollWidth > innerWidth,
      overflowY: document.documentElement.scrollHeight > innerHeight,
      fullscreenEnabled: document.fullscreenEnabled,
      activeTag: document.activeElement?.tagName,
      navButtons: document.querySelectorAll('button').length,
      hiddenMoments: [...document.querySelectorAll('.moment')].filter(x => x.hidden).length
    })""")
    assert metrics["overflowX"] is False and metrics["overflowY"] is False
    assert metrics["navButtons"] >= 10 and metrics["hiddenMoments"] == 6

    page.locator("#fullscreen-button").click()
    page.wait_for_timeout(100)
    if page.evaluate("Boolean(document.fullscreenElement)"):
        assert page.locator("#fullscreen-button").get_attribute("aria-label") == "Salir de pantalla completa"
        page.keyboard.press("Escape")
        page.wait_for_timeout(100)
        if page.evaluate("Boolean(document.fullscreenElement)"):
            page.locator("#fullscreen-button").click()
            page.wait_for_timeout(100)
        assert page.locator("#fullscreen-button").get_attribute("aria-label") == "Entrar en pantalla completa"

    reduced = context.new_page()
    reduced.emulate_media(reduced_motion="reduce")
    reduced.goto(URL, wait_until="networkidle")
    duration = reduced.locator(".moment").first.evaluate("el => getComputedStyle(el).transitionDuration")
    reduced.locator("button[data-go='4']").click()
    assert reduced.locator(".hypothesis").evaluate("el => getComputedStyle(el).visibility") == "visible"
    print({"reduced_motion_transition": duration})
    assert duration in ("0s", "0.01ms", "0.00001s", "1e-05s")
    reduced.close()
    print({"renders": 7, "console_errors": console_errors, "metrics": metrics, "fullscreen_attempt": "API exposed" if metrics["fullscreenEnabled"] else "not exposed in headless"})
    browser.close()
