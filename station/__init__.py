from computer_listener import *
from container import *

class Station:
    MODE_DOCK_AND_SHARE = 0
    MODE_UNDOCK_AND_NOTIFY = 1
    MODE = 0
    def __init__(self, mode):
        if((mode is Station.MODE_DOCK_AND_SHARE) or (mode == Station.MODE_DOCK_AND_SHARE)):
            #Pack the container, then give it to the network
            self.__pack_and_share_to_network = True
            self.__unpack_and_notify_network = False
            self.MODE = Station.MODE_DOCK_AND_SHARE
        elif((mode is Station.MODE_UNDOCK_AND_NOTIFY) or (mode == Station.MODE_UNDOCK_AND_NOTIFY)):
            #Unpack the container, and tell the network you have it
            self.__unpack_and_notify_network = True
            self.__pack_and_share_to_network = False
            self.MODE = Station.MODE_UNDOCK_AND_NOTIFY
        self.__listener = ComputerListener()
        self.__container = Container()
    #Check if the requested mode is 0
    if((MODE is MODE_DOCK_AND_SHARE)):
        #If so, allow usage of dock_and_share function
        def dock_and_share(self, path, container_name):
            self.__container.pack_into_container(path, container_name)
    else:
        #If not, allow usage of undock_and_notify function
        def undock_and_notify(self, path):
            self.__container.unpack_container(path)
    def listen_for_other_stations(self, neighbor_station):
        #Listen for all stations on the network
        self.__listener.get_all_computers_on_ip(neighbor_station, max_count=5)
    
    def get_listener(self):
        return self.__listener
    
    def get_container(self):
        return self.__container