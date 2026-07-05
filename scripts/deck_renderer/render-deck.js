const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");

function usage() {
  console.error("Usage: node render-deck.js <deck-spec.json> <output.pptx> [--theme theme.json]");
  process.exit(2);
}

const args = process.argv.slice(2);
if (args.length < 2) usage();

const specPath = path.resolve(args[0]);
const outPath = path.resolve(args[1]);
const themeFlag = args.indexOf("--theme");
const themePath = themeFlag >= 0 && args[themeFlag + 1]
  ? path.resolve(args[themeFlag + 1])
  : path.join(__dirname, "theme-charlas.json");

const specDir = path.dirname(specPath);
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
const defaultTheme = JSON.parse(fs.readFileSync(themePath, "utf8"));
const T = { ...defaultTheme, ...(spec.theme || {}) };

const SLIDE_W = 13.333;
const SLIDE_H = 7.5;

function fail(message) {
  throw new Error(message);
}

function requireField(obj, field, context) {
  if (obj[field] === undefined || obj[field] === null || obj[field] === "") {
    fail(`${context} missing required field: ${field}`);
  }
}

function resolveAsset(name) {
  if (!name) fail("Missing asset name");
  const candidates = [
    path.resolve(specDir, name),
    path.resolve(specDir, "assets", name),
    path.resolve(__dirname, name)
  ];
  const found = candidates.find((p) => fs.existsSync(p));
  if (!found) fail(`Missing asset: ${name}. Tried: ${candidates.join(", ")}`);
  return found;
}

function makePptx() {
  const pptx = new pptxgen();
  pptx.defineLayout({ name: "WIDE", width: SLIDE_W, height: SLIDE_H });
  pptx.layout = "WIDE";
  pptx.author = spec.meta?.author || "charlas";
  pptx.company = "charlas";
  pptx.subject = spec.meta?.subtitle || spec.meta?.title || "charlas deck";
  pptx.title = spec.meta?.title || "charlas deck";
  pptx.lang = T.lang || "es-PE";
  pptx.theme = {
    headFontFace: T.headFont,
    bodyFontFace: T.bodyFont,
    lang: T.lang || "es-PE"
  };
  pptx.margin = 0;
  return pptx;
}

const pptx = makePptx();

function bg(slide, color = T.background) {
  slide.background = { color };
}

function rect(slide, x, y, w, h, color, line = color, radius = false) {
  slide.addShape(radius ? pptx.ShapeType.roundRect : pptx.ShapeType.rect, {
    x, y, w, h,
    rectRadius: radius ? 0.08 : undefined,
    fill: { color },
    line: { color: line, width: 1 }
  });
}

function line(slide, x, y, w, color = T.orange, width = 2) {
  slide.addShape(pptx.ShapeType.line, {
    x, y, w, h: 0,
    line: { color, width }
  });
}

function text(slide, value, x, y, w, h, opts = {}) {
  slide.addText(String(value ?? ""), {
    x, y, w, h,
    fontFace: opts.font || T.bodyFont,
    fontSize: opts.size || 14,
    bold: !!opts.bold,
    italic: !!opts.italic,
    color: opts.color || T.ink,
    align: opts.align || "left",
    valign: opts.valign || "top",
    margin: opts.margin ?? 0.03,
    fit: opts.fit || "shrink",
    paraSpaceAfterPt: opts.paraSpaceAfterPt ?? 0,
    breakLine: false
  });
}

function header(slide, s) {
  requireField(s, "kicker", "slide");
  requireField(s, "title", "slide");
  bg(slide);
  rect(slide, 0.55, 0.34, 1.25, 0.08, T.orange);
  text(slide, s.kicker.toUpperCase(), 0.62, 0.58, 3.2, 0.22, {
    font: T.monoFont, size: 8.5, bold: true, color: T.orange, margin: 0
  });
  text(slide, s.title, 0.62, 0.86, 9.85, 0.78, {
    font: T.headFont, size: 27, bold: true, color: T.ink, margin: 0.01
  });
}

