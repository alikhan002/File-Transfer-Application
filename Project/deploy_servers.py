from os import system
import threading
def open_server(dept, port):
	system("python3 ./server.py " + dept + str(port))

CS_server = threading.Thread(target=open_server, args=("Computer_Science/ ", 8081,))
CS_server.start()

SE_server = threading.Thread(target=open_server, args=("Software_Engineering/ ", 8082,))
SE_server.start()

AI_server = threading.Thread(target=open_server, args=("Artificial_Intelligence/ ", 8083,))
AI_server.start()

CY_server = threading.Thread(target=open_server, args=("Cyber_Security/ ", 8084,))
CY_server.start()
