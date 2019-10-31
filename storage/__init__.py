import sys
import os
import xml.etree.ElementTree as Tree
import urllib.request as url

class Storage:
    def __init__(self, path, root_tag="Station"):
        path = str(path)
        #Instantiate the path variable for class use
        self.__path = path
        #Check if the path is a url
        if(path.startswith("http")):
            #Open the given website
            __page = url.urlopen(path)
            #Create our document element using urllib
            self.__document = Tree.fromstring(__page.read().decode("utf-8"))
        elif(os.path.exists(path)):
            #Create our document by parsing our path and getting the root element
            self.__document = Tree.parse(self.__path).getroot()
        else:
            #Create our document by initiating a root element
            self.__document = Tree.Element(root_tag)
    def add_element(self, tag, value, attribute_keys=None, attribute_values=None):
        #Create a child element
        __child = Tree.SubElement(self.__document, tag)
        #Check if the attribute set is not null
        if(attribute_keys is not None and attribute_values is not None):
            #Loop through the attribute key set
            for __key in attribute_keys:
                #Get the index
                __index = attribute_keys.index(__key)
                #Get the value at the given index
                __value = attribute_values[__index]
                #Add the key value pair
                __child.set(__key, __value)
        #Check if the value is not none
        if(value is not None):
            #Set the value of our child element
            __child.set("value", value)
        #Get the content as a string
        __content = Tree.tostring(self.__document)
        #Open the file and write the content
        __file = open(self.__path, "wb")
        #Write the content
        __file.write(__content)
        #Flush the file
        __file.flush()
        #Close the file
        __file.close()

    def get_value(self, tag):
        #Find the element with the given tag
        __element = self.__document.find(tag)
        #Return the value of our element
        return __element.get("value")
    
    def get_attribute(self, tag, attribute_key):
        #Find the element with the given tag
        __element = self.__document.find(tag)
        #Return the value of our element
        return __element.get(attribute_key)
    
    def get_all_elements(self, tag):
        #Return all of our elements with the given tag
        return self.__document.findall(tag)

    def get_all_attribute_values(self, tag, attribute_key):
        #Find all of the elements
        __elements = self.__document.findall(tag)
        #Create a list variable for the elements + attribute values
        __element_attribute_pairs = list()
        #Loop through all of the elements
        for __element in __elements:
            #Check if our attribute exists in the element
            if(__element.get(attribute_key)):
                #Add the element to our element attribute pair
                __element_attribute_pairs.append(__element)
                #Add the attribute's value to our list
                __element_attribute_pairs.append(__element.get(attribute_key))
        #Return the attribute pairs
        return __element_attribute_pairs