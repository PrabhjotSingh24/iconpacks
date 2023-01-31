import os
import sys
from string import ascii_uppercase, punctuation


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
        self.generate_iconpack()

    def generate_drawable(self):
        with open("drawable.txt", "w") as f:
            f.write(f'    <category title="New" />\n\n')
            self.load_files()
            for i in self.new_files:
                f.write(f'    <item drawable="{i}" />\n')
            #!All files
            f.write(f'\n    <category title="All" />\n\n')
            all_files = sorted(self.new_files + self.old_files)
            for i in all_files:
                f.write(f'    <item drawable="{i}" />\n')
            for i in ascii_uppercase:
                f.write(f'\n    <category title="{i}" />\n\n')
                for j in all_files:
                    if j[0].upper() == i:
                        f.write(f'    <item drawable="{j}" />\n')
    def generate_iconpack(self):
        with open("iconpack.txt", "w") as f:
            f.write(f'    <string-array name="icons_preview">\n')
            self.load_files()
            for i in self.new_files:
                f.write(f'        <item>{i}</item>\n')
            f.write(f'    </string-array>\n')
            ##
            f.write(f'\n    <string-array name="icon_filters">\n')
            f.write(f'        <item>New</item>\n')
            f.write(f'        <item>All</item>\n')
            for i in ascii_uppercase:
                f.write(f'        <item>{i}</item>\n')
            f.write(f'    </string-array>\n')
            ##
            f.write(f'\n    <string-array name="New">\n')
            for i in self.new_files:
                f.write(f'        <item>{i}</item>\n')
            f.write(f'    </string-array>\n')
            #!All files
            f.write(f'\n    <string-array name="All">\n')
            all_files = sorted(self.new_files + self.old_files)
            for i in all_files:
                f.write(f'        <item>{i}</item>\n')
            for i in ascii_uppercase:
                f.write(f'\n    <string-array name="{i}">\n')
                for j in all_files:
                    if j[0].upper() == i:
                        f.write(f'        <item>{j}</item>\n')
                f.write(f'    </string-array>\n')

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

    @staticmethod
    def check_name(name):
        for i in ascii_uppercase + punctuation:
            if i in name:
                return False
        return True

    def change_name(self):
        for names in self.new_files:
            if not self.check_name(names):
                user_input = input("Please Enter a name: ")
                os.rename(
                    f"{self.new_path}/{names}.png", f"{self.new_path}/{user_input}.png"
                )


if __name__ == "__main__":
    new_icon_pack = IconPack(
        "E:/GlassiCons Apps/Fiesta New",
        "E:/GlassiCons Apps/Blueprint-sample (1)/Blueprint-sample/app/src/main/res/drawable-nodpi",
    )
    new_icon_pack.load_files()
    new_icon_pack.generate()
