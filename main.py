import sys, pygame, time
from bird import Bird
from pipe import Pipe, Pipes, Obstacles
from input import InputHandler
from collision_detector import CollisionDetector

pygame.init()

running = True

size = width, height = 288, 512

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bird = Bird()
background = pygame.image.load("assets/img/background.png")
bg_pos = [0, background.get_width()]
floor = pygame.image.load("assets/img/fg.png")
floor_rect = floor.get_rect()
floor_rect.topleft = (0, height - floor_rect.height)

input = InputHandler(pygame, bird)
collision_detector = CollisionDetector()

obstacles = Obstacles()

group = pygame.sprite.Group()
group.add(bird)
group.add(obstacles.all_pipes)
while running:

    input.handle()
    bg_pos = [bg_pos[0]-1.4, bg_pos[1]-1.4]
    if bg_pos[0] < background.get_width() * -1:
        bg_pos[0] = background.get_width()
    
    if bg_pos[1] < background.get_width() * -1:
        bg_pos[1] = background.get_width()

    collisions = [floor_rect, *obstacles.all_pipes]

    if collision_detector.detect(bird.rect, *collisions):
        bird = Bird()
        obstacles = Obstacles()
        group = pygame.sprite.Group()
        group.add(bird)
        group.add(obstacles.all_pipes)
        input = InputHandler(pygame, bird)
        continue

    screen.blit(background, (bg_pos[0], 0))
    screen.blit(background, (bg_pos[1], 0))
    group.draw(screen)
    group.update()
    obstacles.update_group(bird.pos[0], group)
    screen.blit(floor, floor_rect)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)