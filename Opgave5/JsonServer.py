import threading
import json
from socket import *

serverPort = 12000
serverHost = "127.0.0.1"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)
print("Server is ready to connect")

def handleClient(connectionSocket, address):
    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        print(f"Received from {address}: {data}")
        
        try:
            request = json.loads(data)
            method = request.get("method", "").lower()
            arg1 = request.get("Tal1", None)
            arg2 = request.get("Tal2", None)

            if method == "random" and arg1 and arg2:
                import random
                result = random.randint(arg1, arg2)
            elif method == "add" and arg1 and arg2:
                result = arg1 + arg2
            elif method == "subtract" and arg1 and arg2:
                result = arg1 - arg2
            elif method == "exit":
                break
            else:
                raise ValueError("Invalid method or arguments")

            response = {"result": result}

        except Exception as e:
            response = {"error": str(e)}

        connectionSocket.send(json.dumps(response).encode())

    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
