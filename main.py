import os
import re
import shutil
from string import ascii_uppercase
from xml.etree import ElementTree as ET

PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""


def fix_path(*strings):
    """
    Replaces a backward slash with forward slash if the current system is windows otherwise returns the list of strings as is

    Args:
        *strings (str): Multiple string arguments representing parts of a file path.

    Returns:
        str: A combined and fixed file path.
    """
    return list(map(lambda x: x.replace("\\", "/"), strings)) if strings[0] in ["nt", "java"] else strings


class IconPackGeneration:
    def __init__(

        self,
        new_path,
        old_path,
        default_files_to_ignore=None,
    ):
        """
        Initializes the IconPackGeneration class.

        Args:
            new_path (str): Path to the new icons.
            old_path (str): Path to the old icons.
            default_files_to_ignore (list, optional): List of files to ignore. Defaults to None.
        """
        if default_files_to_ignore is None:
            default_files_to_ignore = [
                "app_splash_screen_picture.png",
                "main.py",
                "default_wall.png",
                ".vscode",
                ".gitignore",
                "drawable.txt",
                "iconpack.txt",
                ".git",
                "ic_splash_screen1.png",
                "ic_splash_screen.png",
                "clock_bg.png",
                "clock_minute.png",
                "clock_hour.png",
                "pd_logo.png",
                "home_image.png",
                "nav_bar.png",
            ]
        self.new_path = (
            new_path
        )
        self.old_path = old_path
        self.ignored_files = default_files_to_ignore
        self.new_files = []
        self.old_files = []

    def generate(self, dashboard="candybar"):
        """Calls the generate_drawable and iconpack functions based on the given dashboard
        Args:
            dashboard (str, optional): Type of dashboard. Can be 'candybar' or 'blueprint'. Defaults to 'candybar'."""
        if dashboard == "candybar":
            self.generate_drawable_candybar()
        else:
            self.generate_drawable_blueprint()
            self.generate_iconpack()

    def generate_drawable_candybar(self):
        """Creates an XML for all the images in self.new_files and self.old_files objects, for 'candybar' dashbaord"""
        root = ET.Element("resources")
        ver = ET.SubElement(root, "version").text = "1"
        root.append(ET.Comment(""))
        ET.SubElement(root, "category", title="New")
        root.append(ET.Comment(""))
        for i in self.new_files:
            ET.SubElement(root, "item", {"drawable": i})
        else:
            root.append(ET.Comment(""))

        for i in ascii_uppercase:
            ET.SubElement(root, "category", title=i).tail = "\n "
            root.append(ET.Comment(""))
            for j in self.old_files:
                if j != "":
                    if j[0].upper() == i:
                        ET.SubElement(root, "item", {"drawable": j})
                else:
                    root.append(ET.Comment(""))
            root.append(ET.Comment(""))
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write("drawable.xml", encoding="utf-8", xml_declaration=True)

    def generate_drawable_blueprint(self):
        """Creates an XML for all the images in self.new_files and self.old_files objects, for 'blueprint' dashbaord"""
        root = ET.Element("resources")
        ver = ET.SubElement(root, "version").text = "1"
        root.append(ET.Comment(""))
        ET.SubElement(root, "category", title="New")
        root.append(ET.Comment(""))
        for i in self.new_files:
            ET.SubElement(root, "item", {"drawable": i})
        else:
            root.append(ET.Comment(""))
        ET.SubElement(root, "category", title="All")
        root.append(ET.Comment(""))
        for i in sorted(self.new_files + self.old_files):
            ET.SubElement(root, "item", {"drawable": i})
        else:
            root.append(ET.Comment(""))
        for i in ascii_uppercase:
            ET.SubElement(root, "category", title=i).tail = "\n "
            for j in self.old_files:
                if j != "":
                    if j[0].upper() == i:
                        ET.SubElement(root, "item", {"drawable": j})
                else:
                    root.append(ET.Comment(""))
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write("drawable.xml", encoding="utf-8", xml_declaration=True)

    def generate_iconpack(self):
        """Creates iconpack.xml for all the images in self.new_files and self.old_files objects, for 'blueprint' dashbaord"""
        all_files = sorted(self.new_files + self.old_files)
        root = ET.Element(
            "resources",
            attrib={
                "xmlns:tools": "http://schemas.android.com/tools",
                "tools:ignore": "ExtraTranslation",
            },
        )
        root.append(ET.Comment(""))
        # self.load_files() redundant line already called in the main
        ET.SubElement(root, "string-array", {"name": "icon_preview"})
        root.append(ET.Comment(""))
        for i in all_files:
            ET.SubElement(root, "item").text = i
        root.append(ET.Comment(""))
        ET.SubElement(root, "string-array", {"name": "icon_filters"})
        root.append(ET.Comment(""))
        ET.SubElement(root, "item").text = "New"
        ET.SubElement(root, "item").text = "All"
        for i in ascii_uppercase:
            ET.SubElement(root, "item").text = i
        root.append(ET.Comment(""))
        ET.SubElement(root, "string-array", {"name": "New"})
        root.append(ET.Comment(""))
        for i in self.new_files:
            ET.SubElement(root, "item").text = i
        ET.SubElement(root, "string-array", {"name": "All"})
        root.append(ET.Comment(""))
        for i in all_files:
            ET.SubElement(root, "item").text = i
        root.append(ET.Comment(""))
        for i in ascii_uppercase:
            ET.SubElement(root, "string-array", {"name": i})
            root.append(ET.Comment(""))
            for j in self.old_files:
                if j != "":
                    if j[0].upper() == i:
                        ET.SubElement(root, "item").text = j
            root.append(ET.Comment(""))
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write("iconpack.xml", encoding="utf-8", xml_declaration=True)

    def load_files(self, with_extensions=False):
        """
        Loads the files from specified paths.

        Args:
            with_extensions (bool, optional): Whether to include file extensions. Defaults to False.
        """
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

    def copy_files(self):
        """
        Copies the files from the old path to the new path.
        """
        for name in self.new_files:
            try:
                shutil.copyfile(
                    f"{self.new_path}/{name}.png", f"{self.old_path}/{name}.png"
                )
            except shutil.SameFileError:
                print("File Already Exists: {name}.png\n")


if __name__ == "__main__":
    new_icon_pack = IconPackGeneration(
        *fix_path(r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\glassicons new",
                  r"C:\Users\prabh\OneDrive\Desktop\GlassiCons Apps\Glassicons Pro\app\src\main\res\drawable-nodpi")
    )

    new_icon_pack.load_files()
    new_icon_pack.generate()
    # new_icon_pack.copy_files()
