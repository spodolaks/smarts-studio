# smarts.studio

Portfolio site of smArts.studio (Maria Pranka and Sergejs Podolaks), live at https://smarts.pranka.id.lv/

Static site built with Astro. No WordPress, no database.

## Branches
- `source` - this project (edit here).
- `main` - the built site that GitHub Pages serves. Never edit by hand; it is the content of `dist/` after `npm run build`.

## Run locally
    npm install
    npm run dev        # http://localhost:4321
    npm run build      # output in dist/

## Content
- `src/data/projects.json` - the 16 projects: title, text, photo order, layout mode per project.
- `src/data/captions.json` - photo titles and texts (Beloved Pics, Gaze of Mountain).
- `src/data/images.json` - width/height of every photo.
- `public/img/<id>.jpg` - full view (max 2200 px), `public/img/t/<id>.jpg` - thumbnail (max 900 px wide).
- `scripts/images.py` - makes both sizes from originals (sRGB, EXIF rotation applied).
- `scripts/subpath.mjs` - only needed if the site ever has to live in a subfolder again (`npm run build:sub`).

## Layout modes (projects.json, "mode")
auto (sliders), rows, captions (photo grid with hover text), pages (two-column page grid), grid12 (original 12-column grid).

## Contact form
Web3Forms, delivers to iampranka@gmail.com. The access key is in `.env` (public by design - it is visible in the page HTML).
