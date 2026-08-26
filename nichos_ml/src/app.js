(() => {
  const moments = [...document.querySelectorAll('.moment')];
  const positionButtons = [...document.querySelectorAll('.position-button')];
  const prev = document.querySelector('#prev-button');
  const next = document.querySelector('#next-button');
  const fullscreen = document.querySelector('#fullscreen-button');
  const stage = document.querySelector('#stage');
  let current = 1;
  const innerState = new Map([[1, 0], [2, 0], [3, 0], [4, 0]]);

  const resetInner = (index) => {
    innerState.set(index, 0);
    if (index === 2) {
      document.querySelectorAll('.lens-route').forEach((el, i) => el.classList.toggle('is-focus', i === 0));
      document.querySelector('#lens-index').textContent = 'A / 04';
    }
    if (index === 3) {
      document.querySelector('.registered-stack').dataset.inner = '0';
    }
    if (index === 4) {
      document.querySelector('#demo-step').textContent = '01 · config';
      document.querySelector('.demo-table').dataset.inner = '0';
    }
  };

  const updateMoment = (nextIndex, { focus = true } = {}) => {
    current = Math.max(1, Math.min(7, nextIndex));
    moments.forEach((moment, i) => {
      const active = i + 1 === current;
      moment.classList.toggle('is-active', active);
      moment.hidden = !active;
    });
    positionButtons.forEach((button, i) => {
      const active = i + 1 === current;
      button.classList.toggle('is-current', active);
      if (active) button.setAttribute('aria-current', 'step'); else button.removeAttribute('aria-current');
    });
    stage.dataset.moment = String(current);
    if (focus) {
      const heading = moments[current - 1].querySelector('h1, h2');
      heading?.focus?.({ preventScroll: true });
    }
  };

  const advanceInner = () => {
    if (current === 2) {
      const value = (innerState.get(2) + 1) % 4; innerState.set(2, value);
      document.querySelectorAll('.lens-route').forEach((el, i) => el.classList.toggle('is-focus', i === value));
      document.querySelector('#lens-index').textContent = String.fromCharCode(65 + value) + ' / 04';
    } else if (current === 3) {
      const value = (innerState.get(3) + 1) % 5; innerState.set(3, value);
      const sheets = document.querySelectorAll('.stack-sheet');
      sheets.forEach((sheet, i) => sheet.style.transform = i === value ? 'translateX(3.2rem) rotate(0deg)' : '');
      document.querySelector('.registered-stack').dataset.inner = String(value);
    } else if (current === 4) {
      const value = Math.min(3, innerState.get(4) + 1); innerState.set(4, value);
      const labels = ['01 · config', '02 · baseline', '03 · rule + métricas', '04 · holdout + hipótesis'];
      document.querySelector('#demo-step').textContent = labels[value];
      const table = document.querySelector('.demo-table');
      table.dataset.inner = String(value);
      const focusTargets = ['.demo-config', '.baseline-strip', '.rule-reveal', '.holdout-strip'];
      table.querySelector(focusTargets[value])?.focus?.({ preventScroll: true });
    } else if (current === 1) {
      document.querySelector('.average-scene').classList.add('is-revealed');
    }
  };

  const resetCurrent = () => {
    resetInner(current);
    if (current === 1) document.querySelector('.average-scene').classList.remove('is-revealed');
    if (current === 4) document.querySelector('.demo-table').dataset.inner = '0';
    if (current === 3) document.querySelectorAll('.stack-sheet').forEach(sheet => sheet.style.transform = '');
  };

  prev.addEventListener('click', () => updateMoment(current - 1));
  next.addEventListener('click', () => updateMoment(current + 1));
  positionButtons.forEach(button => button.addEventListener('click', () => updateMoment(Number(button.dataset.go))));
  fullscreen.addEventListener('click', async () => {
    try {
      if (!document.fullscreenElement) await document.documentElement.requestFullscreen(); else await document.exitFullscreen();
    } catch { fullscreen.setAttribute('aria-label', 'Pantalla completa no disponible en este navegador'); }
  });
  document.addEventListener('fullscreenchange', () => {
    const active = Boolean(document.fullscreenElement);
    fullscreen.querySelector('span').textContent = active ? 'salir' : 'pantalla completa';
    fullscreen.setAttribute('aria-label', active ? 'Salir de pantalla completa' : 'Entrar en pantalla completa');
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === 'PageDown') { event.preventDefault(); updateMoment(current + 1); return; }
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') { event.preventDefault(); updateMoment(current - 1); return; }
    if (event.key === 'Home') { event.preventDefault(); updateMoment(1); return; }
    if (event.key === 'End') { event.preventDefault(); updateMoment(7); return; }
    if (event.key.toLowerCase() === 'r') { event.preventDefault(); resetCurrent(); return; }
    if (event.key === ' ' || event.key === 'Enter') {
      if (event.target.matches('button, input, textarea, select')) return;
      event.preventDefault(); advanceInner();
    }
  });
  // Headings are not interactive, but focus them on navigation for a readable
  // announcement in assistive technology without adding a focus trap.
  moments.forEach(moment => moment.querySelector('h1, h2')?.setAttribute('tabindex', '-1'));
  document.querySelectorAll('.demo-config, .baseline-strip, .rule-reveal, .holdout-strip').forEach(el => el.setAttribute('tabindex', '-1'));
  document.querySelector('.demo-table')?.classList.add('is-interactive');
  resetInner(2);
  updateMoment(1, { focus: false });
})();
