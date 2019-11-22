import sys
import os
from storage import *
import random

#Create a compressor class
class Compressor:
    def __init__(self, path):
        #Create the class-wide path variable
        self.__path = path
        #Create our chunking class
        self.__chunk = Chunk()
        #Verify that the given path is not a directory
        if(os.path.isdir(self.__path) is False):
            #If that is true, create a storage variable
            self.__storage = Storage(path)
    
    def chunk(self, path, output_dir):
        self.__chunk.chunk_archive(path, output_dir)

    def restore_chunks(self, chunk_dir, restored_archive_path):
        self.__chunk.restore_chunk(chunk_dir, restored_archive_path)

    def add_file(self, file_path, parent_path, delete_post_compression=True):
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
        #Check if the parent dir is empty
        if(parent_path is ""):
            #Set the parent path to .
            parent_path = "."
        #Save the content
        __element = self.__storage.add_element("Compressed", __content, attribute_keys=["file_name", "parent_dir"], attribute_values=[os.path.basename(file_path), parent_path])
        #Check if we should delete after compressing to save storage
        if(delete_post_compression):
            #Delete the file
            os.remove(file_path)
    def add_folder(self, folder_path, delete_post_compression=True):
        #Loop through the files
        for root, folders, files in os.walk(folder_path):
            #Loop through the files and compress
            for file in files:
                #Compression time!
                self.add_file(root + "/" + file, root, delete_post_compression=delete_post_compression)
            #Loop through the folders
            for folder in folders:
                #Compress the folders
                self.add_folder(root + "/" + folder, delete_post_compression=delete_post_compression)
                #Check if we should delete after compressing
                if(delete_post_compression):
                    #Remove the folder
                    os.rmdir(folder_path)
    def add(self, path, delete_post_compression=True):
        if(os.path.isfile(path)):
            #Check if the os is windows
            if(os.name is "nt"):
                #Split the path
                __path_list = path.split("\\")
            else:
                #Split the path
                __path_list = path.split("/")
            #Get the parent dir
            __path = os.path.basename(os.path.dirname(path))
            #Compress the file
            self.add_file(path, __path, delete_post_compression=delete_post_compression)
        else:
            #Compress the folder
            self.add_folder(path, delete_post_compression=delete_post_compression)
    
    def decompress(self):
        #First, check if the path is a folder
        if(os.path.isdir(self.__path)):
            #If so, attempt to restore the chunks inside
            self.restore_chunks(self.__path, "restored.pack")
            #Now set our pack path is restored.pack
            __pack_path = "restored.pack"
        else:
            #If not, then our pack path is self.__path
            __pack_path = self.__path
        #Create the storage variable
        __storage = Storage(__pack_path)
        #Loop through all elements with Compressed tag
        for element in __storage.get_element("Compressed"):
            #Get the parent directory
            parent_dir = element.get("parent_dir")
            #Get the file name
            file_name = element.get("file_name")
            #Get the content of the compressed file
            content = element.get("value")
            #Create an output bytearray
            __output = bytearray()
            #Split the lines inside and loop via ','
            for num in content.split(","):
                #Verify our number being legitimate
                if(num is not ""):
                    #Update the output with the number
                    __output.append(int(num))
            #Check if the parent directory exists
            if(os.path.exists(parent_dir) is False):
                #Make the parent directory
                os.mkdir(parent_dir)
            #Open our file for writing
            file = open(parent_dir + "/" + file_name, "wb")
            #Write the bytes to the file
            file.write(__output)
            #Flush the file
            file.flush()
            #Close the file
            file.close()

    def get_chunk(self):
        return self.__chunk
#Create a chunk class
class Chunk:
    def __init__(self):
        pass

    def chunk_archive(self, archive_path, output_dir, min_payload_size=1):
        #Created a saved content counter
        __saved_content_counter = 0
        #Get the size of our payload
        __payload_size = os.path.getsize(archive_path)
        #Open the payload for byte-based reading
        __payload = open(archive_path, "rb")
        #Get all of the lines in the payload
        __lines = __payload.readlines()
        #Get the length of the lines
        __line_length = len(__lines)
        #Verify that our output exists
        if(os.path.exists(output_dir) is False):
            #Make the output dir
            os.mkdir(output_dir)
        #Check if the content length is even
        if((__line_length % 2) == 0):
            #We are breaking by 2
            __break_by = 2
        else:
            #We are breaking by 3
            __break_by = 3
        #Create a saved content array
        __saved_content = list()
        #Check if the payload is chunkable
        if(__line_length >= min_payload_size):
            #Loop through the bytes
            for __byte in __lines:
                #Loop through the bits
                for __bit in __byte:
                    #Add the bit to our saved content
                    __saved_content.append(__bit)
                    #Check if the saved content modulo break by is 0
                    if(random.randint(0, 2) != 0):
                        #Notify of chunking
                        print("Chunking payload for easy uploading...")
                        #Get the file name
                        __chunk_name = os.path.basename(archive_path)
                        #Open our chunk for writing
                        chunk = open(output_dir + "/" + __chunk_name + ".chunk_" + str(__saved_content_counter), "w")
                        #Loop through saved content
                        for __saved in __saved_content:
                            #Write the chunk
                            chunk.write(str(__saved) + ",")
                        #Flush
                        chunk.flush()
                        #Close
                        chunk.close()
                        #Update saved content counter
                        __saved_content_counter += 1
                        #Reset our saved content
                        __saved_content.clear()
    def __sort_chunks(self, chunk_dir):
        #Create a chunk counter
        __chunk_counter = 0
        #Create a last known chunk count
        __last_known_chunk_counter = 0
        #Create a variable for finding the root path
        __root_path = ""
        #And create a file list for listing files later
        __files_list = list()
        __chunk_array = list()
        #Go through the files and folders in the chunk dir
        for root, folders, files in os.walk(chunk_dir):
            #Loop through the files
            for file in files:
                #Verify that the file is a chunk
                if(".chunk_" in file):
                    #Get the file path
                    __root_path = root + "/" + file
                    #Get the file path without .chunk
                    __root_path = __root_path.split(".chunk_")[0]
                    #Update the file counter
                    __chunk_counter += 1
                    __chunk_array.append(__chunk_counter)
        #Loop through a range between 0:__chunk_counter
        for num in range(0, __chunk_counter):
            #Get the chunk
            __chunk = __root_path + ".chunk_%s"%(str(num))
            #Append the file list
            __files_list.append(__chunk)
        #Return the new file list
        return __files_list

    def restore_chunk(self, chunk_dir, restored_archive_path):
        #Sort the chunks
        sorted_file_list = self.__sort_chunks(chunk_dir)
        #Open the archive
        archive = open(restored_archive_path, "wb")
        #Create an output
        output = bytearray()
        #Loop through the chunks in our sorted list
        for chunk_path in sorted_file_list:
            #Open the selected chunk for reading
            chunk = open(chunk_path, "r")
            #Loop through its lines
            for line in chunk.readlines():
                #Split the lines  by ,
                for num in line.split(","):
                    #Ignore whitespaces
                    if(num is not ""):
                        #Append the output with the given number
                        output.append(int(num))
            #Flush the chunk
            chunk.flush()
            #Close the chunk
            chunk.close()
        #Write the output
        archive.write(output)
        #Flush the archive
        archive.flush()
        #Close the archive
        archive.close()