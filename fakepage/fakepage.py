from sys import exit
import os

os.system("clear")
os.system("python3 banner.py")
a = input("\x1b[92mEnter Target Address:{e.g http://xyz.com}\x1b[39m")
if a == "back" or a == "exit":
	exit()
os.system("httrack " + a + " -O fakepage/fakepages")
