#Simple Port Scanner
import socket
import ipinfo

#global variable - s=creates a stream socket IP4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#functions
def iplookup():
	try:
		#ipinfo ip lookup
		access_token = '123456789abc'
		handler = ipinfo.getHandler(access_token)
		ip_address = target
		details = handler.getDetails(ip_address)
		
		#details wanted
		ip_city = details.city
		ip_country = details.country_name
		ip_hostname = details.hostname

		# print/confirm scan?
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
portr1 = input("Please enter port range to scan (1-65535): \n\tStart Port> ")
portr2 = input("\tEnd Port> ")
iplookup()
#add in confirm scan
print("\nScan initiated on Target:\n" + target + ", on ports: "
 + portr1 + "-" + portr2)

for port in range(int(portr1),(int(portr2)+1)):
	print("Scanning port "+ str(port) +"...")
	if portscan(port):
		print("Port "+ str(port) +": Open")
