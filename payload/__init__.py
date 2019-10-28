import sys
import os
import ssl
import urllib
import socketserver
import zipfile
import random
import xml.etree.ElementTree as Tree
from storage import *

class Payload:

    PAYLOAD_REQUEST_WEBHOST = 0
    PAYLOAD_REQUEST_FILE_SHARE = 1
    PAYLOAD_REQUEST_TERMINAL = 2
    SELECTED_SUPPORT_TYPE = 0

    def __init__(self, payload_requests_support_type):
        Payload.SELECTED_SUPPORT_TYPE = payload_requests_support_type
        self.__old_dir = None
    
    def create_unique_id(self, length = 0):
        #Get a list of alpha numeric values
        alpha_numeric_values = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        #Create a result value
        result = ""
        #Check if the requested length is less than or is 0
        if(length <= 0):
            #If either, set the length to the length of the 
            #Alpha numeric values
            length = len(alpha_numeric_values)
        #Loop through a range from 0 to length
        for i in range(0, length):
            #Append the result to the value residing on random.randint(0, len(alpha_numeric_values))
            #In the alpha_numeric_values variable
            result += alpha_numeric_values[random.randint(0, len(alpha_numeric_values))]
        #Return the result
        return result

    def write_to_payload_info(self, payload_path, tag, value, attribute_keys=None, attribute_values=None):
        #Create a variable for the info file
        info_path = payload_path + "/payload_info.xml"
        #Check if the info path exists
        if(os.path.exists(info_path)):
            #Create a parent variable based on the
            #Root tag
            parent = Tree.parse(info_path).getroot()
        else:
            #Create a root tag
            parent = Tree.Element("Payload")
        #Create the child element
        child = Tree.SubElement(parent, tag)
        #Set the value
        child.set("value", value)
        #Check if there is an attribute
        if(attribute_keys is not None and attribute_values is not None):
            #Loop through the keys
            for key in attribute_keys:
                #Get the index of the key
                index = attribute_keys.index(key)
                #Get the value
                _value = attribute_values[index]
                #Set the child's attributes
                child.set(key, _value)
        #Convert the content in the parent tag to string
        content = Tree.tostring(parent, encoding='utf8', method='xml')
        #Open the info path in write mode
        info = open(info_path, "wb")
        #Write all the lines
        info.write(content)
        #Flush the file
        info.flush()
        #Close the file
        info.close()

        #Return the parent tag
        return parent
    def get_value_from_info(self, payload_path, tag, return_all=False):
        info_path = payload_path + "/payload_info.xml"
        #Check if the file exists
        if(os.path.exists(info_path) is False):
            #Raise an error
            raise Exception("%s does not exist!" % (info_path))
        #Get the root tag
        parent = Tree.parse(info_path).getroot()
        #Get all of the children
        return parent.find(tag).get("value")
    
    def get_attribute_value_from_info(self, payload_path, tag, attribute_key):
        info_path = payload_path + "/payload_info.xml"
        #Check if the file exists
        if(os.path.exists(info_path) is False):
            #Raise an error
            raise Exception("%s does not exist!" % (info_path))
        #Get the root tag
        parent = Tree.parse(info_path).getroot()
        #Return the child element's attribute value
        return parent.find(tag).get(attribute_key)

    def wrap_payload(self, payload_path, payload_name):
        payload_out_dir = os.path.expanduser("~") + "/Payloads/%s"%(payload_name)
        #Check if the payload out dir does not exist
        if(os.path.exists(payload_out_dir)is False):
            #Create the out directory
            os.makedirs(payload_out_dir)
        #Set the payload output directory again, with the package
        payload_out_dir = os.path.expanduser("~") + "/Payloads/%s/%s.pack"%(payload_name, payload_name)
        #Check if the payload exists
        if(os.path.exists(payload_path) and os.path.isdir(payload_path)):
            #Write the payload name to our payload
            self.write_to_payload_info(payload_path, "PayloadName", payload_name)
            #Create the zip variable
            _zip = zipfile.ZipFile(payload_out_dir, "w", zipfile.ZIP_DEFLATED)
            #Loop through the path
            self.__zip_dir(_zip, payload_path)
            __storage = Storage("info.xml", root_tag="Stations")
            __payload_list = Storage(__storage.get_attribute_value("Info", "payload_list_path")[0], root_tag="PayloadList")
            __payload_list.write_node("Payload", attribute_keys=["payload_path", "payload_name"], attribute_values=[payload_path, payload_name])
    def __zip_dir(self, _zip, path):
        if(self.__old_dir is None):
            self.__old_dir = os.getcwd()
            os.chdir(path)
            path = "."
        #Get all items in this path
        for item in os.listdir(path):
            #Create a _path variable with the item added
            _path = path + "/" + item
            #Check if the path is a directory
            if(os.path.isdir(_path)):
                #Loop and add all files in the _path dir to our zip
                self.__zip_dir(_zip, _path)
            else:
                #Write the _path file to the zip
                _zip.write(_path)
                #print(_path)