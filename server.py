import socket
import threading

#configuration variables

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

#creating the server ipv4 and streaming data
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected  = True
    while connected:
        # HEADER LENGTH CODE

        # msg_length = conn.recv(HEADER).decode(FORMAT)
        # msg_length = int(msg_length)
        # msg = conn.recv(msg_length).decode(FORMAT)

        #WITHOUT A HEADER

        #accepting 2048 byte message
        msg = conn.recv(2048).decode(FORMAT) 

        #checking if there is a message (avoiding empty connection messages)
        if msg: 

            #HANDLING DISCONNECT
            if msg == DISCONNECT_MSG :
                connected = False 

            print(f"[{addr}] {msg}")
        
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        conn , addr = server.accept()

        #new thread for new connection
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        
        #there is always 1 active for the server thats why - 1 is came
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") 
    
   
print(SERVER)
print('[STARTING] server is starting')
start()

