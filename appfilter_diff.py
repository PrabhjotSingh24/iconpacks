import xml.etree.ElementTree as ET
from main import IconPack, fix_path


class IconPackDiff(IconPack):
    def __init__(self, new_path, old_path, appfilter_path):
        super().__init__(new_path, old_path)
        super().load_files()
        self.appfilter_path = appfilter_path

    def find_diff(self):

        tree = ET.parse(self.appfilter_path)
        root = tree.getroot()
        appfilter_file = []
        for i in root.findall("item"):
            appfilter_file.append(i.get("drawable"))
        appfilter_file = set(appfilter_file)
        with open("./difference.txt", "w", encoding="utf-8") as f:
            for i in sorted(list(appfilter_file.difference(set(self.new_files)))):
                f.write(f"{i}\n")


icon_diff = IconPackDiff(
    *fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\drawable-nodpi",
              r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\drawable-nodpi",
              r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\xml\appfilter.xml"))
icon_diff.find_diff()
