import pygame

#Screen and video settings
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME
MAX_FPS = 60 #30
BACKGROUND_COLOR = (0,0,0)
BACKGROUND_ANIMATION_DELAY = 0.3

#def get_screen_width(): return SCREEN_WIDTH Tutta il gioco è progettato per andare a 720x480 ma sarebbe carino che se il giocatore volesse cambiare la risoluzione potesse farlo
#def get_screen_height(): return SCREEN_HEIGHT e che quindi tutto il gioco venisse scalato di conseguenza, ed eventualmente scalato una seconda volta se ridimensiona la finestra
def get_max_fps(): return MAX_FPS #Accetta però solamente dimensioni conosciute come 480p o 1080p

#def set_screen_width(width): global SCREEN_WIDTH; SCREEN_WIDTH = width
#def set_screen_height(height): global SCREEN_HEIGHT; SCREEN_HEIGHT = height
def set_max_fps(fps): global MAX_FPS; MAX_FPS = fps

#Camera keybinds
ZOOM_UP_KEY = pygame.K_q
ZOOM_DOWN_KEY = pygame.K_z

def get_zoom_up_keybind(): return ZOOM_UP_KEY
def get_zoom_down_keybind(): return ZOOM_DOWN_KEY

def set_zoom_up_keybind(key): global ZOOM_UP_KEY; ZOOM_UP_KEY = key
def set_zoom_down_keybind(key): global ZOOM_DOWN_KEY; ZOOM_DOWN_KEY = key

#Camera settings
ZOOM_SCALING_VELOCITY = 0.1
ZOOM_SCALE_LIMITS = (1, 2) 
INITIAL_ZOOM = 1.5
INTERNAL_SURFACE_SIZE = (2500,2500) #2500, 2500

#Player settings
PLAYER_SPEED = 3
PLAYER_ANIMATION_DELAY = 0.3 #Secondi tra i frame delle animazioni

#Keybinds
POKEDEX_KEY = pygame.K_p #Pulsante per aprire il PokèDex
PAUSE_KEY = pygame.K_ESCAPE #Pulsante per mettere in pausa il gioco ed uscire dal menu delle impostazioni
EXIT_KEY = pygame.K_n #Pulsante per uscire dal gioco
INTERACTION_KEY = pygame.K_e #Pulsante per interagire con gli oggetti e confermare durante la battaglia
MAP_KEY = pygame.K_m #Pulsante per aprire la mappa
INVENTORY_KEY = pygame.K_i #Pulsante per aprire l'inventario
SAVE_SETTINGS_KEY = pygame.K_s #Pulsante per salvare le impostazioni quando nel menù delle impostazioni
DISCARD_SETTINGS_KEY = pygame.K_d #Pulsante per scartare le impostazioni quando nel menù delle impostazioni
RESTORE_SETTINGS_KEY = pygame.K_r #Pulsante per ripristinare le impostazioni di default
MUTE_KEY = pygame.K_m #Pulsante per mutare il gioco (scorciatoia nel menu delle impostazioni)

def get_pokedex_keybind(): return POKEDEX_KEY
def get_pause_keybind(): return PAUSE_KEY
def get_exit_keybind(): return EXIT_KEY
def get_interaction_keybind(): return INTERACTION_KEY
def get_map_keybind(): return MAP_KEY
def get_inventory_keybind(): return INVENTORY_KEY

def set_pokedex_keybind(key): global POKEDEX_KEY; POKEDEX_KEY = key
def set_pause_keybind(key): global PAUSE_KEY; PAUSE_KEY = key
def set_exit_keybind(key): global EXIT_KEY; EXIT_KEY = key
def set_interaction_keybind(key): global INTERACTION_KEY; INTERACTION_KEY = key
def set_map_keybind(key): global MAP_KEY; MAP_KEY = key
def set_inventory_keybind(key): global INVENTORY_KEY; INVENTORY_KEY = key

#Keybinds for movement
FORWARD_KEY = pygame.K_w #Pulsante per muoversi in avanti
LEFT_KEY = pygame.K_a #Pulsante per muoversi a sinistra
BACKWARD_KEY = pygame.K_s #Pulsante per muoversi indietro
RIGHT_KEY = pygame.K_d #Pulsante per muoversi a destra

def get_forward_keybind(): return FORWARD_KEY
def get_left_keybind(): return LEFT_KEY
def get_backward_keybind(): return BACKWARD_KEY
def get_right_keybind(): return RIGHT_KEY

def set_forward_keybind(key): global FORWARD_KEY; FORWARD_KEY = key
def set_left_keybind(key): global LEFT_KEY; LEFT_KEY = key
def set_backward_keybind(key): global BACKWARD_KEY; BACKWARD_KEY = key
def set_right_keybind(key): global RIGHT_KEY; RIGHT_KEY = key

