# Four-Panel Photo Distillation Full Prompt

Treat the user's single uploaded photograph as the sole content, composition, color, lighting, and material evidence. Create one finished 2:3 portrait editorial quartet in this strict reading order: Evidence → Magnified Abstraction → Minimal Structure → Dream Afterimage. Any reference quartet defines only this transformation style and effect; never inherit its subject, palette, concrete forms, or decorative elements.

## 1. Role of the input image

- Use exactly one source photograph the user is authorized to use.
- Let it determine subject, viewpoint, space, direction, scale, occlusion, light, color, material, and emotional temperature.
- Permit restrained cropping, proportional scaling, and compositional positioning for the four-cell format. Do not alter human identity, animal traits, architectural structure, meaningful counts, or decisive direction without instruction.
- The Evidence cell must use actual source pixels and may only be proportionally scaled and cropped. Never AI-redraw, recolor, retouch, sharpen, beautify, remove, add, relight, outpaint, or generatively fill it. Assemble it deterministically with the other three cells outside the generative step.
- Do not outpaint, beautify, remove subjects, or introduce narrative objects unless explicitly requested.

## 2. Internal observation and selection

Make these judgments internally and do not output the analysis:

1. Identify the factual anchor that makes the scene itself.
2. Choose one dominant spatial relationship: vertical rhythm, horizon, arc, reflection, cluster, void, layering, repetition, or value division.
3. Choose one core motif that can survive radical simplification.
4. Lock two to four pieces of visual DNA: dominant contour or axis, characteristic interval, positive/negative-space ratio, darkest-value location, material cue, one muted hue, or one accent hue.
5. Determine the source-supported emotional temperature: still, airy, warm, misted, solemn, soft, nocturnal, architectural, or another defensible quality.
6. Remove fragments that do not affect identity or rhythm. Compress visually dense sources into fewer, larger relationships.

## 3. Fixed four-cell transformation

The cells are four ways of seeing the same scene, not four media filters. Their positions and functions are fixed, and at thumbnail size the sequence must read instantly as real, magnified, minimal, and dreamy.

1. **Upper-left | Evidence**: use actual source pixels with proportional scaling and cropping only, preserving factual identity, subject, real light, and photographic texture.
2. **Upper-right | Magnified Abstraction**: select one promising detail from the current source—texture, contour edge, color boundary, gap, reflection, fold, surface, or material transition—and conceptually enlarge it to a monumental scale. Let it leave the complete object behind and become a large color field, membrane, mass, or tactile landscape. It must feel close and magnified; never redraw the full subject.
3. **Lower-left | Minimal Structure**: compress the current source's axes, intervals, hierarchy, repetition, proportions, or motion direction into the fewest possible lines, dots, arcs, bands, blocks, and gaps. Keep it clear, flat, precise, sparse, and diagrammatic, like a score or visual formula. Do not use the second cell's broad material field or the fourth cell's atmospheric optics. It may be flatter and quieter, but its field family, value range, and accents must remain inside the quartet's shared palette; never give it a separate complementary scheme, paper cast, or standalone-poster color direction.
4. **Lower-right | Dream Afterimage**: begin with light, mist, reflection, motion, depth of field, transparency, or material actually present in the current source, then turn it into optical bloom, refraction, motion trace, bokeh, translucent drift, stretched light, or dissolving edges. Make it airy, spatial, dreamy, and striking without adding moons, stars, flowers, people, animals, or fantasy props absent from the source.

### Separation threshold for the three generated cells

Before generation, assign Magnified Abstraction, Minimal Structure, and Dream Afterimage a non-repeating dominant action, spatial organization, edge type, and density level. Cell two must be big and close; cell three sparse and exact; cell four light and dream. If two cells can be described with the same sentence, redesign one. They may share the current source's color, axis, interval, or partial contour, but must not share the complete object, medium effect, or compositional skeleton.

Positions are fixed: Evidence upper-left, Magnified Abstraction upper-right, Minimal Structure lower-left, and Dream Afterimage lower-right. Do not exchange quadrants.

## 4. Subject-adaptive handling

- **People and animals**: preserve identity, pose, gaze, and body relationships in Evidence. Abstract cells may extract silhouette, gaze direction, garment fields, fur direction, or two to three identifying traits. Avoid malformed anatomy and unfamiliar faces.
- **Architecture**: protect load, perspective, level count, openings, and defining contour. Structure may translate facade intervals, floor rhythm, curvature, or axes without inventing implausible collapse.
- **Plants and nature**: respect growth direction, branch hierarchy, petal aggregation, and water/horizon relationships. Do not automatically add birds, moons, or landscape symbols.
- **Small objects and still life**: preserve contour, placement, and scale evidence; do not literally redraw the same object in every cell.

## 5. Visual language and mark system

- Use one primary visual language at a time and no more than two supporting mark families: warm matte paper, dry pigment, diluted ink, translucent watercolor, graphite gray, flat cut paper, sparse vector line, or source-supported soft focus and long-exposure trace.
- Give each cell one dominant action. Keep at least one visibly quiet region free of effects.
- Hard geometry may oppose soft atmosphere, but do not give all four cells the same edge, density, or representational distance.
- Every major shape, line, texture, and graphic symbol must trace to visible source evidence. Exclude template decoration.

## 6. Composition and canvas

