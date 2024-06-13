import xml.etree.ElementTree as ET
from main import IconPackGeneration, fix_path
from os import path, chdir
import cv2,os,re


class IconPackTools(IconPackGeneration):
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

    def icon_dimensions(self):
        self.check_dimensions(self.new_files, self.new_path)
        if self.new_path != self.old_path:
            self.check_dimensions(self.old_files, self.old_path)

    def check_dimensions(self, files, path):
        chdir(path)
        for icons in files:
            shape = cv2.imread(f"{icons}.png").shape[:2]
            if shape != (192, 192):
                print(f"{icons}: {shape[1]}x{shape[0]}")
            else:
                ...

    def remove_icons_not_in_appfilter(self):
        ...
    def add_icons_to_another_appfilter(self):
        ...
    def change_name(self):
        for names in self.new_files:
            if not self.check_name(names):
                suggestion = names.lower()
                user_input = input(f"Please Enter a name\nSuggestion:{suggestion}\n: ")
                if user_input.lower() == "y":
                    os.rename(
                        f"{self.new_path}/{names}.png",
                        f"{self.new_path}/{suggestion}.png",
                    )
                else:
                    os.rename(
                        f"{self.new_path}/{names}.png",
                        f"{self.new_path}/{user_input}.png",
                    )

    def fix_case(self):
        for name in self.new_files:
            os.rename(
                f"{self.new_path}/{name}.png", f"{self.new_path}/{name.lower()}.png"
            )
    def check_name(self, name):
        if re.search("[#$%&()*+-.?@]", name) or re.search("[A-Z]", name):
            return False
        return True




icon_diff = IconPackTools(
    *fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\drawable-nodpi",
              r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\drawable-nodpi",
              r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\xml\appfilter.xml"))
# icon_diff.find_diff()
icon_diff.icon_dimensions()
