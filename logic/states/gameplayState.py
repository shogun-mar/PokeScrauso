import pygame
from logic.gameState import GameState
import settings

def handle_gameplay_input(self, key):
        if key == settings.MAP_KEY: self.game_state = GameState.MAP #Apre la mappa
        elif key == settings.SQUAD_KEY: self.game_state = GameState.SQUAD_MENU #Apre il menu della squadra
        elif key == settings.INVENTORY_KEY: self.game_state = GameState.INVENTORY #Apre l'inventario
        elif key == settings.POKEDEX_KEY: self.game_state = GameState.POKEDEX #Apre il PokèDex
        elif key == settings.PAUSE_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            self.darkened_surface = pygame.Surface(self.fake_screen.get_size())
            self.darkened_surface.blit(self.fake_screen, (0,0))
            self.darkened_surface.set_alpha(128)
            self.game_state = GameState.PAUSE #Apre il menu di pausa
        elif key == settings.HELP_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            self.darkened_surface = pygame.Surface(self.fake_screen.get_size())
            self.darkened_surface.blit(self.fake_screen, (0,0))
            self.darkened_surface.set_alpha(128) 
            self.game_state = GameState.HELP_MENU

def render_gameplay(self):
    self.camera_group.custom_draw(self.player)