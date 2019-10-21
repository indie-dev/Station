# Station
Station is a peer-to-peer docker-like program that allows you to store files and execute programs (code, binary files, etc) on another user's computer, allowing 
for you to potentially reduce server costs for web hosting. The future for this program involves sandboxing unpacked containers so that no hacker or person with 
malicious intent can execute viruses or malware on your machine.

Currently, station can do these few things:
1. Find computers associated with a neighbor computer
2. Host a list of computers your machine knows
3. Host a list of containers that your machine has

What I hope in the future is to centralize some bits of information for creating custom alpha-numeric identifiers for containers, allowing multiple containers 
to have the same name.

# Instructions?
Currently, its best to run the test.py file as this project is new and has no instructions manual.
I also suggest allowing port forwarding for port 2087 and 8080 on your router, linking them back to
your static ip address. 2087 is the port used for hosting information such as the index.html page generated
when you run the function unpack_container, residing in the Container class. Port 8080 is what is used
for web hosting, in case that the container you have is actually a website.