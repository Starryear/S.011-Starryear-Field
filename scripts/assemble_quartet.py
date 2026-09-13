#!/usr/bin/env python3
"""Assemble four 2:3 cells into one 2:3 portrait quartet."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def crop_only(image: Image.Image, size: tuple[int, int], position: tuple[float, float]) -> Image.Image:
    """Resize proportionally and crop; never alter source color or content."""
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=position)


def is_two_by_three(image: Image.Image) -> bool:
    """Return True only for an exact 2:3 portrait image."""
    return image.width * 3 == image.height * 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--essence", required=True, type=Path)
    parser.add_argument("--structure", required=True, type=Path)
    parser.add_argument("--afterimage", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--width", type=int, default=2048)
    parser.add_argument("--height", type=int, default=3072)
    parser.add_argument("--source-x", type=float, default=0.5)
    parser.add_argument("--source-y", type=float, default=0.5)
    args = parser.parse_args()

    if args.width % 2 or args.height % 2 or args.width * 3 != args.height * 2:
        raise SystemExit("Canvas must have even dimensions in an exact 2:3 ratio")
    if not 0 <= args.source_x <= 1 or not 0 <= args.source_y <= 1:
        raise SystemExit("Source centering values must be between 0 and 1")

    cell = (args.width // 2, args.height // 2)
    paths = [args.source, args.essence, args.structure, args.afterimage]
    images = []
    for index, path in enumerate(paths):
        with Image.open(path) as opened:
            if index > 0 and not is_two_by_three(opened):
                raise SystemExit(
                    f"Generated cell must be exact 2:3 portrait: {path} "
                    f"is {opened.width}x{opened.height}"
                )
            rgb = opened.convert("RGB")
            center = (args.source_x, args.source_y) if index == 0 else (0.5, 0.5)
            images.append(crop_only(rgb, cell, center))

    canvas = Image.new("RGB", (args.width, args.height))
    for image, xy in zip(images, [(0, 0), (cell[0], 0), (0, cell[1]), cell]):
        canvas.paste(image, xy)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
