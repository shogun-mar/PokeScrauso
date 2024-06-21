import pygame

#Screen and video settings
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE
MAX_FPS = 60 #30
BACKGROUND_COLOR = (0,0,0)

#def get_screen_width(): return SCREEN_WIDTH Tutta il gioco è progettato per andare a 720x480 ma sarebbe carino che se il giocatore volesse cambiare la risoluzione potesse farlo
#def get_screen_height(): return SCREEN_HEIGHT e che quindi tutto il gioco venisse scalato di conseguenza, ed eventualmente scalato una seconda volta se ridimensiona la finestra
def get_max_fps(): return MAX_FPS #Accetta però solamente dimensioni conosciute come 480p o 1080p

#def set_screen_width(width): global SCREEN_WIDTH; SCREEN_WIDTH = width
#def set_screen_height(height): global SCREEN_HEIGHT; SCREEN_HEIGHT = height
def set_max_fps(fps): global MAX_FPS; MAX_FPS = fps

#Camera settings
ZOOM_SCALING_VELOCITY = 0.1
ZOOM_SCALE_LIMITS = (1, 2) 
INITIAL_ZOOM = 1.5
INTERNAL_SURFACE_SIZE = (2500,2500) #2500, 2500

#Player settings
PLAYER_SPEED = 3
PLAYER_ANIMATION_DELAY = 0.3 #Secondi tra i frame delle animazioni

#Keybinds

global FORWARD_KEY, LEFT_KEY
global BACKWARD_KEY, RIGHT_KEY
global FULLSCREEN_KEY, POKEDEX_KEY
global EXIT_KEY, INTERACTION_KEY
global MAP_KEY, INVENTORY_KEY
global HELP_KEY, ZOOM_IN_KEY
global ZOOM_OUT_KEY

POKEDEX_KEY = pygame.K_p #Pulsante per aprire il PokèDex
PAUSE_KEY = pygame.K_ESCAPE #Pulsante per mettere in pausa il gioco ed uscire dal menu delle impostazioni
EXIT_KEY = pygame.K_n #Pulsante per uscire dal gioco
INTERACTION_KEY = pygame.K_e #Pulsante per interagire con gli oggetti e confermare durante la battaglia
MAP_KEY = pygame.K_m #Pulsante per aprire la mappa
INVENTORY_KEY = pygame.K_i #Pulsante per aprire l'inventario
MUTE_KEY = pygame.K_m #Pulsante per mutare il gioco (scorciatoia nel menu delle impostazioni)
FULLSCREEN_KEY = pygame.K_f #Pulsante per mettere il gioco in fullscreen (scorciatoia nel menu delle impostazioni)
HELP_KEY = pygame.K_h #Pulsante per aprire il menu di aiuto
ACCEPTABLE_KEYBINDS = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_SPACE, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] #pygame.K_ESCAPE, pygame.K_BACKSPACE, pygame.K_TAB, pygame.K_CAPSLOCK, pygame.K_LSHIFT

def get_pokedex_keybind(): return POKEDEX_KEY
def get_pause_keybind(): return PAUSE_KEY
def get_exit_keybind(): return EXIT_KEY
def get_interaction_keybind(): return INTERACTION_KEY
def get_map_keybind(): return MAP_KEY
def get_inventory_keybind(): return INVENTORY_KEY
def get_fullscreen_keybind(): return FULLSCREEN_KEY
def get_help_keybind(): return HELP_KEY

def set_pokedex_keybind(key): global POKEDEX_KEY; POKEDEX_KEY = key
def set_pause_keybind(key): global PAUSE_KEY; PAUSE_KEY = key
def set_exit_keybind(key): global EXIT_KEY; EXIT_KEY = key
def set_interaction_keybind(key): global INTERACTION_KEY; INTERACTION_KEY = key
def set_map_keybind(key): global MAP_KEY; MAP_KEY = key
def set_inventory_keybind(key): global INVENTORY_KEY; INVENTORY_KEY = key
def set_fullscreen_keybind(key): global FULLSCREEN_KEY; FULLSCREEN_KEY = key
def set_help_keybind(key): global HELP_KEY; HELP_KEY = key

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

#Camera keybinds
ZOOM_OUT_KEY = pygame.K_q
ZOOM_IN_KEY = pygame.K_z

def get_zoom_out_keybind(): return ZOOM_OUT_KEY
def get_zoom_in_keybind(): return ZOOM_IN_KEY

def set_zoom_out_keybind(key): global ZOOM_OUT_KEY; ZOOM_OUT_KEY = key
def set_zoom_in_keybind(key): global ZOOM_IN_KEY; ZOOM_IN_KEY = key

#Funzione di ripristino a valori di default
def set_default_configuration():
    # Default configuration settings
    default_config = {
        "FORWARD_KEY": pygame.K_w,
        "LEFT_KEY": pygame.K_a,
        "BACKWARD_KEY": pygame.K_s,
        "RIGHT_KEY": pygame.K_d,
        "FULLSCREEN_KEY": pygame.K_f,
        "POKEDEX_KEY": pygame.K_p,
        "EXIT_KEY": pygame.K_n,
        "INTERACTION_KEY": pygame.K_e,
        "MAP_KEY": pygame.K_m,
        "INVENTORY_KEY": pygame.K_i,
        "HELP_KEY": pygame.K_h,
        "ZOOM_IN_KEY": pygame.K_z,
        "ZOOM_OUT_KEY": pygame.K_q
    }
    
    return default_config
