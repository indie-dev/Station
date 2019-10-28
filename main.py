from payload import *
import os
__payload = Payload(Payload.PAYLOAD_REQUEST_WEBHOST)
__payload.wrap_payload(os.getcwd(), "Station")