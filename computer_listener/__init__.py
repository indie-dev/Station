import sys
import os
import ssl
import urllib.request as url
import http.server
import socketserver
import threading

class ComputerListener:

    def __init__(self, initial_computer_list=None):
        #Check if initial_computer_list is none
        if(initial_computer_list is None):
            #If so, create the computer list
            self.__computer_list = []
        else:
            #If not, set computer list to initial_computer_list
            self.__computer_list = initial_computer_list
        #Instantiate the current counter
        self.__current_count = 0
        #Create the context
        self.__context = ssl.create_default_context()
        #No host name check
        self.__context.check_hostname = False
        #Set verify mode to none
        self.__context.verify_mode = ssl.CERT_NONE
        #Create an end of branch variable
        self.NETWORK_BRANCH_END = "END_OF_BRANCH"
        self.DEFAULT_HOST_PORT = 2087
        self.HANDLER = http.server.SimpleHTTPRequestHandler
        self.CONTAINER_LIST = "container_list.html"
        self.COMPUTER_LIST = "computer_list.txt"
        self.MAIN_PAGE = "index.html"

    def get_all_computers_on_ip(self, ip, using_port=2087, max_count=2, add_to_computer_list=True, auto_save=True):
        #Check if port being used is 80
        if(using_port is 2087):
            #Create the full url with no port
            full_url = "https://" + str(ip) + ":2087/" + self.COMPUTER_LIST
        else:
            #Create the full url with the given port
            full_url = "https://" + str(ip) + ":" + str(using_port) + "/" + self.COMPUTER_LIST
        #Check if the current counter exceeds our max count
        if(self.__current_count > max_count):
            #End the function
            return None
        #Open the url
        website = url.urlopen(full_url, context=self.__context)
        #Read the content
        content = str(website.read().decode("utf-8"))
        #Check if the content is the end of network
        if((content is self.NETWORK_BRANCH_END) or (content == self.NETWORK_BRANCH_END)):
            #Return nothing, end function
            return None
        #Check if content starts with uri
        if(content.startswith("https://")):
            #Replace the uri
            content = content.replace("https://", "")
        elif(content.startswith("http://")):
            #Replace the uri
            content = content.replace("http://", "")
        #Check if we should add the computer to our list
        if((add_to_computer_list is True) or (add_to_computer_list == True)):
            #Add the computer to our list
            self.add_computer_to_list(content)
        #Check if we should save the computer to our list
        if((auto_save is True) or (auto_save == True)):
            #Save the list to our file
            self.save_computer_list()
        #Update the counter
        self.__current_count += 1
        #Get all the computers on this computer
        self.get_all_computers_on_ip(content, using_port=using_port)

    def add_computer_to_list(self, ip):
        #Add the computer to our list
        self.__computer_list.append(ip)

    def get_computer_list(self):
        #Return the computer list
        return self.__computer_list

    def save_computer_list(self):
        #Check if the computer list exists
        if(os.path.exists(self.COMPUTER_LIST)):
            #Remove the list
            os.remove(self.COMPUTER_LIST)
        #Open the computer list file
        file = open(self.COMPUTER_LIST, "w")
        #Loop through the list of saved computers
        for computer in self.__computer_list:
            #Get the index of our computer here
            index = self.__computer_list.index(computer)
            #Get the length of the computer list
            length = len(self.__computer_list)
            #Check if length - 1 is the index
            if(((length - 1) is index) or ((length - 1) == index)):
                #If it is, write the computer with no comma
                file.writelines(computer)
            else:
                #If it is not, write the computer with a comma
                file.writelines(computer + ",\n")
        #Flush the file
        file.flush()
        #Close the file
        file.close()

    def get_saved_computers(self, nullify_computer_list=True):
        #Check if we should nullify the computer list
        if((nullify_computer_list is True) or (nullify_computer_list == True)):
            #Nullify the list
            self.__computer_list = []
        #Open the file for reading
        file = open(self.COMPUTER_LIST, "r")
        #Read the content
        content = file.readlines()
        #Loop through the content list
        for line in content:
            #Check if the current line ends with a comma
            if(line.endswith(",\n")):
                #Replace the comma with nothing
                line = line.replace(",\n", "")
            #Add the line to the computer list
            self.add_computer_to_list(line)
        #Return the content
        return content