import os
import sys
from string import ascii_uppercase, punctuation


class IconPack:
    def __init__(self,new_path,old_path,default_files_to_ignore=["app_splash_screen_picture.png","main.py","default_wall.png"]):
        self.new_path = new_path
        self.old_path = old_path
        self.ignored_files =default_files_to_ignore
        self.new_files = []
        self.old_files = []
        
    
    def generate(self):
        ...
        
        
    def load_files(self,with_extensions=False):
        self.new_files=os.listdir(self.new_path)
        self.old_files=os.listdir(self.old_path)
        self.new_files=list(filter(lambda x:x not in self.ignored_files,self.new_files))
        self.old_files=list(filter(lambda x:x not in self.ignored_files,self.old_files))
        if not with_extensions:
            self.new_files=list(map(lambda x:x.split(".")[0],self.new_files))
            self.old_files=list(map(lambda x:x.split(".")[0],self.old_files))
    
    
    @staticmethod
    def check_name(name):
        for i in ascii_uppercase+punctuation:
            if i in name:
                return False
        return True
    
    
    def change_name(self):
        for names in self.new_files:
            if not self.check_name(names):
                user_input=input("Please Enter a name: ")
                os.rename(f"{self.new_path}/{names}.png",f"{self.new_path}/{user_input}.png")
            
if __name__=='__main__':
    new_icon_pack=IconPack('E:/GlassiCons Apps/Fiesta New','E:/GlassiCons Apps/Blueprint-sample (1)/Blueprint-sample/app/src/main/res/drawable-nodpi')
    new_icon_pack.load_files()
    print((new_icon_pack.old_path))