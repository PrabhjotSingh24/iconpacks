import xml.etree.ElementTree as ET

tree=ET.parse("./drawable.xml")
root=tree.getroot()
print(root.tag)