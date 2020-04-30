# Write your code here
class CoffeeMachine():
    status = "idle"
    
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.dis_cups = 9    

    def process(self, line):
        if self.status == "idle" and line == "buy":
            self.status = "choosing a type of coffee"
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
        elif self.status == "choosing a type of coffee":
            if line == "back":
                self.status = "idle"
            else:
                self.status = "idle"
                self.buy(int(line))
        elif self.status == "idle" and line == "fill":
            self.fill()
        elif self.status == "idle" and line == "take":
            self.take()
        elif self.status == "idle" and line == "remaining":
            self.print_state()
        elif self.status == "idle" and line == "exit":
            self.status = "off"
        

    def print_state(self):
        print("""The coffee machine has:
            """, self.water, """of water
            """, self.milk, """of milk
            """, self.coffee, """of coffee beans
            """, self.dis_cups, """of disposable cups
            """, "$"+str(self.money), "of money")

    def buy(self, type):
        global money
        global water
        global milk
        global coffee
        global dis_cups
        
        if type == 1:
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee < 16:
                print("Sorry, not enough coffee!")
            elif self.dis_cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.money += 4
                self.water -= 250
                self.coffee -= 16
                self.dis_cups -= 1
        elif type == 2:
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee < 20:
                print("Sorry, not enough coffee!")
            elif self.dis_cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.dis_cups -= 1
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee < 12:
                print("Sorry, not enough coffee!")
            elif self.dis_cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.dis_cups -= 1
        if self.dis_cups < 1:
            print("Sorry, not enough disposable cups!")        
            
    def fill(self):  
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.dis_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        
    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        
coffee_machine = CoffeeMachine()
    
while True:
    if coffee_machine.status == "idle":
        reply = coffee_machine.process(input("Write action (buy, fill, take, remaining, exit):"))
        if coffee_machine.status == "choosing a type of coffee":
            coffee_machine.process(input(reply))
    elif coffee_machine.status == "off":
        break