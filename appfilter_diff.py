import xml.etree.ElementTree as ET
import os


icon_path="/Users/prabhjotsingh/Desktop/fiona exports"
#Extracting all the icon names from the appfilter.xml file
tree=ET.parse("./appfilter.xml")
root=tree.getroot()
appfilter_file=[]
for i in root.findall("item"):
    appfilter_file.append(i.get("drawable"))
appfilter_file=set(appfilter_file)

icon_files=set(map(lambda x: x.replace(".png",""),os.listdir(icon_path)))
print(f"Difference: {len(appfilter_file.difference(icon_files))}")
