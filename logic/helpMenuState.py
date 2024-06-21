from logic.gameState import GameState
import settings

def handle_help_screen_input(self, key):
    if key == settings.HELP_KEY or settings.ESCAPE_KEY:
        self.game_state = GameState.GAMEPLAY

def render_help_menu(self):
    self.fake_screen.blit(self.darkened_surface, (0,0))