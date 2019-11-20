from storage import *
from compression import *

__storage = Storage("init.xml")
__content_list = __storage.get_element_value("Compressed")[0].split(",")
__output = bytearray()
for content in __content_list:
    if(content is not ""):
        __output.append(int(content))
print(__output.decode())