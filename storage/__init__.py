import sys
import os
import ssl
import urllib
import socketserver
import zipfile
import random
import xml.etree.ElementTree as Tree
import urllib.request
import bs4

class Storage:

    def __init__(self, path, root_tag="PayloadStorage"):
        #Set the path of the xml document
        self.__path = path
        #Set the root tag value
        self.__root_tag = root_tag
        #Check if the xml file path exists
        if(os.path.exists(self.__path)):
            self.__document = Tree.parse(self.__path).getroot()
        else:
            #If the file does not exist, create a new root element
            self.__document = Tree.Element(self.__root_tag)
    
    def write_node(self, tag, attribute_keys=None, attribute_values=None):
        new_element = Tree.SubElement(self.__document, tag)
        #Check if the attribute keys and values are not none
        if(attribute_keys is not None and attribute_values is not None):
            #If so, loop through the keys
            for key in attribute_keys:
                #Get the current key's index
                key_index = attribute_keys.index(key)
                #Get the value of our key knowing the index
                value = attribute_values[key_index]
                #Set the attributes given the new_element element
                new_element.set(key, value)
        #Get the content as string
        __content = Tree.tostring(self.__document, encoding='utf8', method='xml')
        #Open the file for writing
        __file = open(self.__path, "wb")
        #Write the bytes
        __file.write(__content)
        #Flush the file
        __file.flush()
        #Close the file
        __file.close()
        #Return the new_element
        return new_element
    
    def get_node(self, tag):
        #Find the node given our tag
        __nodes = self.__document.findall(tag)
        #Return the nodes
        return __nodes

    def get_attribute_value(self, tag, attribute_key):
        #Get the tag as a node
        __nodes = self.__document.findall(tag)
        #Create a list of nodes
        __attribute_values = list()
        #Loop through the array
        for __node in __nodes:
            #Check if the attribute value is not none
            if(__node.get(attribute_key)):
                #Update the attribute values list
                __attribute_values.append(__node.get(attribute_key))
        #Return the attribute values
        return __attribute_values
    
    def get_node_from_site(self, url, tag):
        #Get the xml source code from the url
        __source = urllib.request.urlopen(url).read()
        #Open the source as a tree
        tree = Tree.fromstring(__source)
        #Return all of the nodes
        return tree.findall(tag)
        
    
    def get_attribute_from_site(self, url, tag, key):
        if(str(url).startswith("http") is False):
            url = "http://" + url
        #Open the url for reading, and read it
        __source = urllib.request.urlopen(url).read()
        #Use beautifulsoup for getting the xml code
        __tree = Tree.fromstring(__source)
        #Find all elements with the given tag
        __elements = __tree.findall(tag)
        #Create an empty element list
        __attribute_list = list()
        #Loop through all elements
        for element in __elements:
            if(element.get(key)):
                #Append the attribute list
                __attribute_list.append(element.get(key))
        #Return the attribute list
        return __attribute_list