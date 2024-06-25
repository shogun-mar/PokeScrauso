import settings
from logic.gameState import GameState

previous_gamestate = None #Serve per differenziare i testi da scrivere (se in battaglia non dare l'opzione di uscire dal menù)

def render_squad_menu(game):
    game.fake_screen.blit(game.squad_menu_background, (0, 0))
    game.fake_screen.blit(game.squad_menu_overlay, (0, 384))
    game.fake_screen.blit(game.squad_menu_overlay_text, (35, 428))
    game.fake_screen.blit(game.squad_menu_cancel_button, game.squad_menu_cancel_button_rect)
    for i in range(6):
        game.fake_screen.blit(game.squad_menu_blank_panel, game.squad_menu_panel_rects[i])

def handle_squad_menu_input(game, key):
    global previous_gamestate
    previous_gamestate = game.game_state
    if key == settings.PAUSE_KEY or settings.SQUAD_KEY:
        game.game_state = GameState.GAMEPLAY