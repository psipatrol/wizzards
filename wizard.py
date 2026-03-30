import random
from effects import Effect
from attackType import AttackType


def clamp(min_val, max_val, val_val, factor):
    return int((val_val - min_val) / max_val * factor)


class Wizard:

    def __init__(self, name, hp, attacks, strength, defense, agility):
        self.name = name
        max_val = max(hp, defense, strength, agility)
        self.hp = clamp(0, max_val, hp, 80)
        self.defense = clamp(0, max_val, defense, 80)
        self.strength = clamp(0, max_val, strength, 80)
        self.agility = clamp(0, max_val, agility, 80)
        self.attacks = list(attacks)
        self.effects = list()

    def add_attack(self, attack):
        self.attacks.append(attack)

    def add_effect(self, efctt):
        print(efctt.value)
        self.effects.append(efctt.value)

    def is_alive(self):
        return self.hp > 0

    def attack(self, opponent):
        if Effect.BURNING in self.effects:
            self.hp -= 2
            print(self.name + " is burning")
        if Effect.STUNNED in self.effects:
            self.effects.remove(Effect.STUNNED)
            return "you are stunned"
        if opponent.try_dodge():
            return " ...attack dodged"
        if opponent.defense > self.defense and random.uniform(0.0, 1.0) > 0.5:
            return " ...attack blocked"
        else:
            atck = random.choice(self.attacks)
            if atck.typee is AttackType.FIREBALL:
                opponent.add_effect(atck.typee)
            if atck.typee is AttackType.MEOW:
                opponent.add_effect(atck.typee)

            real_dmh = int(atck.damage * random.uniform(1.0, 1.4) + self.strength / 100)
            opponent.hp -= real_dmh
            return "with " + str(real_dmh)

    def try_dodge(self):
        if self.agility > random.uniform(0, 100):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}... \nSTR: {self.strength}\nHP: {self.hp}\nDEF: {self.defense}\nAGT: {self.agility}\n{self.attacks}"



