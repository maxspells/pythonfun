class shop:
    def hello():
        print("Hello! Welcome to the item shop!")
        print("What can I get you?")
        while True:
            goto = input("buy - b, sell - s, heal - h, levelup - l, exit - e:")
            if goto == "b":
                shop.buy()
            elif goto == "s":
                shop.sell()
            elif goto == "h":
                shop.heal()
            elif goto == "l":
                shop.lvl()
            elif goto == "e":
                break
            else:
                print("invalid input")
    def buy():
        print("shop inventory here")
    def sell():
        print("sell inventory here")
    def heal():
        print("code to spend money to heal")
    def lvl():
        print("level up here")