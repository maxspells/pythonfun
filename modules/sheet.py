class char:
    name = "default"
    str = 10
    int = 10
    maxhp = 20
    currenthp = 20
    xp = 0
    gp = 0
class sheet:
    def cs():
        print(char.name)
        print("HP:",char.currenthp,"/",char.maxhp)
        print("STR:",char.str)
        print("INT:",char.int)
        print("Gold:",char.gp)
        print("EXP:",char.xp)