#Funzione di ripristino a valori di default
def set_default_configuration():
    #Global declarations
    global ZOOM_UP_KEY
    global ZOOM_DOWN_KEY
    global MAX_FPS
    global POKEDEX_KEY
    global PAUSE_KEY
    global EXIT_KEY
    global INTERACTION_KEY
    global MAP_KEY
    global INVENTORY_KEY
    global SAVE_SETTINGS_KEY
    global DISCARD_SETTINGS_KEY
    global FORWARD_KEY
    global LEFT_KEY
    global BACKWARD_KEY
    global RIGHT_KEY
    #Camera keybinds
    ZOOM_UP_KEY = pygame.K_q
    ZOOM_DOWN_KEY = pygame.K_z
    #Video settings
    MAX_FPS = 60 #30
    #Keybinds
    POKEDEX_KEY = pygame.K_p #Pulsante per aprire il PokèDex
    PAUSE_KEY = pygame.K_ESCAPE #Pulsante per mettere in pausa il gioco ed uscire dal menu delle impostazioni
    EXIT_KEY = pygame.K_n #Pulsante per uscire dal gioco
    INTERACTION_KEY = pygame.K_e #Pulsante per interagire con gli oggetti e confermare durante la battaglia
    MAP_KEY = pygame.K_m #Pulsante per aprire la mappa
    INVENTORY_KEY = pygame.K_i #Pulsante per aprire l'inventario
    SAVE_SETTINGS_KEY = pygame.K_s #Pulsante per salvare le impostazioni quando nel menù delle impostazioni
    DISCARD_SETTINGS_KEY = pygame.K_d #Pulsante per scartare le impostazioni quando nel menù delle impostazioni
    #Keybinds for movement
    FORWARD_KEY = pygame.K_w #To move forward
    LEFT_KEY = pygame.K_a #To move to the left
    BACKWARD_KEY = pygame.K_s #To move backwards
    RIGHT_KEY = pygame.K_d #To move to the right
#Funzione di salvataggio delle impostazioni
def save_configuration():
    with open("settings.txt", 'w') as f:
        f.write(f"ZOOM_UP_KEY = {ZOOM_UP_KEY}\n")
        f.write(f"ZOOM_DOWN_KEY = {ZOOM_DOWN_KEY}\n")
        f.write(f"MAX_FPS = {MAX_FPS}\n")
        f.write(f"POKEDEX_KEY = {POKEDEX_KEY}\n")
        f.write(f"PAUSE_KEY = {PAUSE_KEY}\n")
        f.write(f"EXIT_KEY = {EXIT_KEY}\n")
        f.write(f"INTERACTION_KEY = {INTERACTION_KEY}\n")
        f.write(f"MAP_KEY = {MAP_KEY}\n")
        f.write(f"INVENTORY_KEY = {INVENTORY_KEY}\n")
        f.write(f"FORWARD_KEY = {FORWARD_KEY}\n")
        f.write(f"LEFT_KEY = {LEFT_KEY}\n")
        f.write(f"BACKWARD_KEY = {BACKWARD_KEY}\n")
        f.write(f"RIGHT_KEY = {RIGHT_KEY}\n")
#Funzione di caricamento delle impostazioni
def load_configuration():
    with open("settings.txt", 'r') as f:
        global ZOOM_UP_KEY
        global ZOOM_DOWN_KEY
        global MAX_FPS
        global POKEDEX_KEY
        global PAUSE_KEY
        global EXIT_KEY
        global INTERACTION_KEY
        global MAP_KEY
        global INVENTORY_KEY
        global FORWARD_KEY
        global LEFT_KEY
        global BACKWARD_KEY
        global RIGHT_KEY

        for line in f:
            name, value = line.strip().split(' = ')
            if name == "ZOOM_UP_KEY": ZOOM_UP_KEY = int(value)
            elif name == "ZOOM_DOWN_KEY": ZOOM_DOWN_KEY = int(value)
            elif name == "MAX_FPS": MAX_FPS = int(value)
            elif name == "POKEDEX_KEY": POKEDEX_KEY = int(value)
            elif name == "PAUSE_KEY": PAUSE_KEY = int(value)
            elif name == "EXIT_KEY": EXIT_KEY = int(value)
            elif name == "INTERACTION_KEY": INTERACTION_KEY = int(value)
            elif name == "MAP_KEY": MAP_KEY = int(value)
            elif name == "INVENTORY_KEY": INVENTORY_KEY = int(value)
            elif name == "FORWARD_KEY": FORWARD_KEY = int(value)
            elif name == "LEFT_KEY": LEFT_KEY = int(value)
            elif name == "BACKWARD_KEY": BACKWARD_KEY = int(value)
            elif name == "RIGHT_KEY": RIGHT_KEY = int(value)