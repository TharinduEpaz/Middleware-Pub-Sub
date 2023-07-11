import socket
import sys

PORT = 5050
HEADER = 64
SERVER = '192.168.8.205'
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

# Extract the command-line arguments

# script_name = sys.argv[0]
# ip_address = sys.argv[1]
# port = sys.argv[2]
# role = sys.argv[3]
message = sys.argv[1]


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


client.send(message.encode(FORMAT))
