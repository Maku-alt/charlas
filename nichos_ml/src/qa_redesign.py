from pathlib import Path
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate" / "pysubgroup.html"
RENDERS = ROOT / "renders" / "redesign"
RENDERS.mkdir(parents=True, exist_ok=True)


def exercise(page, viewport, prefix):
    errors = []
    page.on("console", lambda msg: errors.append(f"console:{msg.type}:{msg.text}") if msg.type == "error" else None)
    page.on("pageerror", lambda error: errors.append(f"pageerror:{error}"))
    page.goto(CANDIDATE.as_uri(), wait_until="networkidle")
    page.wait_for_timeout(250)

    moment_count = page.locator(".moment").count()
    assert moment_count == 7, moment_count
    assert page.locator(".moment.is-active").count() == 1
    assert page.locator("h1").inner_text().lower().startswith("pysubgroup")
    assert page.locator("img").count() == 0
    assert page.locator("link[rel=stylesheet]").count() == 0
    assert page.locator("script[src]").count() == 0

    for index in range(1, 8):
        page.locator(f".position-button[data-go='{index}']").click()
        page.wait_for_timeout(500)
        assert page.locator(f"#moment-{index}.is-active").count() == 1
        assert page.locator(f"#moment-{index}").get_attribute("hidden") is None
        page.screenshot(path=str(RENDERS / f"{index:02d}-{prefix}.png"), full_page=False)

    page.goto(CANDIDATE.as_uri() + "#moment-5", wait_until="networkidle")
    assert page.locator("#moment-5.is-active").count() == 1
    page.keyboard.press("Home")
    assert page.locator("#moment-1.is-active").count() == 1
    page.keyboard.press("ArrowRight")
    assert page.locator("#moment-2.is-active").count() == 1
    page.keyboard.press("End")
    assert page.locator("#moment-7.is-active").count() == 1
    page.goto(CANDIDATE.as_uri() + "#moment-5", wait_until="networkidle")
    page.keyboard.press("Space")
    assert page.locator(".churn-stage.is-focus").count() == 1
    page.keyboard.press("r")
    assert page.locator(".churn-stage.is-focus").count() == 0

    dimensions = page.evaluate("({width: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight, innerWidth: innerWidth, innerHeight: innerHeight})")
    overflow = dimensions["width"] > dimensions["innerWidth"] + 1 or dimensions["height"] > dimensions["innerHeight"] + 1
    assert not overflow, dimensions
    assert page.locator("#fullscreen-button").get_attribute("aria-label")
    assert not errors, errors
    return {"viewport": viewport, "moment_count": moment_count, "overflow": overflow, "errors": errors, "dimensions": dimensions}


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    )
    desktop = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    results = [exercise(desktop, "1600x900", "desktop"), exercise(mobile, "390x844", "mobile")]
    browser.close()
    print(results)
