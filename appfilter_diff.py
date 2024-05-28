import xml.etree.ElementTree as ET
from main import IconPack, fix_path

icon_path = fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\drawable-nodpi")
icons = IconPack(icon_path, icon_path)
icons.load_files()
# Extracting all the icon names from the appfilter.xml file
tree = ET.parse(
    fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\xml\appfilter.xml"))
root = tree.getroot()
appfilter_file = []
for i in root.findall("item"):
    appfilter_file.append(i.get("drawable"))
appfilter_file = set(appfilter_file)

icon_files = set(map(lambda x: x.replace(".png", ""), icons.new_files))
with open("./difference.txt", "w", encoding="utf-8") as f:
    for i in sorted(list(appfilter_file.difference(icon_files))):
        f.write(f"{i}\n")
