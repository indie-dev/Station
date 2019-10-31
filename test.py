import sys
import os
from radar import *

__radar = Radar(known_stations_list=["192.168.0.32"])
__radar.save_stations_list()