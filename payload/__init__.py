import sys
import os
from zipfile import * 
from storage import *
from radar import *
from storage.zipper import Zipper

class Payload:
    def __init__(self, payload_path, payload_name, password):
        self.__payload_path = payload_path
        self.__payload_name = payload_name
        if(os.path.exists(os.path.expanduser("~") + "/Station") is False):
            os.mkdir(os.path.expanduser("~") + "/Station")
        if(os.path.exists(os.path.expanduser("~") + "/Station/Payloads/") is False):
            os.mkdir(os.path.expanduser("~") + "/Station/Payloads/")
        if(os.path.exists(os.path.expanduser("~") + "/Station/Payloads/" + self.__payload_name)):
            os.mkdir(os.path.expanduser("~") + "/Station/Payloads/" + self.__payload_name)
        self.__zipper = Zipper(os.path.expanduser("~") + "/Station/Payloads/" + self.__payload_name + ".pack", encrypt=True, decrypt=True, password=password)
    def package(self):
        self.__zipper.write_folder(self.__payload_path)
    def unpack(self):
        self.__zipper.unpack(os.path.expanduser("~") + "/Station/Payloads/" + self.__payload_name)
class UploadPayload:
    def __init__(self, package_path):
        self.__package_path = package_path
    #Find all neighbor stations
    def find_available_stations(self, neighbor_station):
        print("Finding stations attached to the station at %s"%(neighbor_station))
    #Check if the neighbor station is capable of handling this station
    def check_neighbor_station_capabilities(self, neighbor_station):
        print("Checking the capabilities of the neighbor station at %s"%(neighbor_station))
    #Ask the network to host this on the first available machine
    def ask_network_to_host(self):
        print("Asking the network to host %s"%(self.__package_path))
    #Ask a selected neighbor to host
    def ask_neighbor_to_host(self, neighbor_station):
        print("Asking the neighbor station at %s to host the payload"%(neighbor_station))