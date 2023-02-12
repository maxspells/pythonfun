import sys
sys.path.append('modules')
import sheet
import battle
from sheet import char
from battle import atk
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
        atk.battle()
    elif goto == "e":
        break
    else:
        print("invalid input")
print("thanks for playing")