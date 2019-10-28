from radar import *
from payload import *
from station import *
from storage import *
import sys

def package_payload(payload_name, payload_path, requests_support_type):
    load = Payload(requests_support_type)
    load.wrap_payload(payload_path, payload_name)

def setup_application(setup_as, supports_type):
    _station = Station(setup_as=setup_as, supports_type=supports_type)
    _station.save_application()
try:
    _argv = sys.argv
    print("Setting up station...")
    #Get the requested station type
    _requested_station_type = _argv[1]
    #Get the requested request support types
    _requested_supports_type = _argv[2]
    #Check if the station supports all
    if(str((_requested_supports_type)).upper() is Station.SUPPORTS_TYPE_ALL):
        _supports_type = Station.SUPPORTS_TYPE_ALL
    #Check if the station supports only file sharing
    elif(str(_requested_supports_type).upper() is Station.SUPPORTS_TYPE_FILE_SHARE):
        _supports_type = Station.SUPPORTS_TYPE_FILE_SHARE
    #Check if the station only supports terminal access
    elif(str(_requested_supports_type).upper is Station.SUPPORTS_TYPE_TERMINAL):
        _supports_type = Station.SUPPORTS_TYPE_TERMINAL
    #Check if the station only supports webhosting
    elif(str(_requested_supports_type).upper() is Station.SUPPORTS_TYPE_WEBHOST):
        _supports_type = Station.SUPPORTS_TYPE_WEBHOST
    else:
        _supports_type = Station.SUPPORTS_TYPE_ALL
    
    #Check if the station is both
    if(str(_requested_station_type).upper() is Station.SETUP_AS_BOTH):
        _setup_type = Station.SETUP_AS_BOTH
    #Check if the station is a ship
    elif(str(_requested_station_type).upper() is Station.SETUP_AS_SHIP):
        _setup_type = Station.SETUP_AS_SHIP
    #Check if the station is a station
    elif(str(_requested_station_type).upper() is Station.SETUP_AS_STATION):
        _setup_type = Station.SETUP_AS_STATION
    else:
        _setup_type = Station.SETUP_AS_BOTH
    #Save the selected values
    setup_application(_setup_type, _supports_type)
except IndexError as identifier:
    print("You currently can run:\n")
    print("\tpython setup.py [STATION_TYPE] [REQUEST_TYPES_SUPPORTED]\n")
    print("\t[STATION_TYPE] tells the application if you wish to host containers, or to only download them. This can be:")
    print("\t\tSTATION: For hosting containers")
    print("\t\tSHIP: For downloading containers")
    print("\t\tBOTH: Your device is a ship and a station")
    print("\t[REQUEST_TYPES_SUPPORTED] tells the application which types of requests your device supports.")
    print("\t\tWEBHOST: Allows others to host websites on your device")
    print("\t\tTERMINAL: Allows a sandboxed, extremely limited terminal access to others")
    print("\t\tFILE_SHARE: Allows others to save their files on your computer")
    print("\t\tALL: Supports all of the above")