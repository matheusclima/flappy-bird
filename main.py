import sys, pygame, time
from bird import Bird
from pipe import Pipe, Pipes, Obstacles
from input import InputHandler
from collision_detector import CollisionDetector

pygame.init()

running = True

size = width, height = 288, 512
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# bird_sprite = pygame.image.load("assets/img/bird.png")
bird = Bird()
# birdrect = bird.birdrect
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
for pipes in obstacles.pipes:
    group.add(pipes.top_pipe)
    group.add(pipes.bottom_pipe)
# print(background.get_width())
while running:

    input.handle()
    # bird.fall()
    bg_pos = [bg_pos[0]-1.4, bg_pos[1]-1.4]
    if bg_pos[0] < background.get_width() * -1:
        bg_pos[0] = background.get_width()
    
    if bg_pos[1] < background.get_width() * -1:
        bg_pos[1] = background.get_width()

    top_pipe_obstacles = [pipes.top_pipe for pipes in obstacles.pipes]
    bottom_pipe_obstacles = [pipes.bottom_pipe for pipes in obstacles.pipes]
    collisions = [floor_rect, *top_pipe_obstacles, *bottom_pipe_obstacles]

    if collision_detector.detect(bird.rect, *collisions):
        print('MORRI------------------')
        bird = Bird()
        obstacles = Obstacles()
        group = pygame.sprite.Group()
        group.add(bird)
        for pipes in obstacles.pipes:
            group.add(pipes.top_pipe)
            group.add(pipes.bottom_pipe)
        input = InputHandler(pygame, bird)
        continue
    

    screen.blit(background, (bg_pos[0], 0))
    screen.blit(background, (bg_pos[1], 0))
    screen.blit(floor, floor_rect)
    group.draw(screen)
    group.update()
    # obstacles.update_points(bird.pos[0])
    obstacles.update_group(bird.pos[0], group)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)