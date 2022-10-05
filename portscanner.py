#!/bin/bash

import sys
import socket
from datetime import datetime

#defining our arguments

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translating hostb name

else:
	print("Invalid amount of arguments")
	print("SyNtAx====>pyhton3 prtscn.py <ip>")
	
#adding banner

print("-*-*" * 50)
print("scanning target" + target)
print("time started:" + str(datetime.now()))
print("-*-*" * 50)

try:
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("port {} is open ;)".format(port))
		s.close()
	
except KeyboardInterrupt:
	print("\n user interruption EXITING program")
	sys.exit()
except socket.gaierror:
	print("\n Hostname could not be resolved")
	sys.exit()
except socket.error:	
	print("Couldn't connect to the server")
	sys.exit()
	
	
	
	#happy hacking
