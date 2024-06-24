import pygame
import time
import settings #Bisogna importare così perchè from ... import * clona le variabili
from logic.collisionController import CollisionController

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, camera_group, keybinds):

        # Call the parent class (Sprite) constructor
        super().__init__(camera_group)
        self.camera_group = camera_group
        self.pos = pos
        self.collision_controller = CollisionController(camera_group)
        self.direction = pygame.math.Vector2()
        self.speed = settings.PLAYER_SPEED # pixels per frame
        self.relative_pos = self.camera_group.calculate_new_player_relative_coords()

        #Animation variables
        self.frame_switch_delay = settings.PLAYER_ANIMATION_DELAY
        self.last_frame_switch_time = time.time()

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

        self.keybinds = keybinds

    def change_frame(self):
        current_time = time.time()

        if current_time - self.last_frame_switch_time >= self.frame_switch_delay: 
            self.current_frame += 1
            if self.current_frame == len(self.current_animation): 
                self.current_frame = 1 #Se il giocatore continua a muoversi ciclo solamente fra i due frame di camminata
            
            self.image = self.current_animation[self.current_frame]
            self.last_frame_switch_time = current_time # Reset the last frame switch time

    def change_animation_verse(self, new_verse):

        if new_verse == "up" and self.verse != "up": #Le seconde condizioni booleane non sono necessarie ma potrebbero aumentare le prestazioni in alcuni casi perchè evitano una assegnazione inutile
            self.image = self.up_sprites[self.current_frame] #Per evitare che ci sia una momentanea differenza fra la direzione del movimento ed il verso che il giocatore sta guardando
            self.current_animation = self.up_sprites 
            self.verse = "up"

        elif new_verse == "down" and self.verse != "down":
            self.image = self.down_sprites[self.current_frame] #Per evitare che ci sia una momentanea differenza fra la direzione del movimento ed il verso che il giocatore sta guardando
            self.current_animation = self.down_sprites
            self.verse = "down"

        elif new_verse == "left" and self.verse != "left":
            self.image = self.left_sprites[self.current_frame] #Per evitare che ci sia una momentanea differenza fra la direzione del movimento ed il verso che il giocatore sta guardando
            self.current_animation = self.left_sprites
            self.verse = "left"

        elif new_verse == "right" and self.verse != "right":
            self.image = self.right_sprites[self.current_frame] #Per evitare che ci sia una momentanea differenza fra la direzione del movimento ed il verso che il giocatore sta guardando
            self.current_animation = self.right_sprites
            self.verse = "right"
            
    def input(self):
        
        keys = pygame.key.get_pressed() #Tupla di booleani contenente lo stato di tutti i tasti
        self.relative_pos = self.camera_group.calculate_new_player_relative_coords() #Calcola le coordinate relative del giocatore rispetto all'immagine della zona in cui si trova
        print(self.relative_pos)

        if (keys[settings.BACKWARD_KEY] and keys[settings.FORWARD_KEY]) or (keys[settings.LEFT_KEY] and keys[settings.RIGHT_KEY]): #Se vengono premuti
            self.direction.y = 0
            self.direction.x = 0

        elif keys[settings.FORWARD_KEY]:
            for speed in (settings.PLAYER_SPEED, 0, -1):
                if self.collision_controller.allow_movement((self.relative_pos.x - speed, self.relative_pos.y)):
                    self.change_animation_verse("up")
                    self.change_frame() #Cambia il frame del giocatore
                    self.direction.y = 1
                    self.direction.x = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    break

        elif keys[settings.BACKWARD_KEY]:
            for speed in (settings.PLAYER_SPEED, 0, -1):
                if self.collision_controller.allow_movement((self.relative_pos.x + speed, self.relative_pos.y)):
                    self.change_animation_verse("down")
                    self.change_frame() #Cambia il frame del giocatore
                    self.direction.y = -1
                    self.direction.x = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    break

        elif keys[settings.LEFT_KEY] and not keys[settings.FORWARD_KEY] and not keys[settings.BACKWARD_KEY]:  
            for speed in (settings.PLAYER_SPEED, 0, -1):
                if self.collision_controller.allow_movement((self.relative_pos.x, self.relative_pos.y - speed)):
                    self.change_animation_verse("left")
                    self.change_frame() #Cambia il frame del giocatore
                    self.direction.x = 1
                    self.direction.y = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    break

        elif keys[settings.RIGHT_KEY] and not keys[settings.FORWARD_KEY] and not keys[settings.BACKWARD_KEY]:    
            for speed in (settings.PLAYER_SPEED, 0, -1):
                if self.collision_controller.allow_movement((self.relative_pos.x, self.relative_pos.y + speed)):
                    self.change_animation_verse("right")
                    self.change_frame() #Cambia il frame del giocatore
                    self.direction.x = -1
                    self.direction.y = 0 #Per garantire che il giocatore non si possa muovere in diagonale
                    break
               
        else:
            self.direction.x = 0
            self.direction.y = 0

        if self.direction.x == 0 and self.direction.y == 0: #Se il giocatore non si sta muovendo disegno il frame che lo rappresenta come fermo
            #self.current_frame = 0 #Non necessario perchè se in movimento cicla fra frame 1 e 2 ma "teoricamente" corretto
            self.image = self.current_animation[0] 
            
    def move(self):
        self.input() #Gestisce l'input del giocatore
        self.rect.center += self.direction * self.speed