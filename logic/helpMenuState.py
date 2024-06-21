from logic.gameState import GameState
from settings import *

def handle_help_screen_input(self, key):
    if key == HELP_KEY:
        self.game_state = GameState.GAMEPLAY

def render_help_menu(self):
    self.fake_screen.blit(self.darkened_surface, (0,0))