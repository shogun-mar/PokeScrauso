import pygame
import time
import settings #Bisogna importare così perchè from ... import * clona le variabili
from random import randint
from os import listdir, environ, path
from ctypes import windll
from logic.player import Player
from logic.gameState import GameState
from logic.cameraGroup import CameraGroup
from logic.states.gameplayState import *
from logic.states.helpMenuState import *
from logic.states.pokedexState import *
from logic.states.inventoryMenuState import *
from logic.states.mapState import *
from logic.states.pauseState import *
from logic.states.settingsMenuState import *
from logic.states.startMenuState import *
from logic.states.nameMenuState import *

class Game:
    def __init__(self):

        #Inizializzazione di Pygame e impostazione dello schermo
        environ['SDL_VIDEO_CENTERED'] = '1' #Center the Pygame window Comando di SDL per centrare la finestra
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), settings.flags, vsync=1)
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PokèScrauso")
        pygame.display.set_icon(pygame.image.load("graphics/menus/logo_small.png"))
        # Allow only specific events
        pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEWHEEL, pygame.QUIT, pygame.KEYDOWN, pygame.VIDEORESIZE])
        # Get physical resolution
        self.hw_screen_width, self.hw_screen_height  = self.get_hw_resolution()
        
        #Variabili di gioco
        self.half_w = settings.SCREEN_WIDTH // 2 #Metà della larghezza dello schermo
        self.half_h = settings.SCREEN_HEIGHT // 2
        self.current_volume_status = True #Stato attuale del volume (True = ON, False = OFF)
        self.game_state = GameState.GAMEPLAY #Stato di gioco iniziale
        #Font
        menu_font = pygame.font.Font("graphics/menus/fonts/standard_font.ttf", 10)
        self.naming_menu_font = pygame.font.Font("graphics/menus/fonts/standard_font.ttf", 20)

        #Colors
        self.naming_menu_color = (0,0,0)

        #Frame oscurato per il menu di pausa e di aiuto
        self.darkened_surface = None #Vuoto in modo che venga inizializzato solo quando serve

        #Pointer images
        self.pointer_image = pygame.image.load("graphics/menus/pointers/pointer.png").convert_alpha()
        self.pointer_image_rect = self.pointer_image.get_rect(center = (0,0))
        self.pointer_click_image = pygame.image.load("graphics/menus/pointers/pointer_click.png").convert_alpha()
        self.pointer_click_image_rect = self.pointer_click_image.get_rect(center = (0,0))
        self.current_pointer = self.pointer_image #Disegno sempre questa variabile ma cambio il suo valore in base alla posizione del mouse
        self.current_pointer_rect = self.pointer_image_rect
        pygame.mouse.set_visible(False) #Nasconde il cursore del mouse (sulla sua posizione verranno però disegnate le immagini dei puntatori personalizzati)   

        #Start menu
        randomint = randint(1,6)
        self.start_background_images = self.import_frames("graphics/menus/start menu/start_menu_background"+str(randomint))
        self.start_menu_current_frame = 0
        if randomint == 1: self.background_frame_switch_delay = 0.16 #Il delay fra i frame cambia in base allo sfondo
        elif randomint == 2 or randomint == 3: self.background_frame_switch_delay = 0.06
        elif randomint == 4: self.background_frame_switch_delay = 0.1
        elif randomint == 5: self.background_frame_switch_delay = 0.2
        elif randomint == 6: self.background_frame_switch_delay = 0.25
        self.background_last_switch_time = time.time()
        self.start_background_image = self.start_background_images[self.start_menu_current_frame]
        self.start_text_image = pygame.image.load("graphics/menus/start menu/start_menu_text.png").convert_alpha()
        self.start_text_image_rect = self.start_text_image.get_rect(center = (self.half_w, self.half_h - 100))
        self.new_game_button = pygame.image.load("graphics/menus/start menu/start_menu_new_game_text.png").convert_alpha()
        self.new_game_button_rect = self.new_game_button.get_rect(center = (self.half_w, self.half_h + 50))
        self.load_save_button = pygame.image.load("graphics/menus/start menu/start_menu_load_save_text.png").convert_alpha()
        self.load_save_button_rect = self.load_save_button.get_rect(center = (self.half_w, self.half_h + 150))
        self.settings_button = pygame.image.load("graphics/menus/start menu/settings_icon.png").convert_alpha()
        self.settings_button_rect = self.settings_button.get_rect(center = (settings.SCREEN_WIDTH - 40, settings.SCREEN_HEIGHT - 40))

        #Settings menu
        self.settings_background_image = pygame.image.load("graphics/menus/settings menu/settings_background" + str(randint(1,2)) + ".png").convert_alpha()
        self.save_button = pygame.image.load("graphics/menus/settings menu/save_button.png").convert_alpha()
        self.save_button_rect = self.save_button.get_rect(center = (self.half_w + 16, settings.SCREEN_HEIGHT - 50 ))
        self.restore_button = pygame.image.load("graphics/menus/settings menu/restore_button.png").convert_alpha()
        self.restore_button_rect = self.restore_button.get_rect(center = (self.half_w - 16, settings.SCREEN_HEIGHT - 50))
        self.discard_button = pygame.image.load("graphics/menus/settings menu/discard_button.png").convert_alpha()
        self.discard_button_rect = self.discard_button.get_rect(center = (self.half_w - 48, settings.SCREEN_HEIGHT - 50))
        self.mute_button = pygame.image.load("graphics/menus/settings menu/mute_button.png").convert_alpha()
        self.mute_button_rect = self.mute_button.get_rect(center = (self.half_w + 48, settings.SCREEN_HEIGHT - 50))
        self.unmute_button = pygame.image.load("graphics/menus/settings menu/unmute_button.png").convert_alpha()
        self.unmute_button_rect = self.unmute_button.get_rect(center = (self.half_w + 48, settings.SCREEN_HEIGHT - 50))

        self.current_keybinds = settings.load_configuration() #Carica le impostazioni attuali
        self.modified_keybinds = self.current_keybinds.copy() #Verrà poi modificato quando l'utente cambia i tasti
        self.modified_keybinds_images = get_configuration_images(self.modified_keybinds) 
        self.modified_keybinds_images_values = list(self.modified_keybinds_images.values())

        self.key_images = self.import_sequence_images("graphics/menus/icons/keys")
        key_images_values = list(self.key_images.values())
        self.last_clicked_index = None #Indice dell'ultima immagine cliccata
        self.modifying_keybind = False #Variabile di stato per indicare se si sta modificando un tasto

        self.settings_menu_images_rects = get_settings_menu_rects(self, key_images_values)

        keybinds_text = [
            "Move forwards", "Move to the left", 
            "Move backwards", "Move to the right", 
            "Toggle fullscreen", "Open the Pokèdex",
            "Closes the game", "Interact with objects",
            "Open the map", "Open the inventory",
            "Open the help menu", #"Pause the game",
            "Zoom in", "Zoom out"
        
            #Text field for max fps
            #Dropdown della risoluzione?
            #Salvataggio rapido
            #Caricamento rapido
        ]
        self.settings_menu_rendered_texts = render_texts(keybinds_text, menu_font, (0,0,0))
        self.settings_menu_rendered_texts_rects = get_settings_menu_texts_rects(self, self.settings_menu_rendered_texts)

        #Help menu
        self.help_keybinds_images_values = list(get_configuration_images(self.current_keybinds).values())
        self.help_menu_images_rects = self.settings_menu_images_rects #Le posizioni delle immagini sono le stesse di quelle del menu delle impostazioni
        self.help_menu_rendered_texts = render_texts(keybinds_text, menu_font, (255,255,255)) #I testi sono li stessi di quelli del menu delle impostazioni ma con un colore diverso
        self.help_menu_rendered_texts_rects = self.settings_menu_rendered_texts_rects #Le posizioni dei testi sono le stesse di quelle del menu delle impostazioni

        #Name menu
        self.name_menu_cursor = pygame.image.load("graphics/menus/naming menu/cursor.png").convert_alpha()
        self.name_menu_cursor_rect = self.name_menu_cursor.get_rect(center = (85, 235))
        self.name_menu_background = pygame.image.load("graphics/menus/naming menu/background.png").convert_alpha()
        self.name_menu_overlay_controls = pygame.image.load("graphics/menus/naming menu/overlay_controls.png").convert_alpha()
        self.name_menu_overlay_tab = pygame.image.load("graphics/menus/naming menu/overlay_tab_" + str(randint(1, 4)) + ".png").convert_alpha()
        self.simbols = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ':', ', ', ';', "'", '"', '!', '?', '(', ')', '+', '-', '*', '/', '=']
        ]
        self.rendered_name_menu_texts  = render_name_menu_texts(self.naming_menu_font, (0,0,0), self)
        self.rendered_name_menu_texts_rects = get_name_menu_texts_rects(self.rendered_name_menu_texts)
        self.simbols_set_index = 0 #Indice del set di simboli attualmente visualizzato
        self.player_name = "____________" # Iniziale nome del giocatore
        self.player_name_text = self.naming_menu_font.render(self.player_name, True,  self.naming_menu_color)

        #Map images
        self.map_image = pygame.image.load("graphics/menus/map menu/map.png").convert_alpha()
        self.map_rect = self.map_image.get_rect(center = self.screen.get_rect().center)
        #Overlay for map
        self.overlay = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.SRCALPHA) # Create a semi-transparent surface the same size as the screen

        #Objects initialization
        self.camera_group = CameraGroup(self.fake_screen) #Gruppo per gli oggetti che seguono la camera
        self.player = Player((0, 200), self.camera_group, self.current_keybinds)

    def start(self):
        while True:
            self.handle_events()
            self.update_logic()
            self.render()

    def handle_events(self):
    
        if self.game_state != GameState.GAMEPLAY: self.current_pointer_rect.topleft = pygame.mouse.get_pos() #Non è necessario aggiornare la posizione del cursore se si è in GAMEPLAY in quanto non viene disegnato

        for event in pygame.event.get():
            if event.type == pygame.QUIT and self.modifying_keybind == False: self.quit_game()  #Chiude il gioco seconda condizione per rendere disponibile il tasto associato quando si stanno modificando le impostazioni
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), settings.flags, vsync=1) # Ridimensiona la superficie dello schermo
            elif event.type == pygame.KEYDOWN:
                if event.key == settings.FULLSCREEN_KEY:  #Attiva/disattiva la modalità fullscreen
                    if not pygame.display.get_surface().get_flags() & pygame.NOFRAME: #Non vera modalità fullscreen per garantire compabilità e rendere più facile cambiare ad altre finestre
                        self.screen = pygame.display.set_mode((self.hw_screen_width, self.hw_screen_height), settings.flags | pygame.NOFRAME, vsync=1)
                    else:
                        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), settings.flags, vsync=1) 
                        
                #Game state specific events
                if event.key == settings.EXIT_KEY: self.quit_game() #Chiude il gioco (scritto qui per evitare ripetizioni nelle funzioni più specifiche)
                elif self.game_state == GameState.START_MENU: handle_start_menu_input(self, event.key)
                elif self.game_state == GameState.GAMEPLAY: handle_gameplay_input(self, event.key)
                elif self.game_state == GameState.PAUSE: handle_pause_input(self, event.key)
                elif self.game_state == GameState.MAP: handle_map_input(self, event.key)
                elif self.game_state == GameState.INVENTORY: handle_inventory_input(self, event.key)
                elif self.game_state == GameState.POKEDEX: handle_pokedex_input(self, event.key)
                elif self.game_state == GameState.SETTINGS_MENU: handle_settings_input(self, event.key)
                elif self.game_state == GameState.HELP_MENU: handle_help_screen_input(self, event.key)
                elif self.game_state == GameState.NAME_MENU: handle_name_menu_input(self, event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Non è possibile unire questo if a quello sopra perchè altrimenti python riconosce pygame.event.Event e quindi non può trovare event.key
                if self.game_state == GameState.SETTINGS_MENU: handle_settings_input_mouse(self)
                elif self.game_state == GameState.START_MENU: handle_start_menu_input_mouse(self)
                elif self.game_state == GameState.NAME_MENU: handle_name_menu_input_mouse(self)
            elif event.type == pygame.MOUSEWHEEL: #Zoom della camera
                self.camera_group.zoom_scale += event.y * settings.ZOOM_SCALING_VELOCITY
            
        #Player controls related events
        if self.game_state == GameState.GAMEPLAY: self.player.move()

        #Update the pointer image if the mouse is over a button
        self.update_pointer()

    def render(self):

        # Pulisce la superficie falsa
        self.fake_screen.fill(settings.BACKGROUND_COLOR)

        if self.game_state == GameState.GAMEPLAY: render_gameplay(self)
        elif self.game_state == GameState.PAUSE: render_pause(self)
        elif self.game_state == GameState.INVENTORY: render_inventory(self)
        elif self.game_state == GameState.POKEDEX: render_pokedex(self)
        elif self.game_state == GameState.MAP: render_map(self)
        elif self.game_state == GameState.START_MENU: render_start_menu(self)
        elif self.game_state == GameState.SETTINGS_MENU: render_settings_menu(self)
        elif self.game_state == GameState.HELP_MENU: render_help_menu(self)
        elif self.game_state == GameState.NAME_MENU: render_name_menu(self, self.simbols_set_index)
        
        #Disegna il puntatore (solamente se non si è in GAMEPLAY)
        if self.game_state != GameState.GAMEPLAY and self.game_state != GameState.HELP_MENU: self.fake_screen.blit(self.current_pointer, self.current_pointer_rect)

        # Ridimensiona la superficie falsa e la disegna sulla finestra
        self.screen.blit(pygame.transform.scale(self.fake_screen, self.screen.get_rect().size), (0, 0))
        pygame.display.flip() # Completly update the display
        self.clock.tick(settings.MAX_FPS)

    def update_logic(self):
        if self.game_state == GameState.START_MENU:
            #Cambio frame dello sfondo
            change_frame_values = self.change_frame(current_animation = self.start_background_images, current_frame = self.start_menu_current_frame, current_last_switch_time = self.background_last_switch_time, image_to_update = self.start_background_image, animation_delay = self.background_frame_switch_delay)
            self.start_background_image = change_frame_values[0]
            self.start_menu_current_frame = change_frame_values[1]
            self.background_last_switch_time = change_frame_values[2]

    def set_pointer_click(self):
        self.current_pointer = self.pointer_click_image
        self.current_pointer_rect = self.pointer_click_image_rect

    def set_pointer_normal(self):
        self.current_pointer = self.pointer_image
        self.current_pointer_rect = self.pointer_image_rect
    
    def update_pointer(self):

        pos = pygame.mouse.get_pos()
        buttons = []

        if self.game_state == GameState.SETTINGS_MENU:
            buttons = [self.save_button_rect, self.restore_button_rect, self.discard_button_rect, self.mute_button_rect]
        elif self.game_state == GameState.START_MENU:
            buttons = [self.new_game_button_rect, self.load_save_button_rect, self.settings_button_rect]
        if any(button.collidepoint(pos) for button in buttons):
            self.set_pointer_click()
        else:
            self.set_pointer_normal()

    def import_frames(self, directory_path): #Importa i frame per una animazione
        images = []
        for filename in listdir(directory_path):
            if filename.endswith('.png') or filename.endswith('.jpg'):
                image = pygame.image.load(path.join(directory_path, filename)).convert_alpha()
                images.append(image)
        return images
    
    def import_sequence_images(self, directory_path): #Importa una serie di immagini come quelle dei tasti per le impostazioni per esempio
        images_dict = {}
        for filename in listdir(directory_path):
            if filename.endswith('.png') or filename.endswith('.jpg'):
                image = pygame.image.load(path.join(directory_path, filename)).convert_alpha()
                # Use os.path.splitext to remove the file extension
                file_name_without_extension = path.splitext(filename)[0]
                images_dict[file_name_without_extension] = image
        return images_dict

    def change_frame(self, current_animation, current_frame, current_last_switch_time, image_to_update, animation_delay): 
        #Al contrario della funzione omonima in player ha bisogno di avere un return perchè ho voluto renderla generica per poterla riutilizzare solo che per fare ciò devo introdurre dei parametri
        current_time = time.time() #e quindi avere un return perchè in python i parametri sono passati per assegnamento e non riferimento
        
        if current_time - self.background_last_switch_time >= animation_delay: 
            current_frame += 1
            if current_frame == len(current_animation): 
                current_frame = 0
            
            image_to_update = current_animation[current_frame]
            current_last_switch_time = current_time # Reset the last frame switch time

        return image_to_update, current_frame, current_last_switch_time
    
    def get_hw_resolution(self):
        # Get a handle to the desktop window
        desktop = windll.user32.GetDesktopWindow()
        # Get a handle to the device context for the desktop window
        dc = windll.user32.GetWindowDC(desktop)
        # Get the physical resolution
        hw_screen_width = windll.gdi32.GetDeviceCaps(dc, 8)  # HORIZONTAL RES
        hw_screen_height = windll.gdi32.GetDeviceCaps(dc, 10)  # VERTICAL RES
        # Release the device context
        windll.user32.ReleaseDC(desktop, dc)

        return hw_screen_width, hw_screen_height

    def quit_game(self):
        pygame.quit()
        quit()