import pygame

class YarnBall(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed