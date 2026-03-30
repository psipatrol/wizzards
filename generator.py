def fight(wizard1, wizard2):
    i = 0
    while wizard1.hp > 0 and wizard2.hp > 0:
        if (i % 2) == 0:
            yield wizard1, wizard2, wizard1.attack(wizard2)
        else:
            yield wizard2, wizard1, wizard2.attack(wizard1)
        i += 1
    yield (wizard1, wizard2, "SLAYED") if wizard1.hp > wizard2.hp else (wizard2, wizard1, "SLAYED")
