import pygame
import os
from settings import *

class Player():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction # 'up', 'down', 'left', 'right'
        self.speed = PLAYER_SPEED # pixels per frame
        self.sprites = {}
        sprites_path = 'graphics/player'
        for file in os.listdir(sprites_path): #This code assumes that the filenames contain the words 'up', 'down', 'left', and 'right'. It loads each sprite into a dictionary self.sprites where the keys are the directions and the values are the loaded images.
            if 'up' in file:
                self.sprites['up'] = pygame.image.load(os.path.join(sprites_path, file)).convert_alpha()
            elif 'down' in file:
                self.sprites['down'] = pygame.image.load(os.path.join(sprites_path, file)).convert_alpha()
            elif 'left' in file:
                self.sprites['left'] = pygame.image.load(os.path.join(sprites_path, file)).convert_alpha()
            elif 'right' in file:
                self.sprites['right'] = pygame.image.load(os.path.join(sprites_path, file)).convert_alpha()

    def get_coordinates(self):
        return (self.x, self.y)
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        self.speed = speed

    def get_sprite(self):
        return self.sprite
    
    def set_sprite(self, path):
        self.sprite = pygame.image.load(path).convert_alpha()

    def move_up(self):
        self.y -= self.speed
    
    def move_down(self):
        self.y += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed