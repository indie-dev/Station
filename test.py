from storage import *
from compression import *

__compression = Compressor("main.xml")
__compression.compress(os.getcwd() + "/test.py")
__compression.decompress()