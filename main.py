import sys
import os
from storage import *
from compression import *

#Get the arguments being passed
__arguments = sys.argv
#Get the initial argument
__initial_argument = __arguments[1]
#Check if the initial argument is upload to network
if(__initial_argument.lower() is "--upload-to-network"):
    #Notify of network upload
    print("Uploading %s to Station network"%(__arguments[2]))
#Check if the initial argument is download from network
elif(__initial_argument.lower() is "--download-from-network"):
    #Notify of payload download
    print("Downloading unique id %s from Station network"%(__arguments[2]))
#Check if the initial argument is test
elif(__initial_argument.lower() =="--test"):
    #Test our compression system
    __compression = Compressor("main.xml")
    __compression.add_file("station.cpp", "Station")
    __compression.decompress()
#If none of those apply, warn of a wrong parameter and tell which params are appropriate
else:
    print("%s is not a valid parameter"%(__initial_argument))
    print("Valid use: ")
    print("\n\t--upload-to-network [PAYLOAD_PATH]: Notifies all stations on the network of your request to upload a payload (file or folder), and uploads to any computer willing to take it. If your payload exceeds a certain size, it will be chunked. These chunks will be uploaded.")
    print("\n\t--download-from-network [PAYLOAD_UNIQUE_ID]: Downloads the payload or chunks with the given unique ID from the Station network. This ID is stored in your known payloads list.")
    print("\n\t--test: Tests a given method, primarily any new compression methods")