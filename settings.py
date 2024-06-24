import pygame

#Screen and video settings
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED
MAX_FPS = 30 #60
BACKGROUND_COLOR = (0,0,0)

#def get_screen_width(): return SCREEN_WIDTH Tutta il gioco è progettato per andare a 720x480 ma sarebbe carino che se il giocatore volesse cambiare la risoluzione potesse farlo
#def get_screen_height(): return SCREEN_HEIGHT e che quindi tutto il gioco venisse scalato di conseguenza, ed eventualmente scalato una seconda volta se ridimensiona la finestra

#def set_screen_width(width): global SCREEN_WIDTH; SCREEN_WIDTH = width
#def set_screen_height(height): global SCREEN_HEIGHT; SCREEN_HEIGHT = height

#Camera settings
ZOOM_SCALING_VELOCITY = 0.1
ZOOM_SCALE_LIMITS = (0.1, 1.50) #0.75, 1.50
INITIAL_ZOOM = 1.0
INTERNAL_SURFACE_SIZE = (1920,1080) #2500, 2500

#Player settings
PLAYER_SPEED = 10
PLAYER_ANIMATION_DELAY = 0.3 #Secondi tra i frame delle animazioni

#Keybinds
POKEDEX_KEY = pygame.K_p #Pulsante per aprire il PokèDex
PAUSE_KEY = pygame.K_ESCAPE #Pulsante per mettere in pausa il gioco ed uscire dal menu delle impostazioni
EXIT_KEY = pygame.K_n #Pulsante per uscire dal gioco
INTERACTION_KEY = pygame.K_e #Pulsante per interagire con gli oggetti e confermare durante la battaglia
MAP_KEY = pygame.K_m #Pulsante per aprire la mappa
INVENTORY_KEY = pygame.K_i #Pulsante per aprire l'inventario
MUTE_KEY = pygame.K_m #Pulsante per mutare il gioco (scorciatoia nel menu delle impostazioni)
FULLSCREEN_KEY = pygame.K_f #Pulsante per mettere il gioco in fullscreen (scorciatoia nel menu delle impostazioni)
HELP_KEY = pygame.K_h #Pulsante per aprire il menu di aiuto
SCREENSHOT_KEY = pygame.K_F12 #Pulsante per fare uno screenshot
CANCEL_KEY = pygame.K_l #Pulsante per annullare un'azione
ACCEPTABLE_KEYBINDS = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, 
                       pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, 
                       pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_0, 
                       pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, 
                       pygame.K_SPACE, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_ESCAPE, pygame.K_BACKSPACE,
                       pygame.K_TAB, pygame.K_CAPSLOCK, pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_LCTRL, pygame.K_RCTRL, pygame.K_LALT,
                       pygame.K_RALT]

#Keybinds for movement
FORWARD_KEY = pygame.K_w #Pulsante per muoversi in avanti
LEFT_KEY = pygame.K_a #Pulsante per muoversi a sinistra
BACKWARD_KEY = pygame.K_s #Pulsante per muoversi indietro
RIGHT_KEY = pygame.K_d #Pulsante per muoversi a destra

#Camera keybinds
ZOOM_OUT_KEY = pygame.K_q
ZOOM_IN_KEY = pygame.K_z

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
        "PAUSE_KEY": pygame.K_ESCAPE,
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
        f.write(f"PAUSE_KEY = {PAUSE_KEY}\n")
        f.write(f"ZOOM_IN_KEY = {ZOOM_IN_KEY}\n")
        f.write(f"ZOOM_OUT_KEY = {ZOOM_OUT_KEY}\n")        

def save_configuration(new_configuration):
    global FORWARD_KEY, LEFT_KEY, \
           BACKWARD_KEY, RIGHT_KEY, \
           FULLSCREEN_KEY, POKEDEX_KEY, \
           EXIT_KEY, INTERACTION_KEY, \
           MAP_KEY, INVENTORY_KEY, \
           HELP_KEY, PAUSE_KEY, \
           ZOOM_IN_KEY, ZOOM_OUT_KEY

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
    PAUSE_KEY = new_configuration["PAUSE_KEY"]
    ZOOM_IN_KEY = new_configuration["ZOOM_IN_KEY"]
    ZOOM_OUT_KEY = new_configuration["ZOOM_OUT_KEY"]

    save_configuration_to_file()

