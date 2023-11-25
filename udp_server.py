import socket
import random
import dataBase

serverPort = 7502
clientPort = 7500
serverAddressPort = ("127.0.0.1")  # destination
bufferSize = 1024  # message transmission size

# creates UDP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sets up server to receive from clients
server.bind((serverAddressPort, serverPort))
print("UDP server up and listening")

greenPlayer = 0
redPlayer = 0

while (True):
    # recieves client message and client ip address
    msgFromClient, clientAddress = server.recvfrom(bufferSize)

    # prints client info
    print("Message from Client:{}".format(msgFromClient))
    print("Client IP Address: {}".format(clientAddress))
    print("----------------------------------")
    
    
    # Simulate game logic
    # For example, check for specific codes and take appropriate actions
    import playActionDisplay

    if msgFromClient.decode('utf-8') == "53":
        print("Code 53 received: Red base scored!")
        randomGreenPlayer = dataBase.getRandomGreenPlayer()
        dataBase.updatePlayerScore(randomGreenPlayer, 100)
        # playActionDisplay.updateTableGreen(playActionDisplay.greenFrame)
        #update code to correctly select from someone that is red or green
        # Implement your scoring logic for the red team
    elif msgFromClient.decode('utf-8') == "43":
        print("Code 43 received: Green base scored!")
        randomRedPlayer = dataBase.getRandomRedPlayer()
        dataBase.updatePlayerScore(randomRedPlayer, 100)
        # playActionDisplay.updateTableRed(playActionDisplay.redFrame)
        # Implement your scoring logic for the green team
    else:
        # sends message back to client
        msgFromClientStr = msgFromClient.decode('utf-8')
        msgFromServer = "Player " + msgFromClientStr + " has been confirmed: REPORTED"
        bytesToSend = str.encode(msgFromServer)
        server.sendto(bytesToSend, clientAddress)

# # kills the server
# if (msgFromClient.decode('utf-8') == "exit"):
#     break

