#Simple Port Scanner
import socket
import ipinfo
import time

#global variable - s=creates a stream socket IP4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#functions
def iplookup():
	try:
		#ipinfo ip lookup
		access_token = '837a8b2c1fbfa9' #get token at ipinfo.io
		handler = ipinfo.getHandler(access_token)
		ip_address = target
		details = handler.getDetails(ip_address)
		
		#details pulled
		ip_city = details.city
		ip_country = details.country_name
		ip_hostname = details.hostname

		print("\n[*][Target: " + target)
		print("[*][GeoInfo: "+ ip_city + ", " + ip_country)
		print("[*][Hostname: " + ip_hostname)
	except:
		print("Unable to lookup that IP address.")

def portscan(port):
	try:
		s.connect((target,port))
	except: 
		return False
	else:
		return True

#Main code
print("\n" * 50)
print(" __________________________________________")
print("|                                          |")
print("|           Simple Port Scanner            |")
print("|__________________________________________|\n")
#input validation needed
target = input("Please enter IP address to scan (1.1.1.1):\n\t> ")
portr1 = input("Please enter port range to scan (1-65535): \n\tFirst Port> ")
portr2 = input("\t Last Port> ")
tic = time.perf_counter()

iplookup()

print("[ ]\n[*][Scan initiated on target.\n[*][Scanning " + 
	target + ", ports: " + portr1 + "-" + portr2)

oports = []

for port in range(int(portr1),(int(portr2)+1)):
	print("[-][Scanning port "+ str(port) +"...")
	if portscan(port):
		print("[!][Port "+ str(port) +": Open")
		oports.append(port)

toc = time.perf_counter()
timer = round(toc - tic, 2)

print("[ ]\n[*][Scan completed in " + str(timer) + 
	" seconds.\n[*][Target: " + target + "\n[*][Scanned ports: " 
	+ portr1 + "-" + portr2 + "\n[*][Open ports: " + str(oports))
