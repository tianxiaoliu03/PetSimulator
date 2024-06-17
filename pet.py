import pygame

class Pet:
    def __init__(self, name, image_path):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.sleepiness = 50
        self.thirstiness = 50
        self.coins = 0
        self.image_path = image_path
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))  # Adjust size as needed
        self.rect = self.image.get_rect(center=(375, 600))  # Center position

    def feed(self):
        if self.coins >= 5:
            self.hunger = max(self.hunger + 10, 0)
            self.coins -= 5
        else:
            print("Not enough coins to buy food.")

    def quench_thirst(self):
        if self.coins >= 5:
            self.thirstiness = max(self.thirstiness + 10, 0)
            self.coins -= 5
        else:
            print("Not enough coins to buy water.")

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

    def earn_coins(self):
        self.coins += 10