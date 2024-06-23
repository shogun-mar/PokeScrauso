import pygame
import settings
from logic.gameState import GameState

start_x = 85
start_y = 235
padding_x = 46
padding_y = 50
row = 1
column = 1

def handle_name_menu_input(game, key):
    if key == settings.FORWARD_KEY or key == settings.BACKWARD_KEY or key == settings.LEFT_KEY or key == settings.RIGHT_KEY:
        move_cursor(game, key)
    elif key == settings.INTERACTION_KEY:
        selected_char = game.simbols[game.simbols_set_index][(row-1)*13 + (column-1)]
        update_player_name(game, selected_char)

def handle_name_menu_input_mouse(game):
    mouse_pos = pygame.mouse.get_pos()
    #ok button topleft: 555, 150 bottomright: 655, 200
    if mouse_pos[0] >= 555 and mouse_pos[0] <= 655 and mouse_pos[1] >= 150 and mouse_pos[1] <= 200:
        if is_name_valid(game): #Se l'utente ha inserito almeno un carattere
            game.player_name = game.player_name.replace("_", "")
            game.game_state = GameState.GAMEPLAY
    

def render_name_menu(game, simbols_set_index):
    game.fake_screen.blit(game.name_menu_background, (0, 0))
    game.fake_screen.blit(game.name_menu_overlay_tab, (22, 190))
    game.fake_screen.blit(game.name_menu_overlay_controls, (22, 120))
    game.fake_screen.blit(game.player_name_text, (100, 50))
    for i in range(len(game.rendered_name_menu_texts[simbols_set_index])):
        game.fake_screen.blit(game.rendered_name_menu_texts[simbols_set_index][i], game.rendered_name_menu_texts_rects[simbols_set_index][i])
    game.fake_screen.blit(game.name_menu_cursor, game.name_menu_cursor_rect)

def move_cursor(game, key):
    global row, column
    simbols_set_index = game.simbols_set_index  # Corrected variable name from 'simbols_set_index' to 'symbols_set_index'

    if key == settings.FORWARD_KEY:
        if row > 1:
            row -= 1

    elif key == settings.BACKWARD_KEY:
        if row < len(game.rendered_name_menu_texts[simbols_set_index]) // 13:
            row += 1

    elif key == settings.LEFT_KEY:
        if game.name_menu_cursor_rect.x > start_x:
            column -= 1
        elif column == 1:
                row -= 1
                column = 13

    elif key == settings.RIGHT_KEY and (row-1)*13 + (column-1) < len(game.rendered_name_menu_texts[simbols_set_index])-1:
        if game.name_menu_cursor_rect.x <= settings.SCREEN_WIDTH - start_x - padding_x:
            column += 1
        elif column == 13:
            row += 1
            column = 1

    game.name_menu_cursor_rect.center = game.rendered_name_menu_texts_rects[simbols_set_index][(row-1)*13 + (column-1)].center

def render_name_menu_texts(font, color, game):
    rendered_texts = []  # List containing dictionaries for each category
    

    for simbol_set in game.simbols:
        temp_array = []
        for simbol in simbol_set:
            temp_array.append(font.render(simbol, True, color))
        rendered_texts.append(temp_array)
    return rendered_texts

def get_name_menu_texts_rects(rendered_texts):
    rects = [] #Three-dimensional list containing the rects of each symbol

    for simbols_set in rendered_texts:
        x_coord = start_x
        y_coord = start_y  
        temp_array = []
        for simbol_surf in simbols_set:
            temp_array.append(simbol_surf.get_rect(center=(x_coord, y_coord)))
            if x_coord <= settings.SCREEN_WIDTH - start_x:
                x_coord += padding_x
            else:
                x_coord = start_x
                y_coord += padding_y
        rects.append(temp_array)
    
    return rects

def update_player_name(game, selected_char):
    new_name = ""
    for char in game.player_name:
        if char != "_":
            new_name += char
        else:
            new_name += selected_char
            break #Dopo aver trovato il carattere da sostituire, esce dal ciclo in modo da poter riempire li spazi rimanenti con '_'

    while len(new_name) < 12: # Comunemente in python quando si scrive _ si intende una variabile trascurabile
        new_name += "_"
    
    game.player_name = new_name
    game.player_name_text = game.naming_menu_font.render(new_name, True, game.naming_menu_color)
    
def is_name_valid(game):
    blank_spaces_count = game.player_name.count("_")
    if blank_spaces_count < 12: #12 è la lunghezza massima del nome
        return True
