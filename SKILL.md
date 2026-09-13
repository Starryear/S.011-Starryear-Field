---
name: four-panel-photo-distillation
description: Transform one user photograph into a vertical 2:3 editorial 2×2 quartet with a crop-only Evidence cell, a magnified abstract detail, a minimal structural reduction, and a dreamy optical afterimage. Use for 四拼、四宫格海报、照片四格抽象, or source-derived editorial abstraction. Do not use for multi-photo collages, four filters, comics, or unrelated image grids.
metadata:
  author: "Starryear年"
  version: "1.2.3"
  license: "Starryear Personal and Non-commercial Use License"
---

# 四拼·照片蒸馏

Create one finished 2:3 portrait bitmap from exactly one authorized source photograph. Use the fixed sequence `Evidence → Magnified Abstraction → Minimal Structure → Dream Afterimage`. This sequence defines the transformation style only; re-derive every subject, palette, lighting relationship, motif, and direction from the current source photograph.

## Workflow

1. Inspect the source once and lock three to six facts: factual anchor, dominant spatial relationship, transferable motif, darkest/lightest distribution, source palette, and emotional temperature.
2. Protect one Evidence cell with actual source pixels. It may be proportionally scaled and cropped only: never regenerate, recolor, retouch, relight, clean up, extend, or otherwise alter it.
3. Build upper-right as a magnified abstract detail: expand one source-specific texture, edge, contour, gap, reflection, or material transition into a large field without repeating the complete subject.
4. Build lower-left as minimal structure: reduce the source to the fewest lines, dots, bands, arcs, blocks, intervals, or negative-space divisions needed to preserve its spatial logic. Keep it crisp, sparse, flat, and quiet, but keep its field color, value family, and accent hue inside the quartet's shared source-derived palette. It must not read as a separately art-directed poster.
5. Build lower-right as a dream afterimage: transform source-supported light, motion, blur, reflection, atmosphere, or material into a radiant spatial echo using optical bloom, refraction, translucent drift, bokeh, stretched light, or dissolving edges. Keep it dreamlike without importing fantasy objects.
6. Generate and compose every cell as an exact 2:3 portrait image. Arrange four equal-size 2:3 cells in reading order on a clear 2×2 grid: Evidence upper-left, Magnified Abstraction upper-right, Minimal Structure lower-left, Dream Afterimage lower-right. Because both axes double equally, the assembled quartet must also remain exactly 2:3 portrait.
7. Carry two to four pieces of source DNA across at least three cells: contour or axis, interval, negative-space ratio, material cue, source hue, or accent hue. Before generating, lock one shared palette bridge: one dominant field family, one dark anchor, and one or two accents sampled from the source. Use that bridge in all three generated cells, with the lower-left reusing at least two of those color roles.
8. Generate only the three transformed cells, each at 2:3 portrait (preferably 1024×1536 or 2048×3072). Then use [scripts/assemble_quartet.py](scripts/assemble_quartet.py) to crop the untouched source into a 2:3 Evidence cell and assemble all four cells. Never ask the image model to recreate the Evidence cell, and never use square or landscape intermediate cells.
9. Return exactly one finished 2:3 image. Verify both invariants before delivery: every individual cell is 2:3, and the assembled 2×2 quartet is 2:3. Review it at full size and thumbnail size; revise if the ratio, sequence, source relationship, palette fidelity, functional separation, or visual balance is unclear.

## Image 2.5 Anti-Fish-Scale Rendering

- Treat dirty fish-scale texture as a generation defect, not as desirable painterly detail. Suppress repeated scallops, overlapping scale-like dabs, tiny leaf-shaped strokes, dense short ripples, stippled clumps, cellular mottling, and evenly distributed high-frequency marks.
- Build surfaces from a few broad value masses, long directional strokes, smooth translucent washes, calm negative space, and deliberately limited texture zones. Use larger brush logic and wider spacing between marks.
- State the anti-pattern explicitly in every generated-cell prompt: `no fish-scale pattern, no repeated scalloped dabs, no dense tiny strokes, no cellular mottling, no all-over texture noise`.
- Keep at least 60% of every generated cell visually calm at medium viewing size. Concentrate tactile detail only near one focal transition; do not distribute it uniformly across water, foliage, feathers, sky, walls, or paper.
- For water, use a small count of broad reflection bands or long soft trails rather than many short horizontal dashes. For foliage, prefer fused shadow masses and a few large leaf groups rather than countless small leaf marks. For feathers, prefer continuous luminous planes and a few directional edges rather than repeated scale-like feather tiles.
- Inspect at 100% and at thumbnail size. Regenerate a cell if texture forms dirty mesh, fish scales, worms, pebbled skin, or repetitive AI brush tiles, even when the subject and composition are otherwise correct.

## Guardrails

- Derive every major form, rhythm, hue, and material cue from visible source evidence; do not add stock moons, birds, flowers, symbols, or decorative geometry without a source basis.
- Match the source's color energy, not a default house palette. A bright, luminous, saturated, cool, or high-key source must not be flattened into beige, gray, dusty paper, or automatic low saturation.
- Judge color at quartet level before judging any cell alone. The lower-left may be flatter and quieter, but it must not introduce a new background cast, isolated complementary scheme, or unmatched saturation/value range. If it looks pasted in at thumbnail size, recolor that cell from the locked shared palette without changing its sparse structural role.
- Do not make four filtered copies or four literal redraws. Recognition should survive through changed representational distance.
- Reject three abstract cells that reuse the same silhouette, medium, density, or compositional gesture. Shared DNA is required; repeated depiction is not.
- Treat any supplied reference quartet as transformation grammar only. Never borrow its subject, palette, lighting, concrete motif, or decorative details unless independently present in the current source.
- The second cell must read as close and magnified, the third as sparse and minimal, and the fourth as dreamy and optical. Do not exchange these roles.
- Preserve faces, gestures, animal identity, architectural load and perspective, meaningful object counts, and defining contours whenever they are decisive evidence.
- Prefer one neutral field plus one or two source-derived accents. Reject rainbow balancing, neon outlines, unrelated fashionable palettes, glossy 3D, heavy grain, dirty parchment, drop shadows, thick borders, and uniform detail density.
- Reject fish-scale texture, scalloped brush repetition, cellular mottling, dense tiny ripple marks, and uniform high-frequency surface noise.
- Typography is optional and subordinate: one short phrase and one micro-caption at most. If reliable spelling cannot be guaranteed, omit all text. Never invent a logo, signature, watermark, date, or pseudo-language.
- No outer mockup, rounded cards, fifth panel, 1×4 strip, ambiguous mosaic, or multiple alternatives.
- No square, landscape, or mismatched-ratio cell. Do not rely on the final assembly to crop a wrongly generated cell into compliance.

## Reference Prompt

Read the appropriate full prompt before producing the image:

- Chinese: [references/four-panel-photo-distillation-prompt.zh-CN.md](references/four-panel-photo-distillation-prompt.zh-CN.md)
- English: [references/four-panel-photo-distillation-prompt.en.md](references/four-panel-photo-distillation-prompt.en.md)
- For deeper visual calibration or failure diagnosis, read [references/style-grammar.md](references/style-grammar.md). The contact sheet is observational reference only, never a template to copy.

Keep [assets/examples](assets/examples) empty during drafting and testing. Do not add reference images, test renders, temporary outputs, `.gitkeep`, or placeholders. After Starryear年 explicitly accepts the tested Skill, add only final images supplied or approved by the user; treat them as examples only and never reuse their subjects, palettes, or composition unless the user supplies that exact image.
