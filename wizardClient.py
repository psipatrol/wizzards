import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(('127.0.0.1', 9797))
name = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(name, "utf-8"))

strength = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(strength, "utf-8"))
health = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(health, "utf-8"))
defense = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(defense, "utf-8"))
agility = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(agility, "utf-8"))
atck1 = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(atck1, "utf-8"))
atck2 = input(clientSocket.recv(1024).decode())
clientSocket.send(bytes(atck2, "utf-8"))

print("WELCOME")
print(clientSocket.recv(1024).decode())

print("FIGHT LOG")
while True:
    try:
        message = clientSocket.recv(1024).decode()
        if not message:
            break
        print(f"{message}")
    except:
        break

print("FIGHT ENDED")
clientSocket.close()
