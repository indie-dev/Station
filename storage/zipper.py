import sys
import os
from storage import *
from pathlib import Path
from utils.files import *
class Zipper:
    def __init__(self, path, encrypt=False, decrypt=False, password=None):
        self.__path = path
        self.__storage = Storage(self.__path)
        self.__encrypt = encrypt
        self.__decrypt = decrypt
        self.__password = password
        if(self.__encrypt is True):
            self.__storage.add_element("Encrypted", self.encrypt(b"true"))
            pass
        self.__pack_count = 0
    def write_folder(self, folder_to_write):
        if(len(os.listdir(folder_to_write)) <= 0):
            print("Cannot pack empty folders")
        else:
            for foldername, dirs, files in os.walk(folder_to_write):
                for file in files:
                    try:
                        self.write(foldername + "/" + file)
                    except UnicodeDecodeError as identifier:
                        pass
    def write(self, file_to_write):
        try:
            print("ADDING: %s"%(file_to_write))
            #Open the requested file for writing
            with open(file_to_write, "r") as read:
                #Create an empty content variable
                content = ""
                #Loop through all of the lines in the file
                for line in read.readlines():
                    #Append the content variable
                    __content = line
                    content += line
                if(self.__encrypt):
                    content = self.encrypt(content)
                #Get the parent path
                #__parent_path = str(os.path.abspath(os.path.join(file_to_write, os.pardir)))
                __parent_path = "."
                #Check if our parent path is not in the file_to_write variable
                if(__parent_path not in file_to_write):
                    #If so, set the parent path to .
                    __parent_path = "."
                #Add our file to the archive
                self.__storage.add_element("File", content, attribute_keys=["path", "multiple_elements_exist"], attribute_values=[file_to_write, __parent_path, "true"])
                self.__pack_count += 1
        except UnicodeDecodeError as identifier:
            pass

    def unpack(self, unpack_path):
        #First, check for encryption
        if(self.__decrypt is True):
            #Check if the password is correct by decrypting the encrypted key
            if(self.decrypt(self.__storage.get_value("Encrypted")).lower() != "true"):
                #If the password is invalid, raise an error
                raise Exception("You have the wrong password!")
        #Loop through all of the elements
        for element in self.__storage.get_all_elements("File"):
            #Get the pat of the element
            __element_path = element.get("path")
            #Get the value of the element
            __element_value = element.get("value")
            #Initiate an element parent variable
            __element_parent = ""
            #Split the element path variable with /
            __paths = __element_path.split("/")
            #Loop through all of the lines in the array
            for line in __paths:
                #Get the index of the current line
                line_index = __paths.index(line)
                #Check if the index is not the final part of our path
                if(line_index is not len(__paths) -1 ):
                    #Append the element parent variable
                    __element_parent += line + "/"
            #Check if there is a decryption request
            if(self.__decrypt is True):
                #Decrypt the  element value
                __element_value = self.decrypt(__element_value)
            #Check if the element parent is .
            if(__element_parent is "."):
                #Set the element parent to . ...
                __element_parent = "."
            #Check if the parent directory exists
            if(os.path.exists(unpack_path + "/" +__element_parent) is False):
                #Create all of the directories and sub directories
                os.makedirs(unpack_path + "/" + __element_parent)
            #Open the file for writing
            with open(unpack_path + "/" + __element_parent + "/" + __paths[len(__paths) - 1], "w") as writer:
                #Write our element value
                writer.writelines(__element_value)
    def encrypt(self, content):
        #Encrypt the content
        encrypted = []
        for i, c in enumerate(content):
            pass_c = ord(self.__password[i % len(self.__password)])
            if(type(content) is bytes):
                msg_c = c
            else:
                msg_c = ord(c)
            #msg_c = ord(c)
            encrypted.append(chr((msg_c + pass_c) % 127))
        return ''.join(encrypted)
    
    def decrypt(self, content):
        #Decrypt the content
        msg = []
        for i, c in enumerate(content):
            pass_c = ord(self.__password[i % len(self.__password)])
            if(type(content) is bytes):
                enc_c = c
            else:
                enc_c = ord(c)
            msg.append(chr((enc_c - pass_c) % 127))
        return ''.join(msg)
    
    def encrypt_file_content(self, path):
        #Encrypt the file's content
        encrypted = ""
        for line in open(path, "r").readlines():
            encrypted += self.encrypt(line)
        return encrypted

    def decrypt_file_content(self, path):
        #Decrypt the file's content
        decrypted = ""
        for line in open(path, "r").readlines():
            decrypted += self.decrypt(line)
        return decrypted
    def get_storage(self):
        #Return the storage
        return self.__storage