import socket

# Declare IP address and port number
IP_ADDRESS = "127.0.0.1"
PORT_NO = 65432
message=""

# Create the socket object
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while message!='q':
    # Send the message
    message=input("(q to quit) --> ")
    clientSock.sendto(message.encode(), (IP_ADDRESS, PORT_NO))

    #used to recieve messages back
    #temp, addr = clientSock.recvfrom(1024)
    #print(temp.decode())
    
clientSock.close()
