import pygame
import settings
from logic.gameState import GameState

start_x = 85
start_y = 235
padding_x = 46
padding_y = 50
row = 1
column = 1

MAX_ROW = 2 #Numero di righe per ogni set di caratteri (placeholder arbitrario)
MAX_COLUMN = 13 #Numero di colonne per ogni riga (placeholder arbitrario)

def handle_name_menu_input(game, key):
    if key == settings.FORWARD_KEY or key == settings.BACKWARD_KEY or key == settings.LEFT_KEY or key == settings.RIGHT_KEY:
        move_cursor(game, key)
    elif key == settings.INTERACTION_KEY:
        selected_char = game.simbols[game.simbols_set_index][(row-1)*13 + (column-1)]
        update_player_name(game, selected_char)

def handle_name_menu_input_mouse(game, mouse_pos):
    print(mouse_pos)

    #lower button
    if game.simbol_set_icons_rects[0].collidepoint(mouse_pos):
        game.simbols_set_index = 0
        update_maximums(game)

    #upper button
    elif game.simbol_set_icons_rects[1].collidepoint(mouse_pos):
        game.simbols_set_index = 1
        update_maximums(game)

    #caratteri accentati button
    elif game.simbol_set_icons_rects[2].collidepoint(mouse_pos):
        game.simbols_set_index = 2
        update_maximums(game)

    #simbols button
    elif game.simbol_set_icons_rects[3].collidepoint(mouse_pos):
        game.simbols_set_index = 3
        update_maximums(game)

    #ok button topleft: 555, 150 bottomright: 655, 200
    elif mouse_pos[0] >= 555 and mouse_pos[0] <= 655 and mouse_pos[1] >= 150 and mouse_pos[1] <= 200:
        if is_name_valid(game): #Se l'utente ha inserito almeno un carattere
            game.player_name = game.player_name.replace("_", "")
            game.game_state = GameState.GAMEPLAY

    #back button: topleft 440, 150 bottomright 540, 200
    elif mouse_pos[0] >= 440 and mouse_pos[0] <= 540 and mouse_pos[1] >= 150 and mouse_pos[1] <= 200:
        delete_last_char(game)

def render_name_menu(game, simbols_set_index):
    game.fake_screen.blit(game.name_menu_background, (0, 0))
    game.fake_screen.blit(game.name_menu_overlay_tab, (22, 190))
    game.fake_screen.blit(game.name_menu_overlay_controls, (22, 120))
    game.fake_screen.blit(game.player_name_text, (150, 50))
    game.fake_screen.blit(game.name_menu_icon_shadow, (75, 70))
    game.fake_screen.blit(game.name_menu_icon, (75, 25))
    for i in range(len(game.simbol_set_icons)):
       if i != simbols_set_index: game.fake_screen.blit(game.simbol_set_icons[i], game.simbol_set_icons_rects[i])
    for i in range(len(game.rendered_name_menu_texts[simbols_set_index])):
        game.fake_screen.blit(game.rendered_name_menu_texts[simbols_set_index][i], game.rendered_name_menu_texts_rects[simbols_set_index][i])
    game.fake_screen.blit(game.name_menu_cursor, game.name_menu_cursor_rect)

def move_cursor(game, key):
    global row, column
    simbols_set_index = game.simbols_set_index

    if key == settings.FORWARD_KEY:
        if row > 1:
            row -= 1

    elif key == settings.BACKWARD_KEY:
        if row < MAX_ROW:
            row += 1

    elif key == settings.LEFT_KEY:
        #if game.name_menu_cursor_rect.x > start_x:
        if column > 1:
            column -= 1
        elif column == 1:
                row -= 1
                column = 13

    elif key == settings.RIGHT_KEY and (row-1)*13 + (column-1) < len(game.rendered_name_menu_texts[simbols_set_index])-1:
        #if game.name_menu_cursor_rect.x <= settings.SCREEN_WIDTH - start_x - padding_x:
        if column < MAX_COLUMN:
            column += 1
        elif column == 13:
            row += 1
            column = 1

    try: #Alcune set di caratteri sono più corti di altri, quindi se si va oltre il limite, si va all'ultimo carattere del set
        game.name_menu_cursor_rect.center = game.rendered_name_menu_texts_rects[simbols_set_index][(row-1)*13 + (column-1)].center
    except IndexError:
        row = len(game.rendered_name_menu_texts[simbols_set_index]) // 13
        column = len(game.rendered_name_menu_texts[simbols_set_index]) % 13
        game.name_menu_cursor_rect.center = game.rendered_name_menu_texts_rects[simbols_set_index][len(game.rendered_name_menu_texts[simbols_set_index])-1].center

def render_name_menu_texts(font, color, game):
    rendered_texts = []  # Two-dimensional list containing dictionaries for each category
                         # [[lower], [upper], [accentati], [speciali]]

    for simbol_set in game.simbols:
        temp_array = []
        for simbol in simbol_set:
            temp_array.append(font.render(simbol, True, color))
        rendered_texts.append(temp_array)
    return rendered_texts

def get_name_menu_texts_rects(rendered_texts):
    rects = [] #Two-dimensional list containing the rects of each symbol
               # [[lower], [upper], [accentati], [speciali]]

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

def delete_last_char(game):
    temp_name_list = list(game.player_name)
    for i in range(11, -1, -1):  #for i in range(len(game.player_name)-1, -1, -1): Sarebbe teoricamente più corretto ma la lunghezza del nome non può superare 12
        if temp_name_list[i] != "_": #quindi evito calcoli non necessari
            temp_name_list[i] = "_"
            break
    game.player_name = "".join(temp_name_list) #Ricongiunge la lista in una stringa
    game.player_name_text = game.naming_menu_font.render(game.player_name, True, game.naming_menu_color) #Renderizza il testo aggiornato

def update_maximums(game):
    global MAX_ROW, MAX_COLUMN
    MAX_ROW = (len(game.rendered_name_menu_texts[game.simbols_set_index]) // 13) + 1 #+ 1 in modo da renderli uniformi con il trattamento di row e column
    MAX_COLUMN = (len(game.rendered_name_menu_texts[game.simbols_set_index]) % 13) + 1 