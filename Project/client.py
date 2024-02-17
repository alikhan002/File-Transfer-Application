import socket
import time
import os
from math import ceil
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno

def connect_to_server(dept, port):
	s = socket.socket()
	host = socket.gethostname()
	time.sleep(1)
	s.connect((host,port))
			
	download_flag = askyesno(title='Transfer', message='Do you want to download a file?')
	if download_flag:
		s.send("1".encode())
	else:
		s.send("0".encode())
	if download_flag:
		filepath = filedialog.askopenfilename(initialdir = dept, title = "Select a File to download", filetypes = [("all files", "*.*"), ("Text files", "*.txt*"), ("PDF files", "*.pdf*")])
		s.send(filepath.encode())

		temp_filename = filepath.split('/')
		filename = temp_filename[-1]

		f = open(filename, "wb")
		while True:
			data = s.recv(1024)
			if data:
				f.write(data)
			else:
				break
		f.close()

	else:
		filepath = filedialog.askopenfilename(initialdir = "~", title = "Select a File to upload", filetypes = [("all files", "*.*"), ("Text files", "*.txt*"), ("PDF files", "*.pdf*")])
		s.send(filepath.encode())

		filesize = os.path.getsize(filepath)
		segments = ceil(filesize/1024)

		f = open(filepath, "rb")
		for i in range(segments):
			data = f.read(1024)
			s.send(data)
		f.close()

window = Tk()

window.title('CN Project')

width= window.winfo_screenwidth()
height= window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))

window.config(background = "white")

label_file_explorer = Label(window, text = "Select your department", font=("Arial", 30, 'bold'), width = 100, height = 4, fg = "blue")
label_file_explorer.place(x = width/2-25, anchor = N)

button_CS = Button(window, text = "Computer Science", height=3, width=20, fg = "white", bg = "blue", font=("Arial", 20, 'bold'), command=lambda: connect_to_server("./Computer_Science/", 8081))
button_SE = Button(window, text = "Software Engineering", height=3, width=20, fg = "white", bg = "blue", font=("Arial", 20, 'bold'), command=lambda: connect_to_server("./Software_Engineering/", 8082))
button_AI = Button(window, text = "Artificial Intelligence", height=3, width=20, fg = "white", bg = "blue", font=("Arial", 20, 'bold'), command=lambda: connect_to_server("./Artificial_Intelligence/", 8083))
button_CY = Button(window, text = "Cyber Security", height=3, width=20, fg = "white", bg = "blue", font=("Arial", 20, 'bold'), command=lambda: connect_to_server("./Cyber_Security/", 8084))
button_exit = Button(window, text = "Exit", height=3, width=20, font=("Arial", 20, 'bold'), fg = "white", bg = "red", command = exit)


button_CS.place(x = width/5-200, y = height/3, anchor = W)
button_SE.place(x = width/5+200, y = height/3, anchor = W)
button_AI.place(x = width/5+600, y = height/3, anchor = W)
button_CY.place(x = width/5+1000, y = height/3, anchor = W)
button_exit.place(x = width/2-200, y = height/2, anchor = W)

window.mainloop()
