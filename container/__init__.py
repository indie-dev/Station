import sys
import os
import zipfile
import http.server
import socketserver
import threading
import asyncio

class Container:
    ADD_COMPUTER_PORT = 3087
    HOST_PORT = 2087
    def __init__(self):
        self.DEFAULT_HOST_PORT = 2087
        self.HANDLER = http.server.SimpleHTTPRequestHandler
        self.CONTAINER_LIST = "container_list.html"
        self.COMPUTER_LIST = "computer_list.txt"
        self.MAIN_PAGE = "index.html"

    def pack_into_container(self, path, container_name):
        #Create the _zip variable
        _zip = zipfile.ZipFile(path + "/" + container_name + ".pack", "w", zipfile.ZIP_DEFLATED)
        #Loop through the root, dirs, and files in the given path
        for root, dirs, files in os.walk(path):
            #Get all of the files in files list
            for file in files:
                #To avoid any issues with anti-virus,
                #Check if the file itself is the container
                if((file is (container_name + ".pack")) or ((file == (container_name + ".pack")))):
                    #Do nothing
                    pass
                else:
                    #Write the file to our container
                    _zip.write(os.path.join(root, file))
    def unpack_container(self, path):
        #Open the zip using zipfile library
        _zip = zipfile.ZipFile(path, "r", zipfile.ZIP_DEFLATED)
        #Extract all of the files
        extract_path = path.replace(".pack", "/")
        #Check if the extract path exists
        if(os.path.exists(extract_path)):
            #If so, remove it
            os.rmdir(extract_path)
        else:
            #If not, make it
            os.mkdir(extract_path)
        #Unzip all of the files
        _zip.extractall(extract_path)
        #Update the container list
        self.add_to_container_list(extract_path)
    
    def add_to_container_list(self, path):
        containers = []
        #Check if the container list exists
        if(os.path.exists(self.CONTAINER_LIST)):
            #Open the file for reading
            file = open(self.CONTAINER_LIST, "r")
            #Read the content
            content = file.readlines()
            #Update the containers list
            containers = content
            #Flush the file
            file.flush()
            #Close the file
            file.close()
        #Add the given path to our container list
        containers.append(path)
        #Open container list for writing
        file = open(self.CONTAINER_LIST, "w")
        #Loop through the container list
        for container in containers:
            #Get the index of the container
            index = containers.index(container)
            #Get the length of the container list
            length = len(containers)
            #Check if the length - 1 is the index
            if(((length - 1) is index) or ((length - 1) == index)):
                #Write the container path without a comma
                file.writelines(os.path.abspath(path))
            else:
                #Write the container path with a comma
                file.writelines(os.path.abspath(path) + ",\n")
        #Flush the file
        file.flush()
        #Close the file
        file.close()
        #Check if the main page exists
        if(os.path.exists(self.MAIN_PAGE)):
            #If so, remove it
            os.remove(self.MAIN_PAGE)
        #Open the main page for writing
        file = open(self.MAIN_PAGE, "w")
        #Write the container list path to our index.html
        file.writelines('%s\n'%(self.CONTAINER_LIST))
        #Write the computer list to our index.html
        file.writelines('%s\n'%("computer_list.txt"))
        #Flush the list
        file.flush()
        #Close the list
        file.close()
        #Serve our httpserver
        self.make_alive()

    def make_alive(self, restart_post_close=True):
        #Create an http server
        with socketserver.TCPServer(("", self.DEFAULT_HOST_PORT), self.HANDLER) as server:
            #Notify that we our hosting the container list
            print("Hosting our container list...")
            #Handle single requests
            server.serve_forever()
            server.shutdown()
        #Close the server
        server.server_close()
        #Restart the serve function
        if(restart_post_close is True):
            #Restart the server
            self.make_alive(restart_post_close=restart_post_close)