import pygame
from settings import *
from classes.player import Player
from gameState import GameState

class Game:
    def __init__(self):

        #Inizializzazione di Pygame e impostazione dello schermo
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PokèScrauso")
        pygame.display.set_icon(pygame.image.load("graphics/icon.png"))

        #Objects initialization
        self.player = Player(0,0,'down') #Parametri arbitrari per testing, da sistemare

        #Variabili di gioco
        self.game_state = GameState.START_MENU #Stato di gioco iniziale
        self.inventory = {} #Inventario del giocatore

        #Images
        self.start_background = pygame.image.load("graphics/menus/backgrounds/startBackground.png").convert_alpha()
        self.map_image = pygame.image.load("graphics/menus/maps/map.png").convert_alpha()
        self.map_rect = self.map_image.get_rect(center = self.screen.get_rect().center)
        
        #Overlay for map
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) # Create a semi-transparent surface the same size as the screen
        overlay.fill((0, 0, 0, 128))  # RGBA color, 128 alpha for 50% transparency

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
            if event.type == pygame.QUIT: #Mette entrambe a false per uscire completamente dal gioco
                self.quit_game() 
            elif event.type == pygame.VIDEORESIZE: # Ridimensiona la superficie dello schermo
                self.screen = pygame.display.set_mode((event.w, event.h), flags, vsync=1)
            elif event.type == pygame.KEYDOWN:
                if self.game_state == GameState.START_MENU:
                        self.handle_start_menu_input(event.key)
                elif self.game_state == GameState.GAMEPLAY:
                    self.handle_gameplay_input(event.key)
                elif self.game_state == GameState.MAP:
                    self.handle_map_input(event.key)
                elif self.game_state == GameState.INVENTORY:
                    self.handle_inventory_input(event.key)
                elif self.game_state == GameState.POKEDEX:
                    self.handle_pokedex_input(event.key)

    def handle_start_menu_input(self, key):
        if key == INTERACTION_KEY: #Chiude il menu iniziale
            self.game_state = GameState.GAMEPLAY

    def handle_gameplay_input(self, key):
        if key == EXIT_KEY: #Chiude il gioco
            self.quit_game()

    def handle_map_input(self, key):
        if key == MAP_KEY: #Chiude la mappa
            self.game_state = GameState.GAMEPLAY

    def handle_inventory_input(self, key):
        if key == INVENTORY_KEY: #Chiude l'inventario
            self.game_state = GameState.GAMEPLAY

    def handle_pokedex_input(self, key):
        if key == POKEDEK_KEY: #Chiude il PokèDex
            self.game_state = GameState.GAMEPLAY

    def update_logic(self):

        keys = pygame.key.get_pressed() # Restituisce una lista di tasti premuti 
        #Controlla i movimenti del giocatore
        if keys[pygame.K_w]:
            self.player.move_up()
        elif keys[pygame.K_s]:
            self.player.move_down()
        elif keys[pygame.K_a]:
            self.player.move_left()
        elif keys[pygame.K_d]:
            self.player.move_right()

    def render(self):
        self.fake_screen.fill((0,0,0))

        if self.game_state == GameState.START_MENU:
            self.render_start_menu()

        # Ridimensiona la superficie falsa e la disegna sulla finestra
        self.screen.blit(pygame.transform.scale(self.fake_screen, self.screen.get_rect().size), (0, 0))
        pygame.display.flip() # Completly update the display
        self.clock.tick(MAX_FPS)

    def render_start_menu(self):
        self.fake_screen.blit(self.start_background, (0,0))
        self.fake_screen.blit(self.start_button, self.start_button_rect)

    def quit_game(self):
        pygame.quit()
        quit()