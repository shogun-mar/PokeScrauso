import pygame
from classes.gameState import GameState
from settings import *

def handle_gameplay_input(self, key):
        if key == MAP_KEY: self.game_state = GameState.MAP #Apre la mappa
        elif key == PAUSE_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            self.darkened_surface = pygame.Surface(self.fake_screen.get_size())
            self.darkened_surface.blit(self.fake_screen, (0,0))
            self.darkened_surface.set_alpha(128)
            self.game_state = GameState.PAUSE #Apre il menu di pausa 
        elif key == INVENTORY_KEY: self.game_state = GameState.INVENTORY #Apre l'inventario
        elif key == POKEDEX_KEY: self.game_state = GameState.POKEDEX #Apre il PokèDex
        elif key == HELP_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            self.darkened_surface = pygame.Surface(self.fake_screen.get_size())
            self.darkened_surface.blit(self.fake_screen, (0,0))
            self.darkened_surface.set_alpha(128) 
            self.game_state = GameState.HELP_MENU

def render_gameplay(self):
    self.camera_group.custom_draw(self.player)