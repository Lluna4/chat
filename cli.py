import socket
import threading
import time
#import telebot
#import network

#bot = telebot.TeleBot("1695155940:AAGntm1f5wrH7fM4N6JVWSrD552xekryTDs", parse_mode=None)


HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!desconectar"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
corriendo = True

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)
conectado = True



def recibir():
    global conectado
    while conectado == True:
        msg2 = cliente.recv(1024).decode(FORMAT)
        #print("Recibido!")
        
        print(msg2)



def enviar(msg): # codifica el mensaje (msg) y lo manda al servidor
    mensaje = msg.encode(FORMAT)
    msg_lenght = len(mensaje)
    mandar_mensaje = str(msg_lenght).encode(FORMAT)
    mandar_mensaje += b" " * (HEADER - len(mandar_mensaje))
    #cliente.send(mandar_mensaje)
    cliente.send(mensaje)
    #print(cliente.recv(2048).decode(FORMAT))



x1 = threading.Thread(target=recibir)
x1.start()

while conectado == True:
    msg = input(":")
    enviar(msg)
    time.sleep(0.1)
    





