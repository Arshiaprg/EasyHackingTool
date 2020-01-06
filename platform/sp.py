import random
import socket

def oport(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('127.0.0.1',int(port)))
	if result == 0:
   		return True
	else:
		return False
num = 4444
random.seed()
while oport(num):
	num = random.randint(1000,5000)

print("ok")
f = open("port.txt","w")
f.write(str(num))
f.close()
