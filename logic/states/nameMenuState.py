import settings

start_x = 85
start_y = 235
padding_x = 46
padding_y = 50

row = 1
column = 1

def handle_name_menu_input(game, key):
    if key == settings.FORWARD_KEY or key == settings.BACKWARD_KEY or key == settings.LEFT_KEY or key == settings.RIGHT_KEY:
        move_cursor(game, key)

def render_name_menu(game, simbols_set_index):
    game.fake_screen.blit(game.name_menu_background, (0, 0))
    game.fake_screen.blit(game.name_menu_overlay_tab, (22, 190))
    game.fake_screen.blit(game.name_menu_overlay_controls, (22, 120))
    for i in range(len(game.rendered_name_menu_texts[simbols_set_index])):
        game.fake_screen.blit(game.rendered_name_menu_texts[simbols_set_index][i], game.rendered_name_menu_texts_rects[simbols_set_index][i])
    game.fake_screen.blit(game.name_menu_cursor, game.name_menu_cursor_rect)

def move_cursor(game, key):
    global row, column
    simbols_set_index = game.simbols_set_index
    if key == settings.LEFT_KEY:
        if game.name_menu_cursor_rect.x > start_x:
            column -=1
        elif column == 1:
            row -= 1
            column = 13

    elif key == settings.RIGHT_KEY:
        if game.name_menu_cursor_rect.x <= settings.SCREEN_WIDTH - start_x - padding_x:
            column += 1
        else:
            row += 1
            column = 1

    elif key == settings.FORWARD_KEY:
        if row > 1:
            row -= 1

    elif key == settings.BACKWARD_KEY:
        if row <= len(game.rendered_name_menu_texts[simbols_set_index])//14:
            row += 1

    game.name_menu_cursor_rect.center = game.rendered_name_menu_texts_rects[simbols_set_index][(row-1)*14 + (column-1)].center
    print((row-1)*13 + (column-1))

def render_name_menu_texts(font, color):
    rendered_texts = [] #[[lettere maiuscole], [lettere minuscole], [numeri e simboli]]
    simbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ':', ', ', ';', "'", '"', '!', '?', '(', ')', '+', '-', '*', '/', '=']
    
    temp_array = [] #Array temporaneo per contenere le lettere renderizzate

    for simbol in simbols:
        rendered_simbol = font.render(simbol, True, color)
        temp_array.append(rendered_simbol)
        if simbol == 'z' or simbol == 'Z' or simbol == '=':
            rendered_texts.append(temp_array)
            temp_array = []

    return rendered_texts

def get_name_menu_texts_rects(rendered_texts):
    all_rects = []  #Three-dimensional list

    for simbols_set in rendered_texts:
        x_coord = start_x
        y_coord = start_y
        temp_array = []
        for simbol in simbols_set:
            temp_array.append(simbol.get_rect(center=(x_coord, y_coord)))
            if x_coord <= settings.SCREEN_WIDTH - start_x:
                x_coord += padding_x
            else:
                x_coord = start_x
                y_coord += padding_y
        all_rects.append(temp_array)

    return all_rects