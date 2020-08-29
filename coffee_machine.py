class CoffeeMachine:
    espresso = {'water': 250, 'milk': 0, 'coffee': 16, 'money': 4}
    latte = {'water': 350, 'milk': 75, 'coffee': 20, 'money': 7}
    cappuccino = {'water': 200, 'milk': 100, 'coffee': 12, 'money': 6}
    menus = {1: espresso, 2: latte, 3: cappuccino}

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cup = 9
        self.money = 550
        self.unavailable_menu = dict()
        # {1: 'water'}
        self.check_resource()

    def buy(self, menu):
        if menu not in self.unavailable_menu:
            if menu in self.menus:
                self.water -= self.menus[menu]['water']
                self.milk -= self.menus[menu]['milk']
                self.coffee -= self.menus[menu]['coffee']
                self.cup -= 1
                self.money += self.menus[menu]['money']
                self.check_resource()
            print('I have enough resources, making you a coffee!\n')
        else:
            print(f'Sorry, not enough {self.unavailable_menu[menu]}!\n')

    def fill(self, water, milk, coffee, cup):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cup += cup
        self.check_resource()

    def take(self):
        print(f'I gave you ${self.money}\n')
        self.money = 0

    def status(self):
        print('The coffee machine has:',
              f'{self.water} of water',
              f'{self.milk} of milk',
              f'{self.coffee} of coffee beans',
              f'{self.cup} of disposable cups',
              f'${self.money} of money\n', sep='\n')

    def check_resource(self):
        self.unavailable_menu = dict()
        for menu, resource in self.menus.items():
            water = self.water >= resource['water']
            milk = self.milk >= resource['milk']
            coffee = self.coffee >= resource['coffee']
            if not water:
                self.unavailable_menu[menu] = 'water'
            elif not milk:
                self.unavailable_menu[menu] = 'milk'
            elif not coffee:
                self.unavailable_menu[menu] = 'coffee'


def main():
    coffee_machine = CoffeeMachine()
    while True:
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        print()
        if action == 'buy':
            menu = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            if menu == 'back':
                continue
            coffee_machine.buy(int(menu))
        elif action == 'fill':
            water = int(input('Write how many ml of water the coffee machine has:\n'))
            milk = int(input('Write how many ml of milk the coffee machine has:\n'))
            coffee = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
            cup = int(input('Write how many disposable cups of coffee do you want to add:\n'))
            coffee_machine.fill(water, milk, coffee, cup)
            print()
        elif action == 'take':
            coffee_machine.take()
        elif action == 'remaining':
            coffee_machine.status()
        elif action == 'exit':
            break


# implement here
main()
