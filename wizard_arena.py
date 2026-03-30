from wizard import Wizard
from attack import Attack
from generator import fight
from attackType import AttackType

attacks = [Attack(AttackType.FIREBALL, 30),
           Attack(AttackType.MEOW, 5)]

thomasTheWizard = Wizard("Tomasz Niszczyciel", 100, attacks, 10, 4, 4)
orangeCar = Wizard("Koteczek", 60, attacks, 10, 4, 4)

for f in fight(orangeCar, thomasTheWizard):
    print(f)