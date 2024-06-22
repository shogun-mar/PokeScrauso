import settings

def handle_name_menu_input(key):
    pass

def render_name_menu(game, simbols_set_index):
    game.fake_screen.blit(game.name_menu_background, (0, 0))
    game.fake_screen.blit(game.name_menu_overlay_tab, (22, 190))
    game.fake_screen.blit(game.name_menu_overlay_controls, (22, 120))
    for i in range(len(game.rendered_name_menu_texts[simbols_set_index])):
        game.fake_screen.blit(game.rendered_name_menu_texts[simbols_set_index][i], game.rendered_name_menu_texts_rects[simbols_set_index][i])
    game.fake_screen.blit(game.name_menu_cursor, game.name_menu_cursor_rect)

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
    start_x = 85
    start_y = 235
    padding_x = 50
    padding_y = 50

    for simbols_set in rendered_texts:
        x_coord = start_x
        y_coord = start_y
        temp_array = []
        for simbol in simbols_set:
            temp_array.append(simbol.get_rect(center=(x_coord, y_coord)))
            if x_coord <= settings.SCREEN_WIDTH - start_x - padding_x:
                x_coord += padding_x
            else:
                x_coord = start_x
                y_coord += padding_y
        all_rects.append(temp_array)

    return all_rects