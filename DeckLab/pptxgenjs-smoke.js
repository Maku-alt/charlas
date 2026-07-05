const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");

const outDir = __dirname;
const assetPath = path.join(outDir, "smoke-asset.png");
const outPath = path.join(outDir, "pptxgenjs-smoke.pptx");

if (!fs.existsSync(assetPath)) {
  throw new Error(`Missing asset: ${assetPath}`);
}

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Codex smoke test";
pptx.company = "charlas";
pptx.subject = "PptxGenJS PowerPoint compatibility smoke";
pptx.title = "PptxGenJS smoke";
pptx.lang = "es-PE";
pptx.theme = {
  headFontFace: "Georgia",
  bodyFontFace: "Calibri",
  lang: "es-PE"
};
pptx.defineLayout({ name: "WIDE", width: 13.333, height: 7.5 });
pptx.layout = "WIDE";

const C = {
  bg: "F4F0E8",
  ink: "0F172A",
  muted: "475569",
  blue: "102A43",
  orange: "C75C2A",
  green: "2D6A4F",
  white: "FFFDF8",
  sand: "EADBC8"
};

function addHeader(slide, kicker, title) {
  slide.background = { color: C.bg };
  slide.addShape(pptx.ShapeType.rect, {
    x: 0.45,
    y: 0.32,
    w: 1.25,
    h: 0.08,
    fill: { color: C.orange },
    line: { color: C.orange }
  });
  slide.addText(kicker.toUpperCase(), {
    x: 0.55,
    y: 0.58,
    w: 2.8,
    h: 0.25,
    fontFace: "Consolas",
    fontSize: 9,
    bold: true,
    color: C.orange,
    margin: 0
  });
  slide.addText(title, {
    x: 0.55,
    y: 0.9,
    w: 8.9,
    h: 0.72,
    fontFace: "Georgia",
    fontSize: 29,
    bold: true,
    color: C.ink,
    breakLine: false,
    margin: 0.02,
    fit: "shrink"
  });
}

function addFooter(slide, text) {
  slide.addText(text, {
    x: 0.55,
    y: 7.08,
    w: 6,
    h: 0.18,
    fontFace: "Consolas",
    fontSize: 7.5,
    color: C.muted,
    margin: 0
  });
}

let slide = pptx.addSlide();
slide.background = { color: C.blue };
slide.addText("PRUEBA LOCAL", {
  x: 0.65,
  y: 0.65,
  w: 2.2,
  h: 0.22,
  fontFace: "Consolas",
  fontSize: 10,
  bold: true,
  color: "E07A3F",
  margin: 0
});
slide.addText("¿PptxGenJS abre limpio en PowerPoint nativo?", {
  x: 0.65,
  y: 1.15,
  w: 8.0,
  h: 1.4,
  fontFace: "Georgia",
  fontSize: 34,
  bold: true,
  color: C.white,
  margin: 0.02,
  fit: "shrink"
});
slide.addText("Tildes: conversación, análisis, revisión, pequeños, documentación.", {
  x: 0.7,
  y: 3.02,
  w: 5.7,
  h: 0.55,
  fontFace: "Calibri",
  fontSize: 18,
  color: C.white,
  margin: 0.04,
  fit: "shrink"
});
slide.addImage({ path: assetPath, x: 8.35, y: 1.0, w: 3.6, h: 4.8 });
addFooter(slide, "pptxgenjs-smoke / slide 1");

slide = pptx.addSlide();
addHeader(slide, "comparación", "El renderer debe resolver estructura sin pedir razonamiento al LLM");
const panels = [
  ["Antes", "Agente interpreta specs, diseña, genera, revisa y corrige."],
  ["Después", "Un JSON alimenta layouts fijos y el script produce el PPTX."],
  ["Riesgo", "Si PowerPoint rechaza el archivo, el renderer no sirve para este repo."]
];
panels.forEach((p, idx) => {
  const x = 0.75 + idx * 4.1;
  slide.addShape(pptx.ShapeType.roundRect, {
    x,
    y: 2.05,
    w: 3.45,
    h: 2.45,
    rectRadius: 0.08,
    fill: { color: C.white },
    line: { color: C.sand, width: 1.1 }
  });
  slide.addText(p[0], {
    x: x + 0.28,
    y: 2.32,
    w: 2.85,
    h: 0.32,
    fontFace: "Georgia",
    fontSize: 19,
    bold: true,
    color: idx === 2 ? "B42318" : C.blue,
    margin: 0
  });
  slide.addText(p[1], {
    x: x + 0.28,
    y: 2.92,
    w: 2.78,
    h: 0.95,
    fontFace: "Calibri",
    fontSize: 14,
    color: C.ink,
    breakLine: false,
    fit: "shrink",
    margin: 0.04
  });
});
slide.addShape(pptx.ShapeType.line, {
  x: 1.0,
  y: 5.25,
  w: 11.2,
  h: 0,
  line: { color: C.orange, width: 2 }
});
slide.addText("Criterio de aceptación: PowerPoint COM debe abrir y exportar PNG sin reparar el archivo.", {
  x: 1.0,
  y: 5.48,
  w: 10.4,
  h: 0.45,
  fontFace: "Calibri",
  fontSize: 17,
  bold: true,
  color: C.ink,
  margin: 0.02,
  fit: "shrink"
});
addFooter(slide, "pptxgenjs-smoke / slide 2");

slide = pptx.addSlide();
addHeader(slide, "cierre", "Si esta prueba falla, no insistimos con PptxGenJS para decks nuevos");
slide.addShape(pptx.ShapeType.rect, {
  x: 0.0,
  y: 4.55,
  w: 13.333,
  h: 2.95,
  fill: { color: C.blue },
  line: { color: C.blue }
});
slide.addText("Decisión técnica basada en apertura nativa, no en esperanza.", {
  x: 0.78,
  y: 5.18,
  w: 8.2,
  h: 0.82,
  fontFace: "Georgia",
  fontSize: 27,
  bold: true,
  color: C.white,
  margin: 0.02,
  fit: "shrink"
});
slide.addText("El objetivo es bajar tokens: contenido con LLM, producción con código.", {
  x: 0.82,
  y: 6.15,
  w: 7.7,
  h: 0.35,
  fontFace: "Calibri",
  fontSize: 16,
  color: "EADBC8",
  margin: 0
});
slide.addImage({ path: assetPath, x: 9.35, y: 4.78, w: 2.65, h: 2.05 });
addFooter(slide, "pptxgenjs-smoke / slide 3");

pptx.writeFile({ fileName: outPath })
  .then(() => {
    console.log(outPath);
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
