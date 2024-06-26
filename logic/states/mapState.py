import pygame
from logic.states.gameState import GameState
import settings

def handle_map_input(game, key):
    if key == settings.MAP_KEY: game.game_state = GameState.MAP if game.game_state == GameState.GAMEPLAY else GameState.GAMEPLAY

def render_map(game):
    game.fake_screen.fill((150,150,150))
    game.fake_screen.blit(game.overlay, (0,0))
    game.fake_screen.blit(game.map_image, game.map_rect)
    #Disegna cursore sulla mappa
    #TODO