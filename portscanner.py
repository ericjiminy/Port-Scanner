from datetime import datetime
import socket
import sys

target = input("Enter a target to scan: ")   # get ip/domain
targetIP = socket.gethostbyname(target)

startPort = int(input("Enter a start port: "))	# get port range
endPort = int(input("Enter an end port: "))

print("Scanning started at: " + str(datetime.now()))	# start time
print("Please wait, scanning target now: " + target)	# wait msg

try:
	for port in range(startPort, endPort):	# loop thru port range
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((targetIP, port))   # try connecting to port
		sock.close()

		status = "close"
		if result == 0:
			status = "open"
		print("Port " + str(port) + ":         " + status)   # print port and status


except socket.error:	# catch socket error
    print("\n An error occurred...")
    sys.exit(1)

print("Port Scanning Completed")    # done msg