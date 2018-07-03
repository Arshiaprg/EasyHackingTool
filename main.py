from sys import exit
import os

os.system("clear")
os.system("python3 banner.py")
while True:
	print("""\x1b[32mThese Are Some Methods For You:
	
	1)Attack To A Platform
	2)Create Fake Page
	3)DOS Attack
	
	0)exit
	""")
	x = input("Which One Of Them Do You Want? :\x1b[39m")
	if int(x) == 1:
		os.system("python3 platform/attacker.py")
	elif int(x) == 2:
		os.system("python3 fakepage/fakepage.py")
	elif int(x) == 3:
		os.system("python3 dos/dos.py")
	elif int(x) == 0:
		exit()
	else:
		print("\x1b[91mEnter Valid Number...\x1b[39m")
		pass