import settings
from logic.states.gameState import GameState

HEALTH_BAR_WIDTH=98
HEALTH_BAR_HEIGHT=7

def handle_battle_input(game, key):
    pass

def handle_battle_input_mouse(game, mouse_pos):
    pass

def render_battle(game):
    game.fake_screen.blit(game.battle_background, (0, 0))
    if game.beginning_battle_animation_finished == False: game.fake_screen.blit(game.beginning_battle_animation_image, (400, 200))





