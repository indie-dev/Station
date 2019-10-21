from computer_listener import *
from container import *
from station import *

comp_st = Station(Station.MODE_DOCK_AND_SHARE)
comp_st.listen_for_other_stations("192.168.0.40")