import pygame
from settings import *
from classes.player import Player
from classes.gameState import GameState
from classes.cameraGroup import CameraGroup

class Game:
    def __init__(self):

        #Inizializzazione di Pygame e impostazione dello schermo
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PokèScrauso")
        pygame.display.set_icon(pygame.image.load("graphics/menus/logo.png"))

        #Variabili di gioco
        self.game_state = GameState.START_MENU #Stato di gioco iniziale
        self.inventory = {} #Inventario del giocatore
        self.pokedex = {} #PokèDex del giocatore

        #Objects initialization
        self.camera_group = CameraGroup(self.fake_screen) #Gruppo per gli oggetti che seguono la camera
        self.player = Player((0,0), self.camera_group) #Parametri arbitrari per testing, da sistemare

        #Images
        self.logo = pygame.image.load("graphics/menus/logo.png").convert_alpha()
        self.logo_rect = self.logo.get_rect(center = (self.screen.get_rect().centerx, self.screen.get_rect().centery - 100))
        self.start_background = pygame.image.load("graphics/menus/backgrounds/startBackground.png").convert_alpha()
        self.map_image = pygame.image.load("graphics/menus/maps/map.png").convert_alpha()
        self.map_rect = self.map_image.get_rect(center = self.screen.get_rect().center)
        
        #Overlay for map
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) # Create a semi-transparent surface the same size as the screen
        self.overlay.fill((0, 0, 0, 128))  # RGBA color, 128 alpha for 50% transparency

        #Frame oscurato per il menu di pausa
        self.pause_surface = None #Vuoto in modo che venga inizializzato solo quando serve

        #Buttons
        self.start_button = pygame.image.load("graphics/menus/buttons/startbutton.png").convert_alpha()
        self.start_button_rect = self.start_button.get_rect(); 
        self.start_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

    def start(self):
        while True:
            self.handle_events()
            self.update_logic()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.quit_game()  #Chiude il gioco
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), flags, vsync=1) # Ridimensiona la superficie dello schermo
            elif event.type == pygame.KEYDOWN:
                #Game state specific events
                if event.key == EXIT_KEY: self.quit_game() #Chiude il gioco (scritto qui per evitare ripetizioni nelle funzioni più specifiche)
                elif self.game_state == GameState.START_MENU: self.handle_start_menu_input(event.key)
                elif self.game_state == GameState.GAMEPLAY: self.handle_gameplay_input(event.key)
                elif self.game_state == GameState.PAUSE: self.handle_pause_input(event.key)
                elif self.game_state == GameState.MAP: self.handle_map_input(event.key)
                elif self.game_state == GameState.INVENTORY: self.handle_inventory_input(event.key)
                elif self.game_state == GameState.POKEDEX: self.handle_pokedex_input(event.key)
            
        #Player controls related events
        if self.game_state == GameState.GAMEPLAY: self.player.move()

    def handle_start_menu_input(self, key):
        if key == INTERACTION_KEY: self.game_state = GameState.GAMEPLAY #Chiude il menu iniziale

    def handle_gameplay_input(self, key):
        if key == MAP_KEY: self.game_state = GameState.MAP #Apre la mappa
        elif key == PAUSE_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            self.pause_surface = pygame.Surface(self.screen.get_size())
            self.pause_surface.blit(self.fake_screen, (0,0))
            self.pause_surface.set_alpha(128)
            self.game_state = GameState.PAUSE #Apre il menu di pausa 
        elif key == INVENTORY_KEY: self.game_state = GameState.INVENTORY #Apre l'inventario
        elif key == POKEDEK_KEY: self.game_state = GameState.POKEDEX #Apre il PokèDex

    def handle_map_input(self, key):
        if key == MAP_KEY: self.game_state = GameState.MAP if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

    def handle_inventory_input(self, key):
        if key == INVENTORY_KEY: self.game_state = GameState.INVENTORY if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

    def handle_pokedex_input(self, key):
        if key == POKEDEK_KEY: self.game_state = GameState.POKEDEX if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

    def handle_pause_input(self, key):
        if key == PAUSE_KEY:
            if self.game_state == GameState.GAMEPLAY:
                self.game_state = GameState.PAUSE
            else:
                self.game_state = GameState.GAMEPLAY

    def update_logic(self):
        pass

    def render(self):

        # Pulisce la superficie falsa
        self.fake_screen.fill((0,0,0))

        if self.game_state == GameState.GAMEPLAY: self.render_gameplay()
        elif self.game_state == GameState.PAUSE: self.render_pause()
        elif self.game_state == GameState.INVENTORY: self.render_inventory()
        elif self.game_state == GameState.POKEDEX: self.render_pokedex()
        elif self.game_state == GameState.MAP: self.render_map()
        elif self.game_state == GameState.START_MENU: self.render_start_menu()
        
        # Ridimensiona la superficie falsa e la disegna sulla finestra
        self.screen.blit(pygame.transform.scale(self.fake_screen, self.screen.get_rect().size), (0, 0))
        pygame.display.flip() # Completly update the display
        self.clock.tick(MAX_FPS)

    def render_gameplay(self):
        
        self.camera_group.custom_draw(self.player)

    def render_pause(self):
        #print("Rendering pause")
        self.fake_screen.blit(self.pause_surface, (0,0))
        font = pygame.font.Font(None, 36)  # Choose the font for the text
        text = font.render("Pause", True, (255, 255, 255))  # Create a surface with the text
        text_rect = text.get_rect(center=self.screen.get_rect().center)  # Get the rectangle of the text surface
        self.fake_screen.blit(text, text_rect)

    def render_inventory(self):
        pass
        #print("Rendering inventory")

    def render_pokedex(self):
        pass
        #print("Rendering pokedex")

    def render_map(self):
        #print("Rendering map")
        self.fake_screen.fill((150,150,150))
        self.fake_screen.blit(self.overlay, (0,0))
        self.fake_screen.blit(self.map_image, self.map_rect)

        #Disegna cursore sulla mappa
        #...

    def render_start_menu(self):

        #Disegno dei componenti
        self.fake_screen.blit(self.start_background, (0,0))
        self.fake_screen.blit(self.logo, self.logo_rect)
        self.fake_screen.blit(self.start_button, self.start_button_rect)

        #Controllo interazione con il pulsante
        mouse_pos = pygame.mouse.get_pos()
        if self.start_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]: self.game_state = GameState.GAMEPLAY

    def quit_game(self):
        pygame.quit()
        quit()