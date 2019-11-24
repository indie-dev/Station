import sys
import os
from xml.etree import ElementTree as Tree

class Storage:
    def __init__(self, xml_path, auto_save=True):
        #Update the auto save feature
        self.__auto_save = auto_save
        #Set the path
        self.__path = xml_path
        #Check if the path exists
        if(os.path.exists(self.__path)):
            #Create a document variable
            #The value is the root of the parsed path
            self.__document = Tree.parse(self.__path).getroot()
        else:
            #Create a new element with the tag "Document"
            self.__document = Tree.Element("Document")
            #Check if its parent directory exists
            if(os.path.exists(self.__path.replace(os.path.basename(self.__path), "")) is False or os.path.isdir(self.__path.replace(os.path.basename(self.__path), "")) is False):
                #If not, make it
                os.mkdir(self.__path.replace(os.path.basename(self.__path), ""))
    
    def add_element(self, element_tag, value, attribute_keys=None, attribute_values=None):
        #Check if the path exists
        if(os.path.exists(self.__path)):
            #Create a document variable
            #The value is the root of the parsed path
            self.__document = Tree.parse(self.__path).getroot()
        else:
            #Create a new element with the tag "Document"
            self.__document = Tree.Element("Document")
        #Create a new sub element
        __element = Tree.SubElement(self.__document, element_tag)
        #Check if the attribute keys are not none
        if(attribute_keys is not None):
            #Loop through the attribute keys
            for __key in attribute_keys:
                #Get the index of the key
                __key_index = attribute_keys.index(__key)
                #Get the value associated with that index
                __value = attribute_values[__key_index]
                #Update our element
                __element.set(__key, __value)
        #Update our element with the given value
        __element.set("value", value)
        #Check if auto save is enabled
        if(self.__auto_save is True):
            #Save the document
            self.save()
        #Return the element
        return __element

    def get_element(self, element_tag):
        #Get the values
        __elements = self.__document.findall(element_tag)
        #Return the elements
        return __elements

    def get_element_value(self, element_tag):
        #Get the values
        __values = self.__document.findall(element_tag)
        #Check if our values is a list
        if("list" in str(type(__values))):
            #Create a value list
            __result = list()
            #Loop through the list
            for __value in __values:
                #Update our result array
                __result.append(__value.get("value"))
            #Return the result
            return __result
        else:
            #Return our value
            return __values.get("value")

    def get_element_attribute_value(self, element_tag, attribute_key):
        #Get the values
        __values = self.__document.findall(element_tag)
        #Check if our values is a list
        if("list" in str(type(__values))):
            #Create a value list
            __result = list()
            #Loop through the list
            for __value in __values:
                #Update our result
                __result.append(__value.get(attribute_key))
            #Return the list
            return __result
        else:
            #Return our value
            return __values.get(attribute_key)

    def get_document(self):
        #Return the document
        return self.__document

    def save(self):
        #Convert the document to bytes
        __bytes = Tree.tostring(self.__document)
        #Open the path for writing bytes
        __file = open(self.__path, "wb")
        #Write the bytes
        __file.write(__bytes)
        #Flush the file
        __file.flush()
        #Close the file
        __file.close()


class Settings(Storage):
    def add_int(self, key, value):
        #Add the element
        return super().add_element("Integer", str(value), attribute_keys=["key"], attribute_values=[key])
        
    def add_float(self, key, value):
        #Add the element
        return super().add_element("Float", str(value), attribute_keys=["key"], attribute_values=[key])
        
    def add_string(self, key, value):
        #Add the element
        return super().add_element("String", value, attribute_keys=["key"], attribute_values=[key])
        
    def add_setting(self, setting_type, key, value):
        #Add the element
        return super().add_element(setting_type, value, attribute_keys=["key"], attribute_values=[key])
    
    def get_int(self, key):
        for element in super().get_element("Integer"):
            if(element.get("key") == key):
                return int(element.get("value"))
                
    def get_float(self, key):
        for element in super().get_element("Float"):
            if(element.get("key") == key):
                return float(element.get("value"))
                
    def get_string(self, key):
        for element in super().get_element("String"):
            if(element.get("key") == key):
                return element.get("value")
                
    def get_setting(self, key):
        for element in super().get_element("Setting"):
            if(element.get("key") == key):
                return element.get("value")