function footer(slide, idx) {
  text(slide, `charlas / ${idx + 1}`, 0.62, 7.08, 2.5, 0.16, {
    font: T.monoFont, size: 7.5, color: T.muted, margin: 0
  });
}

function bulletList(slide, items, x, y, w, h, color = T.ink) {
  const value = (items || []).map((item) => `\u2022 ${item}`).join("\n");
  text(slide, value, x, y, w, h, {
    font: T.bodyFont, size: 13.3, color, margin: 0.03
  });
}

const layouts = {
  cover(slide, s, idx) {
    requireField(s, "title", "cover slide");
    bg(slide, T.blue);
    rect(slide, 0, 0, SLIDE_W, SLIDE_H, T.blue);
    rect(slide, 0.0, 0, 0.26, SLIDE_H, T.orange);
    text(slide, (s.kicker || "charla").toUpperCase(), 0.72, 0.72, 3.3, 0.25, {
      font: T.monoFont, size: 10, bold: true, color: T.orange2, margin: 0
    });
    text(slide, s.title, 0.7, 1.18, 7.05, 1.55, {
      font: T.headFont, size: 35, bold: true, color: T.white, margin: 0.01
    });
    text(slide, s.subtitle || spec.meta?.subtitle || "", 0.75, 3.25, 5.9, 0.72, {
      size: 17, color: T.sand, margin: 0.02
    });
    if (s.image) slide.addImage({ path: resolveAsset(s.image), x: 8.25, y: 0.75, w: 3.95, h: 5.25 });
    text(slide, spec.meta?.date || "", 0.75, 6.82, 2.5, 0.2, {
      font: T.monoFont, size: 8, color: T.sand, margin: 0
    });
    footer(slide, idx);
  },

  thesis(slide, s, idx) {
    requireField(s, "statement", "thesis slide");
    header(slide, s);
    rect(slide, 0.78, 2.1, 7.55, 2.2, T.white, T.sand, true);
    text(slide, s.statement, 1.08, 2.42, 6.85, 1.18, {
      font: T.headFont, size: 25, bold: true, color: T.blue, margin: 0.02
    });
    rect(slide, 8.75, 2.05, 3.25, 2.25, T.blue);
    text(slide, s.calloutLabel || "Lectura ejecutiva", 9.05, 2.38, 2.6, 0.25, {
      font: T.monoFont, size: 9, bold: true, color: T.orange2, margin: 0
    });
    text(slide, s.calloutValue || "1", 9.05, 2.75, 2.55, 0.6, {
      font: T.headFont, size: 36, bold: true, color: T.white, margin: 0
    });
    text(slide, s.calloutBody || "", 9.05, 3.48, 2.48, 0.54, {
      size: 13, color: T.sand, margin: 0.02
    });
    line(slide, 0.9, 5.1, 11.3);
    text(slide, s.takeaway || "", 0.92, 5.38, 10.3, 0.45, {
      size: 18, bold: true, color: T.ink, margin: 0.01
    });
    footer(slide, idx);
  },

  comparison(slide, s, idx) {
    requireField(s, "left", "comparison slide");
    requireField(s, "right", "comparison slide");
    header(slide, s);
    [[s.left, 0.8, T.red], [s.right, 6.95, T.green]].forEach(([side, x, accent]) => {
      rect(slide, x, 2.05, 5.55, 3.35, T.white, T.sand, true);
      rect(slide, x, 2.05, 0.12, 3.35, accent);
      text(slide, side.title, x + 0.35, 2.35, 4.55, 0.36, {
        font: T.headFont, size: 21, bold: true, color: T.blue, margin: 0
      });
      bulletList(slide, side.items || [], x + 0.38, 3.05, 4.45, 1.55);
    });
    text(slide, s.takeaway || "", 1.1, 6.08, 10.7, 0.35, {
      size: 16, bold: true, color: T.ink, margin: 0.01
    });
    footer(slide, idx);
  },

  process(slide, s, idx) {
    requireField(s, "steps", "process slide");
    header(slide, s);
    s.steps.slice(0, 4).forEach((step, i) => {
      const x = 0.75 + i * 3.1;
      rect(slide, x, 2.45, 2.45, 2.18, T.white, T.sand, true);
      rect(slide, x + 0.25, 2.78, 0.45, 0.45, i % 2 ? T.green : T.orange);
      text(slide, `${i + 1}`, x + 0.37, 2.88, 0.2, 0.18, {
        font: T.monoFont, size: 10, bold: true, color: T.white, margin: 0
      });
      text(slide, step.label, x + 0.25, 3.42, 1.9, 0.32, {
        font: T.headFont, size: 18, bold: true, color: T.blue, margin: 0
      });
      text(slide, step.body, x + 0.25, 3.98, 1.82, 0.45, {
        size: 12.5, color: T.ink, margin: 0.01
      });
      if (i < Math.min(s.steps.length, 4) - 1) line(slide, x + 2.58, 3.55, 0.35, T.orange, 1.5);
    });
    footer(slide, idx);
  },

  matrix(slide, s, idx) {
    requireField(s, "columns", "matrix slide");
    requireField(s, "rows", "matrix slide");
    header(slide, s);
    const x0 = 1.0, y0 = 2.15;
    rect(slide, x0, y0, 11.2, 3.25, T.white, T.sand, true);
    text(slide, s.firstColumn || "Modo", x0 + 0.35, y0 + 0.35, 2.0, 0.28, { font: T.monoFont, size: 9, bold: true, color: T.muted, margin: 0 });
    s.columns.forEach((c, i) => text(slide, c, x0 + 3.0 + i * 2.5, y0 + 0.35, 1.7, 0.28, {
      font: T.monoFont, size: 9, bold: true, color: T.muted, margin: 0
    }));
    s.rows.forEach((row, r) => {
      const y = y0 + 0.92 + r * 0.72;
      line(slide, x0 + 0.25, y - 0.14, 10.7, T.sand, 1);
      text(slide, row.name, x0 + 0.35, y, 2.0, 0.28, { font: T.headFont, size: 16, bold: true, color: T.blue, margin: 0 });
      row.values.forEach((v, i) => {
        const color = v === "Alta" ? T.green : v === "Baja" ? T.red : T.orange;
        rect(slide, x0 + 3.0 + i * 2.5, y - 0.02, 1.0, 0.28, color);
        text(slide, v, x0 + 3.12 + i * 2.5, y + 0.03, 0.76, 0.14, { font: T.monoFont, size: 8.5, bold: true, color: T.white, margin: 0, align: "center" });
      });
    });
    text(slide, s.takeaway || "", 1.1, 6.05, 10.3, 0.36, { size: 16, bold: true, color: T.ink, margin: 0.01 });
    footer(slide, idx);
  },

  architecture(slide, s, idx) {
    requireField(s, "nodes", "architecture slide");
    header(slide, s);
    s.nodes.slice(0, 4).forEach((node, i) => {
      const x = 0.82 + i * 3.02;
      rect(slide, x, 2.5, 2.25, 1.55, i === 1 ? T.blue : T.white, i === 1 ? T.blue : T.sand, true);
      text(slide, node.name, x + 0.2, 2.78, 1.85, 0.26, {
        font: T.monoFont, size: 12, bold: true, color: i === 1 ? T.white : T.blue, margin: 0
      });
      text(slide, node.body, x + 0.2, 3.22, 1.7, 0.35, {
        size: 11.5, color: i === 1 ? T.sand : T.ink, margin: 0.01
      });
      if (i < Math.min(s.nodes.length, 4) - 1) line(slide, x + 2.38, 3.28, 0.45, T.orange, 2);
    });
    rect(slide, 1.0, 5.25, 11.0, 0.62, T.sand, T.sand, true);
    text(slide, s.takeaway || "", 1.25, 5.43, 9.8, 0.22, {
      size: 15, bold: true, color: T.ink, margin: 0
    });
    footer(slide, idx);
  },

  evidence(slide, s, idx) {
    requireField(s, "facts", "evidence slide");
    header(slide, s);
    rect(slide, 0.85, 2.05, 4.15, 3.65, T.blue);
    text(slide, s.panelTitle || "Gate final", 1.17, 2.42, 2.5, 0.35, { font: T.headFont, size: 23, bold: true, color: T.white, margin: 0 });
    text(slide, s.panelKicker || "PowerPoint nativo", 1.18, 3.02, 2.8, 0.34, { font: T.monoFont, size: 13, bold: true, color: T.orange2, margin: 0 });
    text(slide, s.panelValue || "abre + exporta", 1.16, 3.58, 2.85, 0.55, { font: T.headFont, size: 28, bold: true, color: T.white, margin: 0 });
    bulletList(slide, s.facts, 5.55, 2.12, 6.35, 2.25);
    line(slide, 5.55, 5.18, 5.9);
    text(slide, s.takeaway || "", 5.58, 5.48, 5.5, 0.42, { size: 18, bold: true, color: T.ink, margin: 0.01 });
    footer(slide, idx);
  },

  decision(slide, s, idx) {
    requireField(s, "decision", "decision slide");
    header(slide, s);
    rect(slide, 0.9, 2.0, 6.6, 2.45, T.white, T.sand, true);
    text(slide, s.label || "Decision propuesta", 1.18, 2.3, 2.8, 0.28, { font: T.monoFont, size: 9, bold: true, color: T.orange, margin: 0 });
    text(slide, s.decision, 1.18, 2.78, 5.65, 0.95, { font: T.headFont, size: 24, bold: true, color: T.blue, margin: 0.01 });
    rect(slide, 8.05, 2.0, 3.75, 2.45, T.blue);
    text(slide, s.risksTitle || "Riesgos a probar", 8.35, 2.3, 2.3, 0.28, { font: T.monoFont, size: 9, bold: true, color: T.orange2, margin: 0 });
    bulletList(slide, s.risks || [], 8.35, 2.82, 2.65, 1.1, T.white);
    footer(slide, idx);
  },

  closing(slide, s, idx) {
    requireField(s, "title", "closing slide");
    bg(slide, T.blue);
    rect(slide, 0, 0, SLIDE_W, SLIDE_H, T.blue);
    if (s.image) slide.addImage({ path: resolveAsset(s.image), x: 7.5, y: 0.72, w: 4.3, h: 5.75 });
    text(slide, (s.kicker || "cierre").toUpperCase(), 0.75, 0.78, 2.8, 0.25, { font: T.monoFont, size: 9, bold: true, color: T.orange2, margin: 0 });
    text(slide, s.title, 0.72, 1.28, 6.0, 1.25, { font: T.headFont, size: 33, bold: true, color: T.white, margin: 0.01 });
    if (s.quote) {
      rect(slide, 0.75, 4.65, 5.95, 1.1, T.blue2, T.blue2, true);
      text(slide, s.quote, 1.05, 4.98, 5.35, 0.36, { font: T.headFont, size: 18, italic: true, color: T.sand, margin: 0.01 });
    }
    footer(slide, idx);
  }
};

if (!Array.isArray(spec.slides) || spec.slides.length === 0) {
  fail("deck-spec.json must include a non-empty slides array");
}

spec.slides.forEach((s, idx) => {
  requireField(s, "layout", `slide ${idx + 1}`);
  const render = layouts[s.layout];
  if (!render) fail(`Unsupported layout on slide ${idx + 1}: ${s.layout}`);
  const slide = pptx.addSlide();
  render(slide, s, idx);
});

fs.mkdirSync(path.dirname(outPath), { recursive: true });
pptx.writeFile({ fileName: outPath })
  .then(() => console.log(JSON.stringify({ status: "ok", pptx: outPath, slides: spec.slides.length }, null, 2)))
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
