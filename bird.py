import pygame

from pygame.math import Vector2

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.gravity = Vector2(0, 10)
        self.pos = Vector2((144, 197))
        self.speed = Vector2(0, 0)
        self.image = pygame.image.load("assets/img/bird.png")
        self.rect = self.image.get_rect(center = self.pos)
        
    def jump(self):
        self.speed[1] = -3
    def fall(self):
        self.pos += self.speed
        self.rect.center = self.pos
        self.speed += self.gravity / 100
    
    def update(self):
        self.fall()
        