import sys, os
import xml.etree.ElementTree as Tree
from storage import *
class Station:
    SETUP_AS_STATION = "STATION"
    SETUP_AS_SHIP = "SHIP"
    SETUP_AS_BOTH = "BOTH"
    SUPPORTS_TYPE_WEBHOST = "WEBHOST"
    SUPPORTS_TYPE_FILE_SHARE = "FILE_SHARE"
    SUPPORTS_TYPE_TERMINAL = "TERMINAL"
    SUPPORTS_TYPE_ALL = "ALL"
    SELECTED_SETUP_TYPE = "BOTH"
    SELECTED_SUPPORT_TYPE = "ALL"
    def __init__(self, setup_as="BOTH", payload_list_path = "payload_list.xml", known_stations_list_path = "known_stations.xml", supports_type="ALL"):
        Station.SELECTED_SETUP_TYPE = setup_as
        Station.SELECTED_SUPPORT_TYPE = supports_type
        self.__setup_as = setup_as
        self.__supports_type = supports_type
        self.save_application()
    
    def save_application(self, payload_list_path ="payload_list.xml", known_stations_list_path = "known_stations.xml", save_path="info.xml"):
        #Ship for collecting, station for hosting
        __storage = Storage("info.xml", root_tag="Stations")
        #Get the stored station type
        stored_station_type = __storage.get_attribute_value("Info", "station_type")
        #Get the stored request types that the station supports
        stored_requests_supported = __storage.get_attribute_value("Info", "station_request_types_supported")
        #Check if the stored station type is nothing, and so is the stored requests type
        if(stored_station_type is not True and stored_requests_supported is not True):
            #Save the data
            __storage.write_node("Info", attribute_keys=["station_type"], attribute_values=[self.__setup_as])
            __storage.write_node("Info", attribute_keys=["station_request_types_supported"], attribute_values=[self.__supports_type])
            __storage.write_node("Info", attribute_keys=["payload_list_path"], attribute_values=[payload_list_path])
            __storage.write_node("Info", attribute_keys=["known_stations_list_path"], attribute_values=[known_stations_list_path])
        