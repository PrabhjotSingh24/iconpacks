# import xml.etree.ElementTree as ET
# from string import ascii_lowercase
# import os

# tree=ET.parse("./drawable.xml")
# root=tree.getroot()
# # print(ET.tostring(root)) #returns all tags in the file
# # print(root[1].get("title")) returns the value of the attribute of the 2 element

# files=os.listdir("/Users/prabhjotsingh/Desktop/fiona exports")
# files=list(map(lambda x: x.replace(".png",""),files))
# ET.fromstring('<?xml version="1.0" encoding="utf_8"?>')
# root=ET.Element('resources')

import xml.etree.ElementTree as ET


# Create the root element
root = ET.Element("resources")

# Add child elements to the root if needed
# For example:
item1 = ET.SubElement(root, "item",{"name":"value1"})
# item1.set("name", "value1")
# item1.text = "This is item 1"
ET.Comment("you are here")
ET.indent(root)
item2=ET.SubElement(root,"item",{"name":"value2"})

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write the tree to an XML file
ET.indent(root)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)
