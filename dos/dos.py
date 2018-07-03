from sys import exit
from socket import *
import requests
import os

os.system("clear")
os.system("python banner.py")
def help():
	print("""\n\x1b[93mThere Is Dos Attack Area.Dos Means Denical Of Service.You Can Attack To A Website With This And After That Your Attack 
Finished,Site Coudlnt Show!It Will Have This Error:Server Internal Error.\x1b[39m\n""")
	
a = input("Enter Website Address To Start DOS Attack(If You Want To Know What Is Dos Write 'help'):{e.g example.com}")
if a == "back" or a == "exit":
	exit()
if a == "help":
	help()
	a = input("Enter Website Address To Start DOS Attack:{e.g example.com}")
	a = a.replace("http://","")
	os.system("python3 dos/attack.py " + a)
else:
	a = a.replace("http://","")
	os.system("python3 dos/attack.py " + a)
