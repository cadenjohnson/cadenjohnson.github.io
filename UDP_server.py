# Server side code to receive message
import socket

# Define the IP and the port
IP_ADDRESS = "127.0.0.1"
PORT_NO = 65432
message=""

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the IP and port to the new socket object
serverSock.bind((IP_ADDRESS, PORT_NO))
print("Listening on port ", PORT_NO," for ", IP_ADDRESS, " . . .\n\n")

# Listen to the socket until it is terminated
while message!='q':
    data = serverSock.recvfrom(1024)
    message = data[0].decode()
    host = data[1]
    print(host, "--> ", message)
    
    #used to send messages back
    #serverSock.sendto(message.encode(), host)

serverSock.close()
