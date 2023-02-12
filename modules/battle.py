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
        if mon.currenthp > 0:
            print(mon.currenthp,"hp remaining!")
    def pattack():
        mdmg = random.randint(1,10)+char.str
        mon.currenthp = (mon.currenthp-mdmg)
        print("Melee attack for ",mdmg," damage!")
        if mon.currenthp > 0:
            print(mon.currenthp,"hp remaming!")
    def battle():
        while True:
            if mon.currenthp>0:
                print("What would you like to do?")
                goto = input("Spell attack - s, Melee attack - m:")
                if goto == "s":
                    atk.pspell()
                elif goto == "m":
                    atk.pattack()
                else:
                    print("invalid input")
            else:
                print("The monster is slain!")
                break