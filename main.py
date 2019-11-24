import sys
import os
from storage import *
from compression import *
import random

__arguments = sys.argv
__initial_argument = __arguments[1]
__settings = Settings(os.path.expanduser("~") + "/Station/settings.xml")
if(__settings.get_string("user_setup") is None):
    print("Setting up...")
    __mode = input("Are you a Station, Ship, or both? (Station/Ship/Both): ")
    if(__mode.lower() == "station"):
        #Set the mode of the program
        __settings.add_string("mode", "Station")
        #Generate an alpha numeric value for fancy name
        __alpha_numeric = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        #Empty results
        __results = ""
        #Loop through a random range from 0:10
        for __value in range(0, 10):
            #Add the alpha numeric value
            __results += __alpha_numeric[random.randrange(0, 10)]
        #Add our fancy name to settings
        __settings.add_string("station_name", __results)
        #Get the type of content they support
        __content_supported = input("What type of content do you wish to support? (Web hosting, Terminal access, file sharing, or all): ")
        #Verify the value
        if(__content_supported.lower() == "web hosting"):
            #Set the type supported to 0
            __type_supported = 0
            #Add it to this device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that user has been setup
            __settings.add_string("user_setup", "true")
        elif(__content_supported.lower() == "terminal access"):
            #Set the type supported to 1
            __type_supported = 1
            #Add it to this device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that the user has been set up
            __settings.add_string("user_setup", "true")
        elif(__content_supported.lower() == "file sharing"):
            #Set the type supported to 2
            __type_supported = 2
            #Add it to the device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that the user was set up successfully
            __settings.add_string("user_setup", "true")
        elif(__content_supported.lower() == "all"):
            #Set the type supported to 3
            __type_supported = 3
            #Add it to this device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that the user has been set up
            __settings.add_string("user_setup", "true")
        else:
            #Notify that this is not a valid response
            print("%s is not a valid response"%(__content_supported))
    elif(__mode.lower() == "ship"):
        #Set the mode to ship
        __settings.add_string("mode", "ship")
        #Notify that the user was set up
        __settings.add_string("user_setup", "true")
    elif(__mode.lower() == "both"):
        __settings.add_string("mode", "both")
        #Generate an alpha numeric value for fancy name
        __alpha_numeric = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        #Empty results
        __results = ""
        #Loop through a random range from 0:10
        for __value in range(0, 10):
            #Add the alpha numeric value
            __results += __alpha_numeric[random.randrange(0, 10)]
        #Add our fancy name to settings
        __settings.add_string("station_name", __results)
        #Get the type of content they support
        __content_supported = input("What type of content do you wish to support? (Web hosting, Terminal access, file sharing, or all): ")
        #Verify the value
        if(__content_supported.lower() == "web hosting"):
            #Set the type supported to 0
            __type_supported = 0
            #Add it to this device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that user has been setup
            __settings.add_string("user_setup", "true")
        elif(__content_supported.lower() == "terminal access"):
            #Set the type supported to 1
            __type_supported = 1
            #Add it to this device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that the user has been set up
            __settings.add_string("user_setup", "true")
        elif(__content_supported.lower() == "file sharing"):
            #Set the type supported to 2
            __type_supported = 2
            #Add it to the device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that the user was set up successfully
            __settings.add_string("user_setup", "true")
        elif(__content_supported.lower() == "all"):
            #Set the type supported to 3
            __type_supported = 3
            #Add it to this device's settings
            __settings.add_int("type_supported", __type_supported)
            #Notify that the user has been set up
            __settings.add_string("user_setup", "true")
        else:
            #Notify that this is not a valid response
            print("%s is not a valid response"%(__content_supported))
    #Verify the validity of the payloads directory
    if(os.path.exists(os.path.expanduser("~") + "/Station/Payloads") is False or os.path.isdir(os.path.expanduser("~") + "/Station/Payloads") is False):
        #Make the payloads directory
        os.mkdir(os.path.expanduser("~") + "/Station/Payloads")
    print("Now, if you ran this with your own arguments, run this program again")
elif(__initial_argument.lower() == "--upload-to-network"):
    print("Uploading %s to Station network"%(__arguments[2]))
elif(__initial_argument.lower() == "--download-from-network"):
    print("Downloading unique id %s from Station network"%(__arguments[2]))
elif(__initial_argument.lower() == "--get-network-status"):
    print("Getting network status...")
elif(__initial_argument.lower() == "--get-station-status"):
    print("Getting station %s status..."%(__arguments[2]))
else:
    print("%s is not a valid parameter"%(__initial_argument))
    print("Valid parameters:")
    print("\n\t--upload-to-network [PAYLOAD_PATH]: Uploads the given path to the Station network")
    print("\n\t--download-from-network [PAYLOAD_UNIQUE_ID]: Downloads the given unique id from the Station network")
    print("\n\t--get-network-status: Gets the status of the network (if its available, stations and ships on network, etc)")
    print("\n\t--get-station-status: Gets the status of the given Station on the Station network (availability, payloads it has, etc)")