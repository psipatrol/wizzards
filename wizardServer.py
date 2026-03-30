import socket
import threading
import time

import wizard
from conn_thread import server_listen
from generator import fight

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
serverSocket.bind(('127.0.0.1', 9797))
serverSocket.listen(2)
serverSocket.settimeout(30.0)

print(f"listening on {serverSocket.getsockname()}")
maxWizard = 2
wizard_conn_map = {}
connections = []

def send(message):
    print("sending to every wizard")
    for conn in connections:
        try:
            conn.send(bytes(message, "utf-8"))
        except:
            pass

def send_to(target, message):
    print("sending to every wizard")
    conn = wizard_conn_map.get(target)
    if conn:
        try:
            conn.send(bytes(message, "utf-8"))
        except:
            pass

while len(connections) < maxWizard:
    try:
        connection, address = serverSocket.accept()
        print(f"noticed connection from {address}")
        connections.append(connection)
        t = threading.Thread(target=server_listen, args=(connection, address, wizard_conn_map))
        t.start()
    except socket.timeout:
        print("timeout")
        break

while len(wizard_conn_map) < maxWizard:
    time.sleep(0.1)

send("There will be blood\n")
time.sleep(0.5)

for attacker, defender, fight_unit in fight(list(wizard_conn_map.keys())[0], list(wizard_conn_map.keys())[1]):
    if fight_unit == "SLAYED":
        send_to(attacker, f"\nYou slayed {defender.name}")
        send_to(defender, f"\n{attacker.name} slayed you")
    else:
        send_to(attacker, f"You attack {defender.name} {fight_unit}")
        send_to(defender, f"{attacker.name} attacks you {fight_unit}")
        send_to(attacker, f"{attacker.current_status()}\n")
        send_to(defender, f"{defender.current_status()}\n")
        time.sleep(0.5)

send("...")

for conn in connections:
    conn.close()

