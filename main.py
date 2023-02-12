import sys
sys.path.append('modules')
import sheet
import battle
from sheet import char
from battle import atk
char.name = input("Enter character name:")
while True:
    print("What would you like to do?")
    goto = input("check character sheet - c, battle - b:")
    if goto == "c":
        print(char.name)
        print("hp:",char.maxhp)
        print("str:",char.str)
        print("int:",char.int)
    elif goto == "b":
        print("you pressed b")
        atk.battle()
        break
    else:
        print("you fucked up")