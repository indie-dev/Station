import sys
import os
from storage import *
from compression import *

__arguments = sys.argv
__initial_argument = __arguments[1]
if(__initial_argument.lower() is "--upload-to-network"):
    print("Uploading %s to Station network"%(__arguments[2]))
elif(__initial_argument.lower() is "--download-from-network"):
    print("Downloading unique id %s from Station network"%(__arguments[2]))
else:
    print("%s is not a valid parameter"%(__initial_argument))