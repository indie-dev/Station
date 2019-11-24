import sys
import os
from compression import *
from storage import *
import urllib.request
import urllib.error

class Network:
    def __init__(self, neighbor_station):
        #Set the neighbor station
        self.__neighbor_station = neighbor_station
    
    def listen_for_stations(self):
        self.__look_for_stations("web://localhost/Aversion")
    def __look_for_stations(self, url):
        __own_known_list = Storage(os.path.expanduser("~") + "/Station/known_stations.xml")
        __station_known_list = Storage("%s/known_stations.xml"%(url))
        __known_stations = __station_known_list.get_element("Station")
        for __station in __known_stations:
            __station_name = __station.get("name")
            __station_url = __station.get("value")
            __own_known_list.add_element("Station", __station_url, attribute_keys=["name"], attribute_values=[__station_name])
            try:
                self.__look_for_stations(url)
            except urllib.error.URLError as error:
                print("Ignoring %s"%(url))
    def upload_to_network(self):
        pass

    def upload_to_station(self, station_address):
        pass