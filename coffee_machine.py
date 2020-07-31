class CoffeeMachine:
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'money': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'money': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'money': 6}
    list = {1: espresso, 2: latte, 3: cappuccino}

    def __init__(self):
        self.amount_water = 400
        self.amount_milk = 540
        self.amount_beans = 120
        self.amount_disposable_cups = 9
        self.amount_money = 550

    def __repr__(self):
        return "CoffeeMachine ({}, {}, {}, {}, {})".format(self.amount_water, self.amount_milk, self.amount_beans,
                                                           self.amount_disposable_cups, self.amount_money)

    def buy(self, menu):
        self.amount_water -= self.list[menu]['water']
        self.amount_milk -= self.list[menu]['milk']
        self.amount_beans -= self.list[menu]['beans']
        self.amount_disposable_cups -= 1
        self.amount_money -= self.list[menu]['money']

        return amounts


amounts = CoffeeMachine()

print(repr(amounts))
print(amounts.buy(3))
print(repr(amounts))

def main():
    coffeemachine = CoffeeMachine
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")


# is it right?