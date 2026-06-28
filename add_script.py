from pathlib import Path

html_file = Path("index.html")

clustrmaps_script = """<script type='text/javascript' id='mapmyvisitors' src='https://mapmyvisitors.com/map.js?cl=ffffff&w=353&t=tt&d=CuL-I4uyFN3tF2XZcj-VZgkHu1uA8SsHDV1oRI3AE1I'></script>
"""

content = html_file.read_text(encoding="utf-8")

if clustrmaps_script in content:
    print("mapmyvisitors script is already present.")
elif "</body>" in content:
    content = content.replace("</body>", clustrmaps_script + "</body>", 1)
    html_file.write_text(content, encoding="utf-8")
    print("mapmyvisitors script added successfully.")
else:
    print("Could not find </body> tag in index.html.")