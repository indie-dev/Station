import sys
import os
from storage import *

class Radar:
    DEFAULT_STATION_PATH = "/Station/stations_list.xml"
    def __init__(self, known_stations_list=None):
        #Check if the known stations list is not null
        if(known_stations_list is not None):
            #Initiate our stations list with the known list
            self.__stations_list = known_stations_list
            #Check if the stations list file exists
            if(os.path.exists(os.path.expanduser("~") + Radar.DEFAULT_STATION_PATH)):
                #Open the file in our storage class
                __storage = Storage(os.path.expanduser("~") + Radar.DEFAULT_STATION_PATH)
                #Loop through all device tags
                for __device in __storage.get_all_elements("Device"):
                    #Get the device's location
                    self.__stations_list.append(__device.get("location"))
        else:
            #Initiate our stations list with no data
            self.__stations_list = list()
    
    def find_stations(self, neighbor_station):
        pass
    
    def save_stations_list(self):
        #Check if the parent directory exists
        if(os.path.exists(os.path.expanduser("~") + "/Station") is False):
            #Create the directory
            os.makedirs(os.path.expanduser("~") + "/Station")
        #Create a storage variable
        __storage = Storage(os.path.expanduser("~") + Radar.DEFAULT_STATION_PATH)
        #Loop through our stations list
        for __station in self.__stations_list:
            #Save the given station
            __storage.add_element("Device", None, attribute_keys=["location"], attribute_values=[str(__station)])