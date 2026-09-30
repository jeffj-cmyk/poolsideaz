"""Wrap page.html (the preview source) into a standalone docs/index.html for hosting."""
import pathlib, urllib.parse

root = pathlib.Path(__file__).parent
src = (root / "page.html").read_text()
head, body = src.split("<!--BODY-->", 1)

icon = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#0A7FA3"/>'
        '<circle cx="20" cy="20" r="11" fill="none" stroke="#FF6F8B" stroke-width="8"/>'
        '<circle cx="20" cy="20" r="11" fill="none" stroke="#FFFDF6" stroke-width="8" stroke-dasharray="8.64 8.64"/></svg>')
desc = ("Poolside AZ brings the all-inclusive resort to your backyard: a food and drink menu, "
        "servers at the water's edge, and a pool party that runs like a resort.")

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<meta property="og:title" content="Poolside AZ">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://poolsideaz.com/">
<link rel="canonical" href="https://poolsideaz.com/">
<link rel="icon" href="data:image/svg+xml,{urllib.parse.quote(icon)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""
out = root / "docs"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(doc)
print("wrote", out / "index.html", len(doc), "bytes")
