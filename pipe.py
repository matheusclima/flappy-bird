import pygame

from random import randint

from pygame.math import Vector2

class Obstacles:
    STEP = 200
    HEIGHT_RANGE = (100, 350)
    GAP = 220
    LIST_LENGTH = 3
    CURRENT_PIPE = 0
    
    pipes = []

    def __init__(self):
        self.CURRENT_PIPE = 0
        self.pipes = []
        for i in range(self.LIST_LENGTH):
            pos_x = (i+1)*self.STEP
            pos_y = randint(*self.HEIGHT_RANGE)
            self.pipes.append(Pipes([pos_x, pos_y], self.GAP))

    def update_group(self, current_x, group):
        middle_pipe = self.pipes[int(self.LIST_LENGTH/2)]
        middle_pipe_x = middle_pipe.pos_x
        if current_x > middle_pipe_x:
            pos_x = self.pipes[-1].pos_x + self.STEP
            pos_y = randint(*self.HEIGHT_RANGE)
            removed_pipes = self.pipes.pop(0)

            new_pipes = Pipes([pos_x, pos_y], self.GAP)
            self.pipes.append(new_pipes)

            group.remove(removed_pipes.top_pipe, removed_pipes.bottom_pipe)
            group.add(new_pipes.top_pipe, new_pipes.bottom_pipe)

    def update_points(self, current_x):
        current_pipe = self.pipes[self.CURRENT_PIPE]
        if current_x > current_pipe.pos_x:
            print('PONTOSSSS')
            if self.CURRENT_PIPE < int(self.LIST_LENGTH/2):
                self.CURRENT_PIPE += 1


    @property
    def last_pipes(self):
        return self.pipes[-1]



class Pipes:
    def __init__(self, pos, gap):
        # print(pos)
        self.pos = pos
        top_pipe_pos = [pos[0], pos[1] - gap]
        bottom_pipe_pos = [pos[0], pos[1] + gap]

        self.top_pipe = Pipe(top=True, pos=top_pipe_pos)
        self.bottom_pipe = Pipe(top=False, pos=bottom_pipe_pos)

    @property
    def pos_x(self):
        return self.top_pipe.pos[0]

    @property
    def pos_y(self):
        return self.top_pipe.pos[1]


class Pipe(pygame.sprite.Sprite):

    def __init__(self, top, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2((pos[0], pos[1]))

        self.image = pygame.image.load("assets/img/pipeUp.png") if top else pygame.image.load("assets/img/pipeDown.png")
        self.rect = self.image.get_rect()
        if top:
            self.rect.bottom = pos[1]
        else:
            self.rect.top = pos[1]

    def move(self):
        vel = Vector2((-1, 0))
        # print(self.pos)
        self.pos += vel
        self.rect.center = self.pos
    
    def update(self):
        self.move()
        