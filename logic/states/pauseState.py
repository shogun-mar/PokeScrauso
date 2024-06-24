import pygame
from logic.gameState import GameState
import settings

def handle_pause_input(game, key):
    if key == settings.PAUSE_KEY:
        if game.game_state == GameState.GAMEPLAY:
            game.game_state = GameState.PAUSE
        else:
            game.game_state = GameState.GAMEPLAY

def render_pause(game):
        game.fake_screen.blit(game.darkened_surface, (0,0))
        text = game.naming_menu_font.render("è é ì ò à ù", True, (255, 255, 255))  # Create a surface with the text
        text_rect = text.get_rect(center=game.screen.get_rect().center)  # Get the rectangle of the text surface
        game.fake_screen.blit(text, text_rect)