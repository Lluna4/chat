from logging import error
import socket
import threading
#import telebot
import asyncio

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!desconectar"

#bot = telebot.AsyncTeleBot("1695155940:AAGntm1f5wrH7fM4N6JVWSrD552xekryTDs", parse_mode=None)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

c = False
c2 = 0


clients = [] 
clients_lock = threading.Lock()

def bot2(conn, addr):
    conectado = True
    while True:
        
        msg = conn.recv(1024).decode(FORMAT)
        print(msg)
        msg = msg.encode(FORMAT)
        with clients_lock:
            for client in clients:
                client.send(msg)
                print("Enviado!")




                


   

def start():
    global c
    server.listen()

    print(f"El servidor acepta nuevas conexiones en {SERVER}")
    while True:
        conn, addr = server.accept()
        print("si")
        if c == False:
            x2 = threading.Thread(target=bot2, args=(conn, addr))
            x2.start()
            
        
        clients.append(conn)
        print(type(clients))
        print(clients)
    
          
    



print("El servidor se esta iniciando")


x1 = threading.Thread(target=start)

x1.start()



