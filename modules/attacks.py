import random
import sheet
from sheet import char
class atk:
    def pspell():
        char.sdmg = random.randint(1,20)+char.int
        remaininghp = (char.ehp-char.sdmg)
        print("Spell attack for ",char.sdmg," damage!")
        if remaininghp > 0:
            print(remaininghp,"hp remaining!")
        else:
            print("The enemy is slain!")
    def pattack():
        mdmg = random.randint(1,20)+char.str
        remaininghp = (char.ehp-mdmg)
        print("Melee attack for ",mdmg," damage!")
        if remaininghp > 0:
            print(remaininghp,"hp remaming!")
        else:
            print("The enemy is slain!")