import sys
import os


class Chunk:
    def __init__(self):
        self.__content_saved_count = 0
        self.__files_created_count = 0
        self.__saved_content = list()
        
    def break_payload(self, payload_package_path, content_size_limit=100, out_dir="./"):
        #Get the content length of the file
        __content_length = os.path.getsize(payload_package_path)
        __file = open(payload_package_path, "r")
        __lines = __file.readlines()
        if(out_dir.endswith("/") is False):
            out_dir = out_dir + "/"
        if(os.path.exists(out_dir) is False or os.path.isfile(out_dir) is True):
            os.makedirs(out_dir)
        if(__content_length % 2 == 0):
            #Our content length is even
            __break_by = 2
        else:
            #Our content length is odd
            __break_by = 3
        if(__content_length >= content_size_limit):
            #If our content exceeds 100 megabytes
            #Loop through the content of the file
            for line in __lines:
                #Add the line to our saved content list
                self.__saved_content.append(line)
                #Check if the content saved count exceeds our break by count
                if(self.__content_saved_count % __break_by == 0):
                    #Notify that we are chunking the payload
                    print("Chunking the payload for ease-of-upload...")
                    #Loop through the saved content list
                    #Create a new file based on our files created count
                    if(self.__files_created_count is 0):
                        __chunk = open("%s%s.chunk"%(out_dir, payload_package_path), "w")
                    else:
                        __chunk = open("%s%s.chunk_%s"%(out_dir, payload_package_path, self.__files_created_count), "w")
                    for saved in self.__saved_content:
                        #Write the lines
                        __chunk.writelines(saved)
                    #Flush and close our file
                    __chunk.flush()
                    #Close the file
                    __chunk.close()
                    #Update our files created counter
                    self.__files_created_count += 1
                    #Clear our saved list
                    del self.__saved_content[:]
        else:
            #Notify that the payload is uploadable
            print("Payload is not eligible for chunking!")    
    def __sort(self, chunk_path):
        #Initialize a file counter
        __files_count = 0
        #For last known file count
        __last_known_num = 0
        #For finding the root file path
        __chunk_path = ""
        #For listing the files
        __files_list = list()
        #Walk through the chunk path
        for root, dirs, files in os.walk(chunk_path):
            #Loop through the files
            for file in files:
                #Check if .chunk is in the file
                if(".chunk" in file):
                    #Get the current path
                    __chunk_path = root + "/" + file
                    #Ignore .chunk or .chunk_num in the path
                    __chunk_path = __chunk_path.split(".chunk")[0]
                    #Append the files counter
                    __files_count += 1
        #Loop through a range between 0:__files_count
        for num in range(0, __files_count):
            #Check if the num is 0
            if(num is 0):
                #If so, the file path must end with .chunk
                __file = __chunk_path + ".chunk"
            else:
                #If not, add the number to our path
                __file = __chunk_path + ".chunk_%s"%(num)
            #Append the file list
            __files_list.append(__file)
        #Return the files list
        return __files_list
    def repair_chunked_payload(self, payload_chunks_path, chunk_output_path):
        #Open the output path
        __output = open(chunk_output_path, "w")
        #Sort the chunk list
        __file_list = self.__sort(payload_chunks_path)
        #Loop through the files
        for __file in __file_list:
            #Open the chunk for reading
            __chunk = open(__file, "r")
            #Get the lines
            __lines = __chunk.readlines()
            #Loop through the lines
            for __line in __lines:
                #Write the line to our output
                __output.writelines(__line)
            #Close the chunk
            __chunk.close()
        #Flush the output
        __output.flush()
        #Close the file
        __output.close()