#Funzione di salvataggio delle impostazioni
def save_configuration_to_file():
    with open("settings.txt", 'w') as f:
        f.write(f"FORWARD_KEY = {FORWARD_KEY}\n")
        f.write(f"LEFT_KEY = {LEFT_KEY}\n")
        f.write(f"BACKWARD_KEY = {BACKWARD_KEY}\n")
        f.write(f"RIGHT_KEY = {RIGHT_KEY}\n")
        f.write(f"FULLSCREEN_KEY = {FULLSCREEN_KEY}\n")
        f.write(f"POKEDEX_KEY = {POKEDEX_KEY}\n")
        f.write(f"EXIT_KEY = {EXIT_KEY}\n")
        f.write(f"INTERACTION_KEY = {INTERACTION_KEY}\n")
        f.write(f"MAP_KEY = {MAP_KEY}\n")
        f.write(f"INVENTORY_KEY = {INVENTORY_KEY}\n")
        f.write(f"HELP_KEY = {HELP_KEY}\n")
        f.write(f"ZOOM_IN_KEY = {ZOOM_IN_KEY}\n")
        f.write(f"ZOOM_OUT_KEY = {ZOOM_OUT_KEY}\n")        

def save_configuration(new_configuration):
    global FORWARD_KEY, LEFT_KEY
    global BACKWARD_KEY, RIGHT_KEY
    global FULLSCREEN_KEY, POKEDEX_KEY
    global EXIT_KEY, INTERACTION_KEY
    global MAP_KEY, INVENTORY_KEY
    global HELP_KEY, ZOOM_IN_KEY
    global ZOOM_OUT_KEY

    FORWARD_KEY = new_configuration["FORWARD_KEY"]
    LEFT_KEY = new_configuration["LEFT_KEY"]
    BACKWARD_KEY = new_configuration["BACKWARD_KEY"]
    RIGHT_KEY = new_configuration["RIGHT_KEY"]
    FULLSCREEN_KEY = new_configuration["FULLSCREEN_KEY"]
    POKEDEX_KEY = new_configuration["POKEDEX_KEY"]
    EXIT_KEY = new_configuration["EXIT_KEY"]
    INTERACTION_KEY = new_configuration["INTERACTION_KEY"]
    MAP_KEY = new_configuration["MAP_KEY"]
    INVENTORY_KEY = new_configuration["INVENTORY_KEY"]
    HELP_KEY = new_configuration["HELP_KEY"]
    ZOOM_IN_KEY = new_configuration["ZOOM_IN_KEY"]
    ZOOM_OUT_KEY = new_configuration["ZOOM_OUT_KEY"]

    save_configuration_to_file()

#Funzione di caricamento delle impostazioni
def load_configuration():
    with open("settings.txt", 'r') as f:
        global FORWARD_KEY, LEFT_KEY
        global BACKWARD_KEY, RIGHT_KEY
        global FULLSCREEN_KEY, POKEDEX_KEY
        global EXIT_KEY, INTERACTION_KEY
        global MAP_KEY, INVENTORY_KEY
        global HELP_KEY, ZOOM_IN_KEY
        global ZOOM_OUT_KEY

        for line in f:
            name, value = line.strip().split(' = ')
            if name == "FORWARD_KEY": FORWARD_KEY = int(value)
            elif name == "LEFT_KEY": LEFT_KEY = int(value)
            elif name == "BACKWARD_KEY": BACKWARD_KEY = int(value)
            elif name == "RIGHT_KEY": RIGHT_KEY = int(value)
            elif name == "FULLSCREEN_KEY": FULLSCREEN_KEY = int(value)
            elif name == "POKEDEX_KEY": POKEDEX_KEY = int(value)
            elif name == "EXIT_KEY": EXIT_KEY = int(value)
            elif name == "INTERACTION_KEY": INTERACTION_KEY = int(value)
            elif name == "MAP_KEY": MAP_KEY = int(value)
            elif name == "INVENTORY_KEY": INVENTORY_KEY = int(value)
            elif name == "HELP_KEY": HELP_KEY = int(value)
            elif name == "ZOOM_IN_KEY": ZOOM_IN_KEY = int(value)
            elif name == "ZOOM_OUT_KEY": ZOOM_OUT_KEY = int(value)
            

def get_current_configuration():
    return {
        "FORWARD_KEY": FORWARD_KEY, "LEFT_KEY": LEFT_KEY,
        "BACKWARD_KEY": BACKWARD_KEY, "RIGHT_KEY": RIGHT_KEY,
        "FULLSCREEN_KEY": FULLSCREEN_KEY, "POKEDEX_KEY": POKEDEX_KEY,
        "EXIT_KEY": EXIT_KEY, "INTERACTION_KEY": INTERACTION_KEY,
        "MAP_KEY": MAP_KEY, "INVENTORY_KEY": INVENTORY_KEY,
        "HELP_KEY": HELP_KEY, "ZOOM_IN_KEY": ZOOM_IN_KEY,
        "ZOOM_OUT_KEY": ZOOM_OUT_KEY
    }