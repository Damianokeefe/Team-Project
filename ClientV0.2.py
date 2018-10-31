from socket import *
from tkinter import *

#closing function
def close():
    client.destroy()
    exit()

def sendM():
    message = send.get()
    clientSocket.send(message.encode())
    send.delete(0, END)

#Main
client = Tk()
client.title('Chat Client')
client.configure(background='black')
client.geometry('500x500')

#Create Send Message textfield
send = Entry(client, width=20, bg='white')
send.grid(row=1, column=0, sticky=W)

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while 1:

    #Message Box
    output = Text(client, width=75, height=6, wrap=WORD, background='white')
    output.grid(row=0, column=0, columnspan=2, sticky=W)

    responce = clientSocket.recv(1024).decode()
    output.insert(END, responce)

    # Create Send Button
    Button(client, text='Send', width=6, command=sendM).grid(row=1, column=0, sticky=E)

    # Exit button
    Button(client, text='EXIT', width=6, command=close).grid(row=6, column=0, sticky=W)

    #run mainloop
    client.mainloop()