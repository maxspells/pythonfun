import sys
sys.path.append('modules')
import sheet
import battle
import creature
from sheet import char
from creature import mon
from battle import atk,battle
print("Welcome to my dumbass game")
char.name = input("Enter character name:")
while True:
    print("What would you like to do?")
    goto = input("check character sheet - c, battle - b, exit game - e:")
    if goto == "c":
        print(char.name)
        print("hp:",char.maxhp)
        print("str:",char.str)
        print("int:",char.int)
        print("xp:",char.xp)
    elif goto == "b":
        mon.currenthp = mon.maxhp
        char.currenthp = char.maxhp
        battle.battlewon=False
        while battle.battlewon == False:
            if char.currenthp>0 and mon.currenthp>0:
                battle.turn()
                battle.enemyturn()
            else:
                print("battle has ended")
                break
    elif goto == "e":
        break
    else:
        print("invalid input")
print("thanks for playing")