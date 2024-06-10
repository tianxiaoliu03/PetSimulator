import pygame
import random

class Coin:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)