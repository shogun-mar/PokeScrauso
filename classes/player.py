import pygame
import os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):

        # Call the parent class (Sprite) constructor
        super().__init__(group)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED # pixels per frame
        self.image = pygame.image.load("graphics/player/player.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[BACKWARD_KEY] and keys[FORWARD_KEY]: #Se vengono premuti entrambi i tasti assieme non accade nessun movimento
            self.direction.y = 0
        elif keys[BACKWARD_KEY]:
            self.direction.y = -1
        elif keys[FORWARD_KEY]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[LEFT_KEY] and keys[RIGHT_KEY]: #Se vengono premuti entrambi i tasti assieme non accade nessun movimento
            self.direction.x = 0
        elif keys[LEFT_KEY]:
            self.direction.x = 1
        elif keys[RIGHT_KEY]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self):
        self.input()
        self.rect.center += self.direction * self.speed