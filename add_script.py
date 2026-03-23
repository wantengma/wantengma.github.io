from pathlib import Path

html_file = Path("index.html")

clustrmaps_script = """<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=300&t=tt&d=1STebnccfqr4tYKw8fWnoUDa2czj1Zj5X_jHbnl5vy8&cmn=ffb800'></script>
"""

content = html_file.read_text(encoding="utf-8")

if clustrmaps_script in content:
    print("ClustrMaps script is already present.")
elif "</body>" in content:
    content = content.replace("</body>", clustrmaps_script + "</body>", 1)
    html_file.write_text(content, encoding="utf-8")
    print("ClustrMaps script added successfully.")
else:
    print("Could not find </body> tag in index.html.")