#Funzione di caricamento delle impostazioni
def load_configuration():
    global FORWARD_KEY, LEFT_KEY, \
           BACKWARD_KEY, RIGHT_KEY, \
           FULLSCREEN_KEY, POKEDEX_KEY, \
           EXIT_KEY, INTERACTION_KEY, \
           MAP_KEY, INVENTORY_KEY, \
           HELP_KEY, PAUSE_KEY, \
           ZOOM_IN_KEY, ZOOM_OUT_KEY

    keybinds = {}
    with open("settings.txt", 'r') as f:
        for line in f:
            name, value = line.strip().split(' = ')
            value = int(value)  # Convert value to integer

            # Update the global variables and the dictionary simultaneously
            if name == "FORWARD_KEY":
                FORWARD_KEY = keybinds[name] = value
            elif name == "LEFT_KEY":
                LEFT_KEY = keybinds[name] = value
            elif name == "BACKWARD_KEY":
                BACKWARD_KEY = keybinds[name] = value
            elif name == "RIGHT_KEY":
                RIGHT_KEY = keybinds[name] = value
            elif name == "FULLSCREEN_KEY":
                FULLSCREEN_KEY = keybinds[name] = value
            elif name == "POKEDEX_KEY":
                POKEDEX_KEY = keybinds[name] = value
            elif name == "EXIT_KEY":
                EXIT_KEY = keybinds[name] = value
            elif name == "INTERACTION_KEY":
                INTERACTION_KEY = keybinds[name] = value
            elif name == "MAP_KEY":
                MAP_KEY = keybinds[name] = value
            elif name == "INVENTORY_KEY":
                INVENTORY_KEY = keybinds[name] = value
            elif name == "HELP_KEY":
                HELP_KEY = keybinds[name] = value
            elif name == "PAUSE_KEY":
                PAUSE_KEY = keybinds[name] = value
            elif name == "ZOOM_IN_KEY":
                ZOOM_IN_KEY = keybinds[name] = value
            elif name == "ZOOM_OUT_KEY":
                ZOOM_OUT_KEY = keybinds[name] = value

    return keybinds       
    
def print_configuration():
    print("FORWARD_KEY:", pygame.key.name(FORWARD_KEY))
    print("LEFT_KEY:", pygame.key.name(LEFT_KEY))
    print("BACKWARD_KEY:", pygame.key.name(BACKWARD_KEY))
    print("RIGHT_KEY:", pygame.key.name(RIGHT_KEY))
    print("FULLSCREEN_KEY:", pygame.key.name(FULLSCREEN_KEY))
    print("POKEDEX_KEY:", pygame.key.name(POKEDEX_KEY))
    print("EXIT_KEY:", pygame.key.name(EXIT_KEY))
    print("INTERACTION_KEY:", pygame.key.name(INTERACTION_KEY))
    print("MAP_KEY:", pygame.key.name(MAP_KEY))
    print("INVENTORY_KEY:", pygame.key.name(INVENTORY_KEY))
    print("HELP_KEY:", pygame.key.name(HELP_KEY))
    print("PAUSE_KEY:", pygame.key.name(PAUSE_KEY))
    print("ZOOM_IN_KEY:", pygame.key.name(ZOOM_IN_KEY))
    print("ZOOM_OUT_KEY:", pygame.key.name(ZOOM_OUT_KEY))
          
def get_current_configuration():
    return {
        "FORWARD_KEY": FORWARD_KEY, "LEFT_KEY": LEFT_KEY,
        "BACKWARD_KEY": BACKWARD_KEY, "RIGHT_KEY": RIGHT_KEY,
        "FULLSCREEN_KEY": FULLSCREEN_KEY, "POKEDEX_KEY": POKEDEX_KEY,
        "EXIT_KEY": EXIT_KEY, "INTERACTION_KEY": INTERACTION_KEY,
        "MAP_KEY": MAP_KEY, "INVENTORY_KEY": INVENTORY_KEY,
        "HELP_KEY": HELP_KEY, "PAUSE_KEY": PAUSE_KEY,
        "ZOOM_IN_KEY": ZOOM_IN_KEY,
        "ZOOM_OUT_KEY": ZOOM_OUT_KEY
    }