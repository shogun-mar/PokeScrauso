import settings
from logic.gameState import GameState

def render_squad_menu(game):
    pass

def handle_squad_menu_input(game, key):
    if key == settings.PAUSE_KEY:
        game.game_state = GameState.START_MENU