import sys
sys.dont_write_bytecode = True
import os
from radar import *
from payload import *
from storage.zipper import Zipper

_payload = Payload("storage", "Station", "Abcgold13!")
_payload.package()
_payload.unpack()