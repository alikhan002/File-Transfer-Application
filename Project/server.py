from sys import argv
import socket
import os
from math import ceil

path = argv[1]

host = "localhost"
port = int(argv[2])

s = socket.socket()
s.bind((host,port))
s.listen(1)

print("Waiting for any incoming connctions ... ")
conn, addr = s.accept()
print(addr, "Has connected to the server")

download_flag = conn.recv(1).decode()

if download_flag == "1":
	while True:
		filepath = conn.recv(1024).decode()
		if filepath:
			break
		else:
			continue
	filesize = os.path.getsize(filepath)
	segments = ceil(filesize/1024)
	
	f = open(filepath, "rb")
	for i in range(segments):
		data = f.read(1024)
		conn.send(data)
	f.close()

else:
	while True:
		filepath = conn.recv(1024).decode()
		if filepath:
			break
		else:
			continue
	
	temp_filename = filepath.split('/')
	filename = path + temp_filename[-1]

	f = open(filename, "wb")
	while True:
		data = conn.recv(1024)
		if data:
			f.write(data)
		else:
			break
	f.close()
