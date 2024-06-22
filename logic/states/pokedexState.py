import pygame
from logic.gameState import GameState
import settings

def handle_pokedex_input(self, key):
    if key == settings.POKEDEX_KEY: self.game_state = GameState.POKEDEX if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

def render_pokedex(self):
    pass