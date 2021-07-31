import pygame

from pygame.math import Vector2

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.acceleration = [0, 0]
        self.pos = Vector2((30, 20))
        self.speed = Vector2(self.acceleration[0], self.acceleration[1])
        self.image = pygame.image.load("assets/img/bird.png")
        self.rect = self.image.get_rect(center = self.pos)
        
    def jump(self):
        self.acceleration[1] = -80

    def fall(self):
        self.pos += self.speed
        self.rect.center = self.pos
        self.speed = Vector2(self.acceleration[0], self.acceleration[1]/20)
        self.acceleration[1] += 3
    
    def update(self):
        self.fall()
        