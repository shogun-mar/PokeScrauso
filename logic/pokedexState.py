import pygame
from logic.gameState import GameState
from settings import *

def handle_pokedex_input(self, key):
    if key == POKEDEX_KEY: self.game_state = GameState.POKEDEX if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

def render_pokedex():
    pass