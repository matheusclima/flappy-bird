import pygame

from pygame.math import Vector2

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.gravity = Vector2(0, 10)
        self.pos = Vector2((100, 197))
        self.speed = Vector2(0, 0)
        self.index = 0
        self.animation = []
        for i in range(3):
            img = pygame.image.load(f'assets/img/bird{i}.png').convert_alpha()
            self.animation.append(img)
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect(center = self.pos)
        
    def jump(self):
        self.speed[1] = -3
        
    def fall(self):
        self.pos += self.speed
        self.rect.center = self.pos
        self.speed += self.gravity / 100

    def rotate(self):
        rotated_image = pygame.transform.rotate(self.image, -5*self.speed[1])
        self.image = rotated_image
        self.rect = self.image.get_rect(center = self.pos)

    def animate(self):
        self.index += 0.2
        if self.index > len(self.animation) - 1: self.index = 0 
        self.image = self.animation[int(self.index)]

    def update(self):
        self.fall()
        self.animate()
        self.rotate()
        