import random

import time

from wizardGame_logic import creature, wizard


def main():
    creatures = [creature("toad", 1), creature("bat", 3), creature("tiger", 10), creature("dragon", 50),
                 creature("evil wizard", 100)]


    gandalf = wizard("gandalf", 75)
    print("hello i am {} having level {}".format(gandalf.name,gandalf.level))


    while creatures and gandalf.life > 0:
        active_creature = random.choice(creatures)
        print("a giant {} comes in front of you...".format(active_creature.name))
        cmd = input("do you [a] attack  [r]run away or [l]look around...  ")
        result = False
        if cmd == 'a':
            result = wizard.attack(gandalf,active_creature)
            if result == True:
                print("you have defeated the {}".format(active_creature.name))
                creatures.remove(active_creature)
            else:
                if result==False and gandalf.life == 0:
                    print("oops  all your lives are over...game over... ")
                    break
                else:
                    print("the {} defeated you..  take rest".format(active_creature))
                    time.sleep(10)

        elif cmd=='l':
            print("around you u have..\n")
            for c in creatures:
                print("a {} of level {} ".format(c.name,c.level))



main()
