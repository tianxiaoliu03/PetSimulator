# Pet class
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.sleepiness = 50
        self.coins = 0

    def feed(self):
        if self.coins >= 5:
            self.hunger -= 10
            self.coins -= 5
        else:
            print("Not enough coins to buy food.")

    def play(self):
        if self.happiness < 90:
            self.happiness += 10
        else:
            print(self.name + " is already very happy.")

    def sleep(self):
        if self.sleepiness < 90:
            self.sleepiness += 10
        else:
            print(self.name + " is already well-rested.")

    def check_status(self):
        print("Name:", self.name)
        print("Happiness:", self.happiness)
        print("Hunger:", self.hunger)
        print("Sleepiness:", self.sleepiness)
        print("Coins:", self.coins)

    def earn_coins(self):
        self.coins += 10