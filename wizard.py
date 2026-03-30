import random
from effects import Effect
from attackType import AttackType


def clamp(min_val, max_val, val_val, factor):
    return int((val_val - min_val) / max_val * factor)

attack_effect_map = {
    AttackType.FIREBALL : Effect.BURNING,
    AttackType.MEOW : Effect.STUNNED,
    AttackType.EARTHQUAKE : Effect.STUNNED,
    AttackType.ICY_KISS : Effect.INSANE,
}

class Wizard:

    def __init__(self, name, hp, attacks, strength, defense, agility):
        self.name = name
        max_val = max(hp, defense, strength, agility)
        self.hp = clamp(0, max_val, hp, 80)
        self.defense = clamp(0, max_val, defense, 80)
        self.strength = clamp(0, max_val, strength, 80)
        self.agility = clamp(0, max_val, agility, 80)
        self.attacks = list(attacks)
        self.effects = set()
        self.burning_duration = 0

    def add_attack(self, attack):
        self.attacks.append(attack)

    def add_effect(self, efctt):
        if attack_effect_map.get(efctt) is Effect.BURNING:
            self.burning_duration = 3
        self.effects.add(attack_effect_map.get(efctt))

    def is_alive(self):
        return self.hp > 0

    def current_status(self):
        current_effects = ""
        for effect in self.effects:
            current_effects += f"\n{effect.value}"
        return f"HP: {self.hp} {current_effects}"



    def attack(self, opponent):
        my_effect = ""
        other_effect = ""
        resolve = ""
        if Effect.BURNING in self.effects:
            self.burning_duration -= 1
            if self.burning_duration <= 0:
                self.effects.remove(Effect.BURNING)
        if Effect.BURNING in self.effects:
            self.hp -= 2
            # my_effect += " \n\tburning -2 HP"
        if Effect.STUNNED in self.effects:
            self.effects.remove(Effect.STUNNED)
            # my_effect += "\n\tbut you are stunned, attack canceled"
        else:
            # return "you are stunned"
            if opponent.try_dodge():
                resolve = "\n\tattack dodged"
            elif opponent.defense > self.defense and random.uniform(0.0, 1.0) > 0.5:
                resolve = "\n\tattack blocked"
            else:
                if self.attacks:
                    atck = random.choice(self.attacks)
                    if atck is AttackType.FIREBALL:
                        opponent.add_effect(atck)
                        other_effect += " fire"
                    if atck is AttackType.MEOW:
                        opponent.add_effect(atck)
                        other_effect += " stun"

                real_dmh = int(random.uniform(1.0, 1.4) + self.strength / 20)
                opponent.hp -= real_dmh
                resolve = "with " + str(real_dmh) + " DMG..."

        return f"{resolve} {my_effect} {other_effect}"

    def try_dodge(self):
        if self.agility > random.uniform(0, 160):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}... \nSTR: {self.strength}\nHP: {self.hp}\nDEF: {self.defense}\nAGT: {self.agility}\n{self.attacks}"



