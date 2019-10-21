from computer_listener import *
from container import *
from station import *

comp_station = Station(Station.MODE_DOCK_AND_SHARE)
comp_station.get_container().make_alive()