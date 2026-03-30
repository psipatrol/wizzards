import socket
from wizardHandler import build

def server_listen(connection, address, wizard_conn_map):
    try:
        print(f"established connection with {address}")
        wizard = build(connection)
        wizard_conn_map[wizard] = connection
        print(f"wizard {wizard.name} is ready")
    except Exception as e:
        print(f"error while connecting to {address} \n{e}")
        connection.close()
