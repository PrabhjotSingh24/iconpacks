import os
import re
import shutil
from string import ascii_uppercase
from xml.etree import ElementTree as ET

PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""

def fix_path(string):
    return string.replace("\\","/")
class IconPack:
    def __init__(
        self,
        new_path,
        old_path,
        default_files_to_ignore=[
            "app_splash_screen_picture.png",
            "main.py",
            "default_wall.png",
            ".vscode",
            ".gitignore",
            "drawable.txt",
            "iconpack.txt",
            ".git",
        ],
    ):
        self.new_path = new_path
        self.old_path = old_path
        self.ignored_files = default_files_to_ignore
        self.new_files = []
        self.old_files = []

    def generate(self):
        self.generate_drawable()
        # self.generate_iconpack()


    def generate_drawable(self):
        root=ET.Element("resources")
        ver=ET.SubElement(root,"version").text="1"
        root.append(ET.Comment(""))
        # self.load_files() redundant line already called in the main
        ET.SubElement(root,"category",title="New")
        root.append(ET.Comment(""))
        for i in self.new_files:
            ET.SubElement(root,"item",{"drawable":i})
        else:
            root.append(ET.Comment(""))
        for i in ascii_uppercase:
            ET.SubElement(root,"category",title=i).tail="\n "
            for j in self.old_files:
                if j[0].upper() == i:
                    ET.SubElement(root,"item",{"drawable":j})
            else:
                root.append(ET.Comment(""))
        tree=ET.ElementTree(root)
        ET.indent(tree)
        tree.write("drawable.xml",encoding="utf-8",xml_declaration=True)

    def generate_iconpack(self):
        all_files = sorted(self.new_files + self.old_files)
        with open("iconpack.txt", "w") as f:
            f.write(f'    <string-array name="icons_preview">\n')
            self.load_files()
            for i in all_files:
                f.write(f"        <item>{i}</item>\n")
            f.write(f"    </string-array>\n")
            ##
            f.write(f'\n    <string-array name="icon_filters">\n')
            f.write(f"        <item>New</item>\n")
            f.write(f"        <item>All</item>\n")
            for i in ascii_uppercase:
                f.write(f"        <item>{i}</item>\n")
            f.write(f"    </string-array>\n")
            ##
            f.write(f'\n    <string-array name="New">\n')
            for i in self.new_files:
                f.write(f"        <item>{i}</item>\n")
            f.write(f"    </string-array>\n")
            #!All files
            f.write(f'\n    <string-array name="All">\n')

            for i in all_files:
                f.write(f"        <item>{i}</item>\n")
            f.write(f"    </string-array>\n")
            ##
            for i in ascii_uppercase:
                f.write(f'\n    <string-array name="{i}">\n')
                for j in all_files:
                    if j[0].upper() == i:
                        f.write(f"        <item>{j}</item>\n")
                f.write(f"    </string-array>\n")

    def load_files(self, with_extensions=False):
        self.new_files = os.listdir(self.new_path)
        self.old_files = os.listdir(self.old_path)
        self.new_files = list(
            filter(lambda x: x not in self.ignored_files, self.new_files)
        )
        self.old_files = list(
            filter(lambda x: x not in self.ignored_files, self.old_files)
        )
        if not with_extensions:
            self.new_files = list(map(lambda x: x.split(".")[0], self.new_files))
            self.old_files = list(map(lambda x: x.split(".")[0], self.old_files))

    def check_name(self, name):
        if re.search("[#$%&()*+-.?@]", name) or re.search("[A-Z]", name):
            return False
        return True

#TODO: Fix how the change_name method fixes the name
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
    def copy_files(self):
        for name in self.new_files:
            try:
                shutil.copyfile(f"{self.new_path}/{name}.png",f"{self.old_path}/{name}.png")
            except shutil.SameFileError:
                print("File Already Exists: {name}.png\n")

if __name__ == "__main__":

    new_icon_pack = IconPack("/Users/prabhjotsingh/Desktop/fiona exports","/Users/prabhjotsingh/Desktop/fiona exports")
        #  fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\glassicons new"),
        # fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\glassicons\app\src\main\res\drawable-nodpi"))
        # # "E:/GlassiCons Apps/Fiesta New","E:/GlassiCons Apps/fiesta icons/Blueprint-sample/app/src/main/res/drawable-nodpi")


    new_icon_pack.load_files()
    # new_icon_pack.change_name()
    # new_icon_pack.fix_case()
    new_icon_pack.generate()
    # new_icon_pack.copy_files()
