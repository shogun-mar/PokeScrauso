from logic.gameState import GameState
import settings

def handle_help_screen_input(game, key):
    if key == settings.HELP_KEY or settings.ESCAPE_KEY:
       game.game_state = GameState.GAMEPLAY

def render_help_menu(game):
    game.fake_screen.blit(game.darkened_surface, (0,0))
    draw_images(game)

def draw_images(game):
    for i in range(len(game.help_keybinds_images_values)):
        game.fake_screen.blit(game.help_keybinds_images_values[i], game.help_menu_images_rects[i])
        game.fake_screen.blit(game.help_menu_rendered_texts[i], game.help_menu_rendered_texts_rects[i])

def draw_texts():
    pass