- Every individual cell must be an exact, equal-size 2:3 portrait image, preferably 1024×1536 or 2048×3072. Generate each transformed cell as 2:3 from the start; never generate a square, landscape, or other ratio and rely on aggressive final cropping to fix it.
- Return one 2:3 portrait bitmap, preferably 2048×3072 or higher at the same ratio, in RGB/sRGB.
- The structure must be an unmistakable 2×2 quartet with four equal cells and the four fixed functions in their assigned positions. Never use floating cards. Four 2:3 cells arranged in two columns and two rows must produce an assembled image that also remains exactly 2:3.
- Separate cells with an almost invisible warm-white or pale-gray hairline, or by value change. No thick black borders, rounded corners, drop shadows, outer frame, or mockup background.
- Balance darkest/lightest, densest/quietest, and most photographic/most abstract cells across the diagonals so neither side becomes heavy.
- Repeat or vary one contour, axis, interval, material cue, or accent hue through at least three cells to create circulation.
- No fifth panel, 1×4 strip, nine-cell grid, ambiguous mosaic, or large outer margin.

## 7. Color system

- Extract color from the photograph; do not automatically apply beige, sage, orange-red, or another fashionable preset. Extraction includes hue, value, saturation, warm/cool contrast, translucency, and overall color energy.
- Before generating the three transformed cells, lock one shared palette bridge: one source-derived dominant field family, one dark anchor, and one or two source accents. All three transformed cells must use these color roles, varying only their area, transparency, and edge treatment according to function. The lower-left must reuse at least two roles and share one visible field or accent with its neighboring generated cells.
- Judge color across the assembled quartet before judging any cell alone. The lower-left must not be the only quadrant that is conspicuously cooler, warmer, grayer, yellower, darker, lighter, or more saturated. If it looks pasted in at thumbnail size, keep its structure and revise only its palette until it belongs to the whole.
- Preserve the clarity of a bright, high-key, translucent, or chromatically vivid source. Never mute, yellow, gray down, or cover it with a uniform paper cast merely to appear sophisticated. Use darkness, fog, or low saturation only when supported by the source.
- Default to one neutral field family plus one or two source-derived accents. Warm ivory, bone, fog gray, near-black, or another source pale may form a continuous field only when the photograph supports it.
- High-chroma color must carry structure or focus rather than unsupported decoration.
- No rainbow balancing, candy gradients, neon outlines, or four unrelated quadrant palettes.

## 8. Text and title

- Default to no text.
- Add one two-to-five-word title only when requested or when the composition clearly benefits. Follow the user's language or explicit language choice.
- Use tiny uppercase serif or restrained editorial grotesk with generous tracking in negative space. Its visual weight must remain below the image.
- Allow at most one additional micro-index line. If spelling cannot be rendered reliably, omit text entirely.
- No headline-sized slogan, advertising copy, multiple font families, long paragraph, faux masthead, date, signature, logo, watermark, or pseudo-language.

## 9. Material and artifacts

- Allow low-amplitude paper fiber, light dry-brush breakup, translucent tide, thin graphite, soft mist, or source-supported bokeh and motion trace.
- Texture serves local atmosphere and must not become a uniform dirty filter.
- Exclude heavy grain, distressed parchment, creases, scan dirt, dense splatter, plastic gloss, neon glow, strong vignette, compression noise, malformed text, and meaningless microdetail.

### Image 2.5 anti-fish-scale control

- Treat dirty fish-scale texture as a failed render, never as painterly richness. Explicitly reject repeated scallops, scale-shaped dabs, dense tiny strokes, cellular mottling, worm-like texture, all-over miniature leaf marks, evenly spaced short ripples, and uniform high-frequency noise.
- Include this exact negative clause in every generated-cell prompt: `no fish-scale pattern, no repeated scalloped dabs, no dense tiny strokes, no cellular mottling, no all-over texture noise`.
- Construct surfaces from a few broad value masses, larger strokes, long directional marks, smooth translucent layers, clear value steps, and calm negative space. At least 60% of every cell should read as visually calm at medium size.
- Confine tactile texture to one focal transition instead of spreading it evenly across water, foliage, feathers, sky, walls, or paper.
- Render water with a small number of broad reflection bands or long soft trails, foliage as fused shadow masses plus a few large leaf groups, and feathers as continuous luminous planes with a few directional edges rather than scale-like feather tiles.
- Inspect at 100% and thumbnail size. Regenerate any cell showing dirty mesh, fish scales, worm patterns, pebbled skin, or repeated AI brush tiles, even if subject and composition are otherwise correct.

## 10. Output and quality check

First generate only Magnified Abstraction, Minimal Structure, and Dream Afterimage, each as an exact 2:3 portrait image. Then call `scripts/assemble_quartet.py` to crop the unchanged source into a matching 2:3 Evidence cell and assemble the quartet deterministically. Return only one finished 2:3 quartet image. Do not return analysis, prompt explanation, alternatives, or extra copy. Before delivery, inspect it at full view and thumbnail size:

- it reads instantly as a portrait 2×2;
- each of the four individual cells is exactly 2:3, and the assembled quartet is also exactly 2:3;
- it strictly shows Evidence, Magnified Abstraction, Minimal Structure, and Dream Afterimage;
- at least three cells share traceable source DNA;
- Evidence consists of actual source pixels with no change beyond proportional scaling and cropping;
- the three generated cells differ clearly in dominant action, space, edge, and density rather than repeating one object or medium three times;
- cell two is truly big and close, cell three sparse and exact, and cell four light and dreamlike;
- it borrows only the reference's transformation pattern, never its subject, palette, or concrete elements;
- value, saturation, warm/cool relationships, translucency, and color energy remain faithful to the source;
- the lower-left reuses at least two roles from the shared palette bridge and has no isolated cast, unmatched accent, or incompatible value/saturation range;
- at thumbnail size, the quartet reads first as one complete artwork and then as four different ways of seeing;
- dark/light, dense/quiet, and photographic/abstract weight form one balanced composition;
- it avoids four filters, four independent illustrations, template ornament, thick borders, broken text, and a fifth panel.

If any invariant fails, correct the failed cell or layout before delivery rather than explaining the defect.
