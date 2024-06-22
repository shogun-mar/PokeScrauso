import pygame
from logic.gameState import GameState
import settings

def render_inventory(game):
        pass

def handle_inventory_input(game, key):
        if key == settings.INVENTORY_KEY: game.game_state = GameState.INVENTORY if game.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY