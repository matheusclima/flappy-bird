import pygame, sys

class InputHandler:

    def __init__(self, game, bird):
        self.bird = bird
        

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()