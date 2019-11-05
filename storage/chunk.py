import sys
import os


class Chunk:
    def __init__(self):
        self.__content_saved_count = 0
        self.__files_created_count = 0
        self.__saved_content = list()
        
    def break_payload(self, payload_package_path, content_size_limit=100000, out_dir="./"):
        __file = open(payload_package_path, "rb")
        __lines = __file.readlines()
        __content_length = len(__lines)
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
                    #Loop through the saved content list
                    #Create a new file based on our files created count
                    if(self.__files_created_count is 0):
                        __chunk = open("%s%s.chunk"%(out_dir, payload_package_path), "wb")
                    else:
                        __chunk = open("%s%s.chunk_%s"%(out_dir, payload_package_path, self.__files_created_count), "wb")
                    for saved in self.__saved_content:
                        #Write the lines
                        __chunk.write(saved)
                    #Flush and close our file
                    __chunk.flush()
                    #Close the file
                    __chunk.close()
                    #Update our files created counter
                    self.__files_created_count += 1
                    #Clear our saved list
                    del self.__saved_content[:]
        else:
            print("Payload is not eligible for chunking!")