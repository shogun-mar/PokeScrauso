import pygame
import time
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):

        # Call the parent class (Sprite) constructor
        super().__init__(group)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED # pixels per frame

        #Animation variables
        self.frame_switch_delay = ANIMATION_DELAY
        self.last_frame_switch_time = time.time()

        #Tasti di movimento
        self.keys = {'BACKWARD_KEY': False, 'FORWARD_KEY': False, 'LEFT_KEY': False, 'RIGHT_KEY': False}

        #Player images
        self.down_frame1 = pygame.image.load("graphics/player/down_frame1.png").convert_alpha()
        self.down_frame2 = pygame.image.load("graphics/player/down_frame2.png").convert_alpha()
        self.down_frame3 = pygame.image.load("graphics/player/down_frame3.png").convert_alpha()
        self.down_sprites = [self.down_frame1, self.down_frame2, self.down_frame3]
        
        self.up_frame1 = pygame.image.load("graphics/player/up_frame1.png").convert_alpha()
        self.up_frame2 = pygame.image.load("graphics/player/up_frame2.png").convert_alpha()
        self.up_frame3 = pygame.image.load("graphics/player/up_frame3.png").convert_alpha()
        self.up_sprites = [self.up_frame1, self.up_frame2, self.up_frame3]

        self.left_frame1 = pygame.image.load("graphics/player/left_frame1.png").convert_alpha()
        self.left_frame2 = pygame.image.load("graphics/player/left_frame2.png").convert_alpha()
        self.left_frame3 = pygame.image.load("graphics/player/left_frame3.png").convert_alpha()
        self.left_sprites = [self.left_frame1, self.left_frame2, self.left_frame3]

        self.right_frame1 = pygame.image.load("graphics/player/right_frame1.png").convert_alpha()
        self.right_frame2 = pygame.image.load("graphics/player/right_frame2.png").convert_alpha()
        self.right_frame3 = pygame.image.load("graphics/player/right_frame3.png").convert_alpha()
        self.right_sprites = [self.right_frame1, self.right_frame2, self.right_frame3]

        self.current_frame = 0
        self.current_animation = self.down_sprites
        self.image = self.current_animation[self.current_frame]
        self.rect = self.image.get_rect(center = pos)

        #Change the image of the player depending on the direction of movement
        self.verse = "down" # "up", "down", "left", "right" 

        #Collections of items
        self.inventory = {}
        self.pokedex = {}
        self.squad = []
        self.medals = []

    def change_frame(self):
        current_time = time.time()

        if current_time - self.last_frame_switch_time >= self.frame_switch_delay: 
            self.current_frame += 1
            if self.current_frame == len(self.current_animation) and self.is_player_moving():
                self.current_frame = 1 #Se l'animazione è finita ma il giocatore si sta ancora muovendo torno al secondo frame e non a quello iniziale che rappresenta il personaggio da fermo
            elif self.current_frame == len(self.current_animation):
                self.current_frame = 0 #Se il giocatore si ferma torno al frame iniziale
            
            self.image = self.current_animation[self.current_frame]
            self.last_frame_switch_time = current_time # Reset the last frame switch time

    def change_animation_verse(self, new_verse):

        if new_verse == "up" and self.verse != "up": #Le seconde condizioni booleane non sono necessarie ma potrebbero aumentare le prestazioni
            self.current_animation = self.up_sprites #in alcuni casi perchè evitano una assegnazione inutile
            self.verse = "up"
        elif new_verse == "down" and self.verse != "down":
            self.current_animation = self.down_sprites
            self.verse = "down"
        elif new_verse == "left" and self.verse != "left":
            self.current_animation = self.left_sprites
            self.verse = "left"
        elif new_verse == "right" and self.verse != "right":
            self.current_animation = self.right_sprites
            self.verse = "right"
            
    def is_player_moving(self):
        if self.keys[BACKWARD_KEY] or self.keys[FORWARD_KEY] or self.keys[LEFT_KEY] or self.keys[RIGHT_KEY]:
            return True
        return False
    
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if (self.keys[BACKWARD_KEY] and self.keys[FORWARD_KEY]) or (self.keys[LEFT_KEY] and self.keys[RIGHT_KEY]): #Se vengono premuti entrambi i tasti assieme non accade nessun movimento
                    self.direction.y = 0
                    self.direction.x = 0
                elif event.key == BACKWARD_KEY:
                    self.direction.y = -1
                    self.direction.x = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    self.change_frame() #Cambia il frame del giocatore
                    self.change_animation_verse("down")
                elif event.key == FORWARD_KEY:
                    self.direction.y = 1
                    self.direction.x = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    self.change_frame() #Cambia il frame del giocatore
                    self.change_animation_verse("up")
                elif event.key == LEFT_KEY:
                    self.direction.x = 1
                    self.direction.y = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    self.change_frame() #Cambia il frame del giocatore
                    self.change_animation_verse("left")
                elif event.key == RIGHT_KEY:
                    self.direction.x = -1
                    self.direction.y = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    self.change_frame() #Cambia il frame del giocatore
                    self.change_animation_verse("right")
                else:
                    self.direction.x = 0
                    self.direction.y = 0

    def move(self):
        self.input() #Gestisce l'input del giocatore
        self.rect.center += self.direction * self.speed