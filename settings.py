import pygame

#Screen settings
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE
MAX_FPS = 30
BACKGROUND_COLOR = (0,0,0)

#Camera keybinds
ZOOM_UP_KEY = pygame.K_q
ZOOM_DOWN_KEY = pygame.K_z

#Camera settings
ZOOM_SCALING_VELOCITY = 0.1
ZOOM_SCALE_LIMITS = (1, 2) 
INITIAL_ZOOM = 1.5
INTERNAL_SURFACE_SIZE = (2500,2500)

#Animation settings
ANIMATION_DELAY = 0.3 #Secondi tra i frame delle animazioni

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