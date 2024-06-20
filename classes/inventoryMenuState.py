import pygame
from classes.gameState import GameState
from settings import *

def render_inventory(self):
        pass

def handle_inventory_input(self, key):
        if key == INVENTORY_KEY: self.game_state = GameState.INVENTORY if self.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY