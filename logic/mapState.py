import pygame
from logic.gameState import GameState
from settings import *

def handle_map_input(self, key):
    if key == MAP_KEY: self.game_state = GameState.MAP if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

def render_map(self):
    self.fake_screen.fill((150,150,150))
    self.fake_screen.blit(self.overlay, (0,0))
    self.fake_screen.blit(self.map_image, self.map_rect)
    #Disegna cursore sulla mappa
    #TODO