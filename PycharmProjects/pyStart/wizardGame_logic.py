import random


class wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.life = 3

    def __repr__(self):
        print("this is a {} with level {}".format(self.name, self.level))

    @classmethod
    def attack(self,gandalf,active_creature):
        my_roll = random.randint(1, 12)*gandalf.level
        creature_roll = random.randint(1, 12) * active_creature.level
        if my_roll >= creature_roll:
            return True
        elif gandalf.life > 1:
            gandalf.life -= 1
            return False
        else:
            gandalf.life = 0
            return False


class creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        print("this is a {} with level {}".format(self.name, self.level))
