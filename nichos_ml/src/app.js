(() => {
  const moments = [...document.querySelectorAll('.moment')];
  const positionButtons = [...document.querySelectorAll('.position-button')];
  const prev = document.querySelector('#prev-button');
  const next = document.querySelector('#next-button');
  const fullscreen = document.querySelector('#fullscreen-button');
  const fullscreenLabel = document.querySelector('#fullscreen-label');
  const stage = document.querySelector('#stage');
  const status = document.querySelector('#sr-status');
  const count = moments.length;
  const innerState = new Map([[1, 0], [2, 0], [3, 0], [5, 0]]);
  let current = 1;

  const getMomentFromLocation = () => {
    const queryMoment = Number(new URLSearchParams(window.location.search).get('moment'));
    const hashMatch = window.location.hash.match(/(?:moment-?|m)(\d+)/i);
    const hashMoment = hashMatch ? Number(hashMatch[1]) : 0;
    const candidate = queryMoment || hashMoment;
    return candidate >= 1 && candidate <= count ? candidate : 1;
  };

  const announce = (message) => {
    if (status) status.textContent = message;
  };

  const updateMoment = (nextIndex, { focus = true, writeHash = true } = {}) => {
    current = Math.max(1, Math.min(count, Number(nextIndex) || 1));
    moments.forEach((moment, index) => {
      const active = index + 1 === current;
      moment.classList.toggle('is-active', active);
      moment.hidden = !active;
    });
    positionButtons.forEach((button, index) => {
      const active = index + 1 === current;
      button.classList.toggle('is-current', active);
      if (active) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    if (prev) prev.disabled = current === 1;
    if (next) next.disabled = current === count;
    stage.dataset.moment = String(current);
    if (writeHash) history.replaceState(null, '', `#moment-${current}`);
    const heading = moments[current - 1].querySelector('h1, h2');
    announce(`Momento ${current} de ${count}: ${heading?.textContent.trim() || ''}`);
    if (focus) heading?.focus({ preventScroll: true });
  };

  const setLens = (value) => {
    const normalized = ((value % 4) + 4) % 4;
    innerState.set(2, normalized);
    document.querySelectorAll('.lens-row').forEach((row, index) => row.classList.toggle('is-focus', index === normalized));
    const lensIndex = document.querySelector('#lens-index');
    if (lensIndex) lensIndex.textContent = `${String.fromCharCode(65 + normalized)} / 04`;
  };

  const setPipeline = (value) => {
    const normalized = ((value % 5) + 5) % 5;
    innerState.set(3, normalized);
    document.querySelectorAll('.pipeline-node').forEach((node, index) => node.classList.toggle('is-focus', index === normalized));
  };

  const setDemo = (value) => {
    const normalized = value > 0 ? 1 : 0;
    innerState.set(5, normalized);
    const scene = document.querySelector('.churn-stage');
    scene?.classList.toggle('is-focus', normalized === 1);
    const step = document.querySelector('#demo-step');
    if (step) step.textContent = normalized ? '02 · regla + contraste' : '01 · baseline';
  };

  const resetInner = (index) => {
    if (index === 1) {
      document.querySelector('.opening-field')?.classList.remove('is-emphasis');
      innerState.set(1, 0);
    }
    if (index === 2) setLens(0);
    if (index === 3) setPipeline(0);
    if (index === 5) setDemo(0);
  };

  const resetCurrent = () => {
    resetInner(current);
    announce(`Momento ${current} reiniciado`);
  };

  const advanceInner = () => {
    if (current === 1) {
      const emphasis = innerState.get(1) === 0 ? 1 : 0;
      innerState.set(1, emphasis);
      document.querySelector('.opening-field')?.classList.toggle('is-emphasis', emphasis === 1);
      announce(emphasis ? 'La ventana de contraste queda en foco' : 'La poblacion vuelve a su estado resumido');
      return;
    }
    if (current === 2) {
      const nextLens = (innerState.get(2) + 1) % 4;
      setLens(nextLens);
      announce(`Lente ${String.fromCharCode(65 + nextLens)} de 04`);
      return;
    }
    if (current === 3) {
      const nextNode = (innerState.get(3) + 1) % 5;
      setPipeline(nextNode);
      announce(`Pieza ${nextNode + 1} de 05`);
      return;
    }
    if (current === 5) {
      setDemo(1 - innerState.get(5));
      announce(innerState.get(5) ? 'Contraste enfatizado: 4 por ciento a 12 por ciento' : 'Baseline visible');
    }
  };

  prev?.addEventListener('click', () => updateMoment(current - 1));
  next?.addEventListener('click', () => updateMoment(current + 1));
  positionButtons.forEach((button) => button.addEventListener('click', () => updateMoment(button.dataset.go)));
  document.querySelectorAll('.lens-row').forEach((row, index) => row.addEventListener('click', () => setLens(index)));
  document.querySelectorAll('.pipeline-node').forEach((node, index) => node.addEventListener('click', () => setPipeline(index)));

  fullscreen?.addEventListener('click', async () => {
    try {
      if (!document.fullscreenElement) await document.documentElement.requestFullscreen();
      else await document.exitFullscreen();
    } catch {
      fullscreen.setAttribute('aria-label', 'Pantalla completa no disponible en este navegador');
      announce('Pantalla completa no disponible en este navegador');
    }
  });
  document.addEventListener('fullscreenchange', () => {
    const active = Boolean(document.fullscreenElement);
    if (fullscreenLabel) fullscreenLabel.textContent = active ? 'salir' : 'pantalla completa';
    fullscreen?.setAttribute('aria-label', active ? 'Salir de pantalla completa' : 'Entrar en pantalla completa');
  });

  document.addEventListener('keydown', (event) => {
    const target = event.target;
    const isControl = target.matches('button, a, input, textarea, select');
    if (event.key === 'ArrowRight' || event.key === 'PageDown') { event.preventDefault(); updateMoment(current + 1); return; }
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') { event.preventDefault(); updateMoment(current - 1); return; }
    if (event.key === 'Home') { event.preventDefault(); updateMoment(1); return; }
    if (event.key === 'End') { event.preventDefault(); updateMoment(count); return; }
    if (event.key.toLowerCase() === 'r' && !isControl) { event.preventDefault(); resetCurrent(); return; }
    if ((event.key === ' ' || event.key === 'Enter') && !isControl) { event.preventDefault(); advanceInner(); }
  });

  window.addEventListener('hashchange', () => updateMoment(getMomentFromLocation(), { focus: true, writeHash: false }));
  moments.forEach((moment) => moment.querySelector('h1, h2')?.setAttribute('tabindex', '-1'));
  updateMoment(getMomentFromLocation(), { focus: false, writeHash: false });
})();
