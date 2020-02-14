from socket import AF_INET, socket, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM) 

bufferSize = 2048

Host = ""
Port = 22

server.bind((Host, Port))

server.listen(5000)

print("Server started")

while True:
    DoMessage = input("Do you wish to send them a message before you close the connection? Y/N   >  ")

    if DoMessage == "Y":
        DoMessage = True
        break

    elif DoMessage == "N":
        DoMessage = False
        break

    else:
        print("Invalid input")

if DoMessage == True:
    message = str(input("\nWhat do you want to send them?   >  "))

else:
    message = ""

print("Init. Successful")

def Main(server, bufferSize, DoMessage, message):
    print("Started main")
    logfile = open("log.txt", "a")
    while True:
        try:
            connection, address = server.accept()

            logfile.write('\n' + str(address)

            print("\nReceived from " + str(address))

            if DoMessage == True:
                connection.send(bytes(message, "utf8"))

            connection.close()
        except:
            print("Error, passing")

Main(server, bufferSize, DoMessage, message)