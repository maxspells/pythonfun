import random
import creature
import sheet
from sheet import char
from creature import mon
class atk:
    def pspell():
        char.sdmg = random.randint(1,10)+char.int
        mon.currenthp = (mon.currenthp-char.sdmg)
        print("Spell attack for ",char.sdmg," damage!")
        if mon.currenthp>0:
            print(mon.currenthp,"hp remaining!")
    def pattack():
        mdmg = random.randint(1,10)+char.str
        mon.currenthp = (mon.currenthp-mdmg)
        print("Melee attack for ",mdmg," damage!")
        if mon.currenthp>0:
            print(mon.currenthp,"hp remaming!")
    def eattack():
        mdmg = random.randint(1,10)+mon.str
        char.currenthp = (char.currenthp-mdmg)
        print(mon.name,"attacks you for",mdmg,"damage!")
        if char.currenthp > 0:
                print(char.currenthp,"hp remaining!")
class battle:
    battlewon = False
    def turn():
        while True:
            if battle.battlewon == True:
                print("The monster is slain!")
                char.xp = (char.xp+mon.xp)
                char.gp = (random.randint(1,10)+char.gp)
                break
            else:
                print("An angry",mon.name,"stands before you!")
                print("What would you like to do?")
                goto = input("Spell attack - s, Melee attack - m:")
                if goto == "s":
                    atk.pspell()
                    if mon.currenthp<=0:
                        battle.battlewon = True
                    break
                elif goto == "m":
                    atk.pattack()
                    break
                else:
                    print("invalid input")
    def enemyturn():
        while True:
            if battle.battlewon == True:
                print("The monster is slain!")
                char.xp = (char.xp+mon.xp)
                char.gp = (random.randint(1,10)+char.gp)
                break
            else:
                print("The",mon.name,"moves in to attack!")
                if char.currenthp>0:
                    atk.eattack()
                    break
                else:
                    print("You have died!")
                    break