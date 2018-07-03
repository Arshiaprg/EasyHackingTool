from sys import exit
import random
import os

os.system("clear")
method = input("""\x1b[32mEnter Sql Method:
1)Search For Vulnerable Websites
2)Target Scan From Sql Attack

0)exit

:""")

if not os.path.isdir("sql/sqliv"):
	os.system("git clone https://github.com/the-robot/sqliv.git")

if int(method) == 1:
	d = input("Enter Your Dork For Attack:(If You Dont Know Dork,Type 'nd')")
	if d == "nd":
		a = []
		f = open("sql/sqldork.txt","r")
		for i in f.readlines():
			a.append(i)
		f.close()
		n = random.randint(0,len(a))
		d = a[n].replace("\n","")
	e = input("Enter Your Search Place:(google,yahoo,bing)")
	if not e in ["google","yahoo","bing"]:
		print("Wrong Search Palace")
		exit()
	os.system("python2 sql/sqliv/sqliv.py -d " + d + " -e " + e)
elif int(method) == 2:
	t = input("Enter Target: ")
	os.system("python sql/sqliv/sqliv.py -t" + t)
elif int(method) == 0:
	exit()
else:
	pass
