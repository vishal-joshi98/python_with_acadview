# QUESTION 2: IP ADDRESS OF SOME SITE
import socket

google_ip = socket.gethostbyname("www.google.com")
facebook_ip = socket.gethostbyname("www.facebook.com")
print("\n \t IP ADDRESS OF GOOGLE = ", google_ip)
print("\n\t IP ADDRESS OF FACEBOOK = ", facebook_ip)