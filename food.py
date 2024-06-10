import pygame

class Food:
    def __init__(self):
        self.image = pygame.image.load("food.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(10, 540))