# poolsideaz

The website for [poolsideaz.com](https://poolsideaz.com).

- `docs/index.html` is the published site. GitHub Pages serves the `docs` folder from the `main` branch.
- `page.html` is the source for the page (styles, content, and scripts in one file).
- `build.py` wraps `page.html` into `docs/index.html` with the page head (title, description, icon).

To change the site: edit `page.html`, run `python3 build.py`, and commit both files. GitHub Pages republishes on every push to `main`.
