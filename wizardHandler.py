from attackType import AttackType
from wizard import Wizard


def welcome(connection):
    connection.send(b"I am honored to welcome you at mighty wizard arena!"
            b"\nPlease enter your magic wizard name:\n")
    buf = connection.recv(1024)
    return buf.decode()

def build(connection):
    connection.send(b"I am honored to welcome you at mighty wizard arena!"
            b"\nPlease enter your magic wizard name:\n")
    name = connection.recv(256).decode()
    connection.send(b"Excellent wizard name!"
                    b"\nnow its time to specify what kind of wizard your are"
                    b"\ndistribute your wizard skills wisely"
                    b"\n\ntype number between 0 and 100\n"
                    b"How strong wizard would you like to be?\t")
    try:
        strength = int(connection.recv(256).decode())
    except:
        strength = 1

    connection.send( b"How healthy wizard would you like to be?\t")
    try:
        health = int(connection.recv(256).decode())
    except:
        health = 1

    connection.send( b"How defense wizard would you like to be?\t")
    try:
        defense = int(connection.recv(256).decode())
    except:
        defense = 1

    connection.send( b"How agile wizard would you like to be?\t")
    try:
        agility = int(connection.recv(256).decode())
    except:
        agility = 1

    connection.send(b"Choose your primary attack\n" + bytes(show_attacks(), "utf-8"))
    try:
        atck1 = int(connection.recv(256).decode())
    except:
        atck1 = 0

    connection.send(b"Choose your secondary attack\n" + bytes(show_attacks(), "utf-8"))
    try:
        atck2 = int(connection.recv(256).decode())
    except:
        atck2 = 0

    attacks = compute_attacks((atck1, atck2))
    wizard = Wizard(name, health, attacks, strength, defense, agility)
    connection.send(bytes(wizard.__str__(), "utf-8"))
    return wizard
    
def show_attacks():
    res = ""
    for i, e in enumerate(AttackType):
        res += f"{i+1} - {e.name}\n"
    return res

def compute_attacks(atcks):
    attacks = []
    for i, e in enumerate(AttackType):
        if (i+1) in atcks:
            attacks.append(e)
    return attacks
        