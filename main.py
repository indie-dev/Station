import sys
import os
from storage import *
from compression import *

__arguments = sys.argv
__initial_argument = __arguments[1]
print(__initial_argument)
if(__initial_argument.lower() is "--upload-to-network"):
    print("Uploading %s to Station network"%(__arguments[2]))
elif(__initial_argument.lower() is "--download-from-network"):
    print("Downloading unique id %s from Station network"%(__arguments[2]))
elif(__initial_argument.lower() =="--test"):
    __compression = Compressor("main.xml")
    __compression.decompress()
else:
    print("%s is not a valid parameter"%(__initial_argument))