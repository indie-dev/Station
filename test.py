import sys
import os
from radar import *
from payload import *
from storage.zipper import Zipper

__zipper = Zipper(os.getcwd() + "/Phillipines.pz", encrypt=True, decrypt=True, password="RAM")
__zipper.write("test.py")
__zipper.unpack("test")