import sys
import os
from storage import *

#Create a compressor class
class Compressor:
    def __init__(self, output_path):
        self.__chunk = Chunk()
        #Create the storage element
        self.__storage = Storage(output_path)

    def compress_file(self, file_path, parent_path):
        #Open the given file for byte reading
        __file = open(file_path, "rb")
        #Read the lines
        __lines = __file.readlines()
        #Create a content variable
        __content = ""
        #Loop through the bits in the lines
        for byte in __lines:
            for bit in byte:
                #Update the content
                __content += str(bit) + ","
        #Flush the file
        __file.flush()
        #Close the file
        __file.close()
        #Save the content
        return self.__storage.add_element("Compressed", __content, attribute_keys=["file_name", "parent_dir"], attribute_values=[os.path.basename(file_path), parent_path])
    
    def compress_folder(self, folder_path):
        #Loop through the files
        for root, folders, files in os.walk(folder_path):
            #Loop through the files and compress
            for file in files:
                #Compression time!
                self.compress_file(root + "/" + file, root)
            #Loop through the folders
            for folder in folders:
                #Compress the folders
                self.compress_folder(root + "/" + folder)
    def compress(self, path):
        if(os.path.isfile(path)):
            #Check if the os is windows
            if(os.name is "nt"):
                #Split the path
                __path_list = path.split("\\")
            else:
                #Split the path
                __path_list = path.split("/")
            #Get the parent dir
            __path = __path_list[len(__path_list) - 2]
            #Compress the file
            self.compress_file(path, __path)
        else:
            #Compress the folder
            self.compress_folder(path)
    def decompress(self):
        pass
#Create a chunk class
class Chunk:
    def __init__(self):
        pass

    def chunk_archive(self, archive_path):
        pass