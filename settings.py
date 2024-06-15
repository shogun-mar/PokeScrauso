import pygame

#Screen settings
SCREEN_WIDTH = 728
SCREEN_HEIGHT = 455
flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE
MAX_FPS = 30

#Player settings
PLAYER_SPEED = 5

#Keybinds
POKEDEK_KEY = pygame.K_p #Pulsante per aprire il PokèDex
PAUSE_KEY = pygame.K_ESCAPE #Pulsante per uscire dal gioco
EXIT_KEY = pygame.K_n #Pulsante per uscire dal gioco
INTERACTION_KEY = pygame.K_e #Pulsante per interagire con gli oggetti e confermare durante la battaglia
MAP_KEY = pygame.K_m #Pulsante per aprire la mappa
INVENTORY_KEY = pygame.K_i #Pulsante per aprire l'inventario

#Keybinds for movement
FORWARD_KEY = pygame.K_w #Pulsante per muoversi in avanti
LEFT_KEY = pygame.K_a #Pulsante per muoversi a sinistra
BACKWARD_KEY = pygame.K_s #Pulsante per muoversi indietro
RIGHT_KEY = pygame.K_d #Pulsante per muoversi a destra