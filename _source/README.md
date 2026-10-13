# PayCore website source

The live site at https://paycoresalarysystem.com is built from the files in this folder.
GitHub Pages ignores folders that start with `_`, so nothing here is published.

| File | What it is |
|---|---|
| `site-source.html` | The page itself: all text, styles and animations. Edit this. |
| `build.py` | Turns `site-source.html` into the live files in the repository root (adds SEO tags, structured data, sitemap). |
| `og-image.html` | Source for `og-image.png`, the preview image shown when the link is shared. |
| `shots/` | The two app screenshots used on the page. |

## To change the site
1. Edit `site-source.html`.
2. Run `python3 _source/build.py` from the repository root.
3. Commit and push. GitHub Pages updates the live site within a minute or two.

`build.py` also writes `_source/preview.html`, a single-file preview with images embedded.
To regenerate `og-image.png`, open `og-image.html` in a browser at 1200×630 and screenshot it.

Settings at the top of `build.py`: `SITE_URL` (the domain) and `DL` (where the download links point).
