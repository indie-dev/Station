import sys
import os
from storage import *

class Radar:
    DEFAULT_STATION_LOAD_PATH = "/Station/"
    DEFAULT_STATION_PATH = "/Station/stations_list.xml"
    FINAL_STATION = "FINAL_STATION"
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
        #Initiate the index count
        self.__index_count = 0
    
    def find_stations(self, neighbor_station, max_index_count = 5):
        #Create a station variable based on a stringified neighbor_station
        __station = str(neighbor_station)
        #Check if the neighbor station does not start with http
        if(__station.startswith("http") is False):
            #If that is true, add the http URI
            __station = "http://" + __station
        if(__station.endswith("stations_list.xml") is False):
            #If the station does not end with stations_list.xml, add it
            __station = __station + "/stations_list.xml"
        #Add the given station to our list
        self.__stations_list.append(str(neighbor_station))
        
        #Open the neighbor station
        __station_storage = Storage(__station)
        #Get all of the known stations
        __known_stations = __station_storage.get_all_elements("Device")
        #Loop through all of the stations
        for __known_station in __known_stations:
            #Get the location
            __location = __known_station.get("location")
            print("Found station: %s"%(str(__location)))
            #Check if the index count exceeds the maximum index
            if(self.__index_count > max_index_count or Radar.FINAL_STATION in __location):
                #Save the list
                self.save_stations_list()
                #Exit the loop
                return None
            self.__index_count += 1
            #Go through the stations in the given location
            self.find_stations(str(__location))

    
    def save_stations_list(self):
        #Check if the file exists
        if(os.path.exists(os.path.expanduser("~") + Radar.DEFAULT_STATION_PATH)):
            #Open the xml code
            __file = open(os.path.expanduser("~") + Radar.DEFAULT_STATION_PATH, "r")
            #Read the lines into _xml
            __xml = __file.readlines()
            #Flush the file
            __file.flush()
            #Close the file
            __file.close()
        else:
            #Set _xml to empty
            __xml = ""
        #Check if the parent directory exists
        if(os.path.exists(os.path.expanduser("~") + "/Station") is False):
            #Create the directory
            os.makedirs(os.path.expanduser("~") + "/Station")
        #Create a storage variable
        __storage = Storage(os.path.expanduser("~") + Radar.DEFAULT_STATION_PATH)
        #Loop through our stations list
        for __station in self.__stations_list:
            #Check if the station is not in _xml
            if(__station not in __xml):
                #Save the given station
                __storage.add_element("Device", None, attribute_keys=["location"], attribute_values=[str(__station)])