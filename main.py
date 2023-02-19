import sys
sys.path.append('modules')
import sheet
import battle
import creature
import shop
from shop import shop
from sheet import char,sheet
from creature import mon
from battle import atk,battle
print("Welcome to my game")
char.name = input("Enter character name:")
while True:
    print("What would you like to do?")
    goto = input("character sheet - c, battle - b, shop - s, exit game - e:")
    if goto == "c":
        sheet.cs()
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
    elif goto == "s":
        shop.hello()
    else:
        print("invalid input")
print("thanks for playing")