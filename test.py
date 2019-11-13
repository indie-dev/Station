import sys
import os
from radar import *
from payload import *
from storage.zipper import Zipper
from utils.files import *
from storage.chunk import *
__chunk = Chunk()
__list = ["Be_1", "Here_10", "Or_2", "Be_3", "Square_4"]
__chunk.break_payload("test.py", out_dir="Test")
__chunk.break_payload("test.py", out_dir="Test")
__chunk.repair_chunked_payload("Test", "test.txt")