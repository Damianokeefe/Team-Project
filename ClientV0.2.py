from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from tkinter import *
from PIL import Image

#Clear msg field
def clear(event):
    if msg.get() == "Enter your message here":
        msg.set("")
    return None

#Recieve messages, until broken, or encounter an error
def receive():
    while True:
        try:
            message = clientSock.recv(1024).decode()
            if ":joy:" in message:
                splitat = message.find(':joy:')
                message = message.replace(":joy:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=joy)
                msgHis.insert(tk.END, last)
            elif ":100:" in message:
                splitat = message.find(':100:')
                message = message.replace(":100:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=hun)
                msgHis.insert(tk.END, last)
            elif ":cool:" in message:
                splitat = message.find(':cool:')
                message = message.replace(":cool:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=cool)
                msgHis.insert(tk.END, last)
            elif ":cry:" in message:
                splitat = message.find(':cry:')
                message = message.replace(":cry:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=cry)
                msgHis.insert(tk.END, last)
            elif ":smiley:" in message:
                splitat = message.find(':smiley:')
                message = message.replace(":smiley:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=smiley)
                msgHis.insert(tk.END, last)
            elif ":tired:" in message:
                splitat = message.find(':tired:')
                message = message.replace(":tired:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=tired)
                msgHis.insert(tk.END, last)
            elif ":yum:" in message:
                splitat = message.find(':yum:')
                message = message.replace(":yum:", "")
                first, last = message[:splitat], message[splitat:]
                msgHis.insert(tk.END, first)
                msgHis.image_create(tk.END, image=yum)
                msgHis.insert(tk.END, last)
            else:
                msgHis.insert(tk.END, message+"\n")
        except OSError:
            break

#Create sending function
def send(event=None):
    msgSend = msg.get()
    msg.set("")
    clientSock.send((msgSend).encode())
    if msgSend == "{quit}":
        clientSock.close()
        window.quit()

#Close funtion to send close message
def close(event=None):
    msg.set("{quit}")
    send()

#Create window
window = tk.Tk()
window.title("Chef's Client")
window.configure(background='#2F3136')

#Create Meesage Frame
msgFrame = tk.Frame(window)
msg = tk.StringVar()
msg.set("Enter your message here")

#Create Scrollbar
scroll = tk.Scrollbar(msgFrame)

#Create Message Frame, pack scroll bar onto it
msgHis = Text(msgFrame, height=15, width=50, yscrollcommand=scroll.set, background='#36393F', foreground='#FFFFFF', borderwidth=0, highlightthickness=0, font=13)
scroll.config(command=msgHis.yview)
scroll.pack(side=RIGHT, fill=Y)
msgHis.pack(side=LEFT, fill=BOTH, expand=1)
msgFrame.pack(fill=BOTH, expand=1)

#Create Message Field, create clearing, and sending
msgField = tk.Entry(window, width=52, textvariable=msg, background='#484B51', foreground='#FFFFFF', font=15)
msgField.bind("<Return>", send)
msgField.bind("<Button-1>", clear)
msgField.pack(fill=BOTH)

#Create Protocol to close
window.protocol("WM_DELETE_WINDOW", close)

#Get HOST and PORT, if net specified set defaults
HOST = input('Enter host: ')
if not HOST:
    HOST = '127.0.0.1'
else:
    HOST = int(HOST)

PORT = input('Enter port: ')
if not PORT:
    PORT = 5000
else:
    PORT = int(PORT)

ADDR = (HOST,PORT)

#Create Socket
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(ADDR)

#Start Recieving, until broken
receive_thread = Thread(target=receive)
receive_thread.start()

#Create Emojis
size = 5,5
joy = PhotoImage(file='./joy.png')
hun = PhotoImage(file='./100.png')
cool = PhotoImage(file='./cool.png')
cry = PhotoImage(file='./cry.png')
smiley = PhotoImage(file='./smiley.png')
tired = PhotoImage(file='./tired.png')
yum = PhotoImage(file='./yum.png')
#joy = Image.open('./joy.png')


#Main loop to create gui
tk.mainloop()