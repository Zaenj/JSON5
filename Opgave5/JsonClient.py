from socket import *
import json

serverPort = 12000
serverHost = "127.0.0.1"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

while True:
    command = input('Enter command (Random/Add/Subtract/Exit): ').lower()
    
    if command == "exit":
        request = {"method": "Exit"}
    elif command in ["random", "add", "subtract"]:
        arg1 = int(input('Enter first number: '))
        arg2 = int(input('Enter second number: '))
        request = {"method": command, "Tal1": arg1, "Tal2": arg2}
    else:
        print("Invalid command.")
        continue
    
    clientSocket.send(json.dumps(request).encode())
    response = json.loads(clientSocket.recv(1024).decode())
    
    if "result" in response:
        print('Server response:', response["result"])
    elif "error" in response:
        print('Server error:', response["error"])
    
    if command == "exit":
        break

clientSocket.close()
