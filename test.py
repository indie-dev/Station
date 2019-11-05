import sys
import os
from radar import *
from payload import *
from storage.zipper import Zipper
from utils.files import *

__zipper = Zipper("Zipped.txt", encrypt=True, decrypt=True, password="Test")
__zipper.write_folder("storage", "Test")