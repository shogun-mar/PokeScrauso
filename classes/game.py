import pygame
import time
from random import randint
from os import listdir, environ, path
from ctypes import windll
from settings import *
from classes.player import Player
from classes.gameState import GameState
from classes.cameraGroup import CameraGroup

class Game:
    def __init__(self):

        #Inizializzazione di Pygame e impostazione dello schermo
        # Center the Pygame window
        environ['SDL_VIDEO_CENTERED'] = '1' #Comando di SDL per centrare la finestra
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PokèScrauso")
        pygame.display.set_icon(pygame.image.load("graphics/UI/menus/logo_small.png"))
        # Allow only specific events
        pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEWHEEL, pygame.QUIT, pygame.KEYDOWN, pygame.VIDEORESIZE])
        # Get physical resolution
        self.hw_screen_width = self.get_hw_resolution()[0]  # HORIZONTAL RES
        self.hw_screen_height = self.get_hw_resolution()[1]  # VERTICAL RES
        
        #Variabili di gioco
        self.half_w = SCREEN_WIDTH // 2 #Metà della larghezza dello schermo
        self.half_h = SCREEN_HEIGHT // 2
        self.current_volume_status = True #Stato attuale del volume (True = ON, False = OFF)
        self.game_state = GameState.START_MENU #Stato di gioco iniziale

        #Objects initialization
        self.camera_group = CameraGroup(self.fake_screen) #Gruppo per gli oggetti che seguono la camera
        self.player = Player((0,0), self.camera_group) #Parametri arbitrari per testing, da sistemare

        #Pointer images
        self.pointer_image = pygame.image.load("graphics/UI/menus/pointers/pointer.png").convert_alpha()
        self.pointer_image_rect = self.pointer_image.get_rect(center = (0,0))
        self.pointer_click_image = pygame.image.load("graphics/UI/menus/pointers/pointer_click.png").convert_alpha()
        self.pointer_click_image_rect = self.pointer_click_image.get_rect(center = (0,0))
        self.current_pointer = self.pointer_image #Disegno sempre questa variabile ma cambio il suo valore in base alla posizione del mouse
        self.current_pointer_rect = self.pointer_image_rect
        pygame.mouse.set_visible(False) #Nasconde il cursore del mouse (sulla sua posizione verranno però disegnate le immagini dei puntatori personalizzati)   

        #Start images
        randomint = randint(1,2)
        self.start_background_images = self.import_frames("graphics/UI/menus/backgrounds/start_menu_background"+str(randomint))
        self.start_menu_current_frame = 0
        if randomint == 1: self.background_frame_switch_delay = 0.16 #Il delay fra i frame cambia in base allo sfondo
        elif randomint == 2: self.background_frame_switch_delay = 0.06
        self.background_last_switch_time = time.time()
        self.start_background_image = self.start_background_images[self.start_menu_current_frame]
        self.start_text_image = pygame.image.load("graphics/UI/menus/texts/start_menu_text.png").convert_alpha()
        self.start_text_image_rect = self.start_text_image.get_rect(center = (self.half_w, self.half_h - 100))
        self.new_game_button = pygame.image.load("graphics/UI/menus/buttons/start_menu_new_game_text.png").convert_alpha()
        self.new_game_button_rect = self.new_game_button.get_rect(center = (self.half_w, self.half_h + 50))
        self.load_save_button = pygame.image.load("graphics/UI/menus/buttons/start_menu_load_save_text.png").convert_alpha()
        self.load_save_button_rect = self.load_save_button.get_rect(center = (self.half_w, self.half_h + 150))
        self.settings_button = pygame.image.load("graphics/UI/menus/buttons/settings_icon.png").convert_alpha()
        self.settings_button_rect = self.settings_button.get_rect(center = (SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40))

        #Settings images
        self.settings_background_image = pygame.image.load("graphics/UI/menus/backgrounds/settings_background" + str(randint(1,2)) + ".png").convert_alpha()
        self.save_button = pygame.image.load("graphics/UI/menus/buttons/save_button.png").convert_alpha()
        self.save_button_rect = self.save_button.get_rect(center = (self.half_w + 16, SCREEN_HEIGHT - 50 ))
        self.restore_button = pygame.image.load("graphics/UI/menus/buttons/restore_button.png").convert_alpha()
        self.restore_button_rect = self.restore_button.get_rect(center = (self.half_w - 16, SCREEN_HEIGHT - 50))
        self.discard_button = pygame.image.load("graphics/UI/menus/buttons/discard_button.png").convert_alpha()
        self.discard_button_rect = self.discard_button.get_rect(center = (self.half_w - 48, SCREEN_HEIGHT - 50))
        self.mute_button = pygame.image.load("graphics/UI/menus/buttons/mute_button.png").convert_alpha()
        self.mute_button_rect = self.mute_button.get_rect(center = (self.half_w + 48, SCREEN_HEIGHT - 50))
        self.unmute_button = pygame.image.load("graphics/UI/menus/buttons/unmute_button.png").convert_alpha()
        self.unmute_button_rect = self.unmute_button.get_rect(center = (self.half_w + 48, SCREEN_HEIGHT - 50))

        self.key_images = self.import_frames("graphics/UI/menus/icon/keys")
        
        #Map images
        self.map_image = pygame.image.load("graphics/UI/menus/maps/map.png").convert_alpha()
        self.map_rect = self.map_image.get_rect(center = self.screen.get_rect().center)
        
        #Overlay for map
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) # Create a semi-transparent surface the same size as the screen

        #Frame oscurato per il menu di pausa
        self.pause_surface = None #Vuoto in modo che venga inizializzato solo quando serve

        #Text
        self.poke_font = pygame.font.Font("graphics/fonts/Pokemon Hollow.ttf", 50)

    def start(self):
        while True:
            self.handle_events()
            self.update_logic()
            self.render()

    def handle_events(self):
    
        if self.game_state != GameState.GAMEPLAY: self.current_pointer_rect.topleft = pygame.mouse.get_pos() #Non è necessario aggiornare la posizione del cursore se si è in GAMEPLAY in quanto non viene disegnato

        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.quit_game()  #Chiude il gioco
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), flags, vsync=1) # Ridimensiona la superficie dello schermo
            elif event.type == pygame.KEYDOWN:
                if event.key == FULLSCREEN_KEY:  #Attiva/disattiva la modalità fullscreen
                    if not pygame.display.get_surface().get_flags() & pygame.NOFRAME: #Non vera modalità fullscreen per garantire compabilità e rendere più facile cambiare ad altre finestre
                        self.screen = pygame.display.set_mode((self.hw_screen_width, self.hw_screen_height), flags | pygame.NOFRAME)
                        
                    else:
                        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags) 
                        

                #Game state specific events
                if event.key == EXIT_KEY: self.quit_game() #Chiude il gioco (scritto qui per evitare ripetizioni nelle funzioni più specifiche)
                elif self.game_state == GameState.START_MENU: self.handle_start_menu_input(event.key)
                elif self.game_state == GameState.GAMEPLAY: self.handle_gameplay_input(event.key)
                elif self.game_state == GameState.PAUSE: self.handle_pause_input(event.key)
                elif self.game_state == GameState.MAP: self.handle_map_input(event.key)
                elif self.game_state == GameState.INVENTORY: self.handle_inventory_input(event.key)
                elif self.game_state == GameState.POKEDEX: self.handle_pokedex_input(event.key)
                elif self.game_state == GameState.SETTINGS_MENU: self.handle_settings_input(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Non è possibile unire questo if a quello sopra perchè altrimenti python riconosce pygame.event.Event e quindi non può trovare event.key
                if self.game_state == GameState.SETTINGS_MENU: self.handle_settings_input_mouse()
                if self.game_state == GameState.START_MENU: self.handle_start_menu_input_mouse()
            elif event.type == pygame.MOUSEWHEEL: #Zoom della camera
                self.camera_group.zoom_scale += event.y * ZOOM_SCALING_VELOCITY
            
        #Player controls related events
        if self.game_state == GameState.GAMEPLAY: self.player.move()

        #Update the pointer image if the mouse is over a button
        self.update_pointer()

    def handle_start_menu_input(self, key):
        if key == INTERACTION_KEY: self.game_state = GameState.GAMEPLAY #Chiude il menu iniziale

    def handle_start_menu_input_mouse(self):
        #Controllo interazione con il pulsante
        mouse_pos = pygame.mouse.get_pos()
        if self.new_game_button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: 
                #Start new game
                #TODO
                self.game_state = GameState.GAMEPLAY

        elif self.load_save_button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                #Load save
                #TODO
                self.game_state = GameState.GAMEPLAY
        
        elif self.settings_button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                #Open settings
                self.game_state = GameState.SETTINGS_MENU

    def handle_gameplay_input(self, key):
        if key == MAP_KEY: self.game_state = GameState.MAP #Apre la mappa
        elif key == PAUSE_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            self.pause_surface = pygame.Surface(self.screen.get_size())
            self.pause_surface.blit(self.fake_screen, (0,0))
            self.pause_surface.set_alpha(128)
            self.game_state = GameState.PAUSE #Apre il menu di pausa 
        elif key == INVENTORY_KEY: self.game_state = GameState.INVENTORY #Apre l'inventario
        elif key == POKEDEX_KEY: self.game_state = GameState.POKEDEX #Apre il PokèDex

    def handle_map_input(self, key):
        if key == MAP_KEY: self.game_state = GameState.MAP if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

    def handle_inventory_input(self, key):
        if key == INVENTORY_KEY: self.game_state = GameState.INVENTORY if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

    def handle_pokedex_input(self, key):
        if key == POKEDEX_KEY: self.game_state = GameState.POKEDEX if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

    def handle_pause_input(self, key):
        if key == PAUSE_KEY:
            if self.game_state == GameState.GAMEPLAY:
                self.game_state = GameState.PAUSE
            else:
                self.game_state = GameState.GAMEPLAY

    def handle_settings_input(self, key):
        
        if key == PAUSE_KEY:
            self.game_state = GameState.START_MENU
        elif key == SAVE_SETTINGS_KEY:
            #Salva le impostazioni
            save_configuration()
        elif key == RESTORE_SETTINGS_KEY:
            #Ripristina le impostazioni
            set_default_configuration()
        elif key == DISCARD_SETTINGS_KEY:
            #Scarta le impostazioni
            #TODO
            print("Scarta le impostazioni") #Placeholder
            #discard_configuration()
        elif key == MUTE_KEY:
            print("Muta il gioco")
            #Muta il gioco
            self.current_volume_status = not self.current_volume_status

    def handle_settings_input_mouse(self):
        if self.save_button_rect.collidepoint(pygame.mouse.get_pos()):
            #Salva le impostazioni
            save_configuration()
        elif self.restore_button_rect.collidepoint(pygame.mouse.get_pos()):
            #Ripristina le impostazioni
            set_default_configuration()
        elif self.discard_button_rect.collidepoint(pygame.mouse.get_pos()):
            #Scarta le impostazioni
            #TODO
            print("Scarta le impostazioni") #Placeholder
            #discard_configuration()
        elif self.mute_button_rect.collidepoint(pygame.mouse.get_pos()):
            print("Muta il gioco")
            #Muta il gioco
            self.current_volume_status = not self.current_volume_status

    def render(self):

        # Pulisce la superficie falsa
        self.fake_screen.fill(BACKGROUND_COLOR)

        if self.game_state == GameState.GAMEPLAY: self.render_gameplay()
        elif self.game_state == GameState.PAUSE: self.render_pause()
        elif self.game_state == GameState.INVENTORY: self.render_inventory()
        elif self.game_state == GameState.POKEDEX: self.render_pokedex()
        elif self.game_state == GameState.MAP: self.render_map()
        elif self.game_state == GameState.START_MENU: self.render_start_menu()
        elif self.game_state == GameState.SETTINGS_MENU: self.render_settings_menu()
        
        #Disegna il puntatore (solamente se non si è in GAMEPLAY)
        if self.game_state != GameState.GAMEPLAY: self.fake_screen.blit(self.current_pointer, self.current_pointer_rect)

        # Ridimensiona la superficie falsa e la disegna sulla finestra
        self.screen.blit(pygame.transform.scale(self.fake_screen, self.screen.get_rect().size), (0, 0))
        pygame.display.flip() # Completly update the display
        self.clock.tick(MAX_FPS)

    def render_gameplay(self):
        
        self.camera_group.custom_draw(self.player)

    def render_pause(self):
        self.fake_screen.blit(self.pause_surface, (0,0))
        font = pygame.font.Font(None, 36)  # Choose the font for the text
        text = font.render("Pause", True, (255, 255, 255))  # Create a surface with the text
        text_rect = text.get_rect(center=self.screen.get_rect().center)  # Get the rectangle of the text surface
        self.fake_screen.blit(text, text_rect)

    def render_inventory(self):
        pass

    def render_pokedex(self):
        pass

    def render_map(self):
        self.fake_screen.fill((150,150,150))
        self.fake_screen.blit(self.overlay, (0,0))
        self.fake_screen.blit(self.map_image, self.map_rect)

        #Disegna cursore sulla mappa
        #...

    def render_start_menu(self):

        #Disegno dei componenti
        self.fake_screen.blit(self.start_background_image, (0,0))
        self.fake_screen.blit(self.start_text_image, self.start_text_image_rect)
        self.fake_screen.blit(self.new_game_button, self.new_game_button_rect)
        self.fake_screen.blit(self.load_save_button, self.load_save_button_rect)
        self.fake_screen.blit(self.settings_button, self.settings_button_rect)

    def render_settings_menu(self):

        self.fake_screen.blit(self.settings_background_image, (0,0))
        self.fake_screen.blit(self.save_button, self.save_button_rect)
        self.fake_screen.blit(self.restore_button, self.restore_button_rect)
        self.fake_screen.blit(self.discard_button, self.discard_button_rect)
        self.fake_screen.blit(self.mute_button, self.mute_button_rect) if self.current_volume_status else self.fake_screen.blit(self.unmute_button, self.unmute_button_rect)
    
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