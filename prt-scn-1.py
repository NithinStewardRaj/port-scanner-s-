#!/usr/bin/python

import socket 

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input("\033[1;32;40m [*]Enter the IP to scan: ")
port = int(raw_input("\033[1;32;40m [*]Enter the port to scan: "))

def portscanner(port):
	if soc.connect_ex((host,port)):
		print "\033[5;31;40m port %d is closed :(" % (port)
	else:
		print "\033[5;33;40m port %d is open ;)" % (port)

portscanner(port)
