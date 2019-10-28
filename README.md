# What is Station?
Station is an open source, peer-to-peer based Docker alternative. Station allows for you to not only share your payload, but to gain terminal access to the files inside of the payload on someone else's machine, provided they setup Station to allow you to do so.

# What can station currently do?
1. Given a neighbor station, station can find all stations that station knows. It then iterates through all of the stations that new station knows, all until it runs into an END_OF_BRANCH, or the last station on that branch.

2. Station can currently package your payload, but not ship it off just yet. I am still working on the entire network, so come back in a few months or years.


# What does Station hope to do?
1. Decrease server costs for web developers
2. De-centralize file sharing / file hosting
3. Use unique identifiers for downloading payloads instead of going off of the name
4. Use checksum verification methods for uploading modified versions of the payload
5. Use a custom compression library for payloads, hopefully reducing space used per payload by 30%
6. Password encrypting uploaded payloads to prevent hosters from accessing a user's payload
7. Forcing hosters to use Linux for a permanent move to support linux-only terminal request types. This is because I plan on having the application download a light form of linux and inject that into the payload before launching the payload into the network. This is only for payloads that request terminal access.

As for webhosting, requiring that the user has either xampp or php installed does sound very promising.