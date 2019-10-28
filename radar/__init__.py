import sys
import os
import ssl
import urllib
import socketserver
import zipfile
import random
import xml.etree.ElementTree as Tree
from storage import *
import bs4

class Radar:
    def __init__(self, station_list_path="known_stations.xml"):
        self.__station_list_path = station_list_path
        self.__station_list = Storage(self.__station_list_path, root_tag="Stations")

    def listen_for_stations(self, neighbor_station):
        if(neighbor_station is "END_OF_BRANCH" or ((neighbor_station) == "END_OF_BRANCH")):
            print("FOUND END")
            return None
        __station_list_path = self.__station_list.get_attribute_from_site(neighbor_station + "/info.xml", "Info", "known_stations_list_path")[0]
        __station_list = self.__station_list.get_attribute_from_site(neighbor_station + "/" + __station_list_path, "Station", "station_address")
        for station in __station_list:
            if("END_OF_BRANCH" not in (str(station))):
                self.add_station_to_list(str(station))
            self.listen_for_stations(station)

    
    def add_station_to_list(self, station_address):
        self.__station_list.write_node("Station", attribute_keys=["station_address"], attribute_values=[station_address])

    def get_station_list(self):
        return self.__station_list