import pygame
import settings

def handle_name_menu_input(game):
    pass

def render_name_menu(game):
    for i 

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

    del simbols
    del temp_array
    return rendered_texts

def get_name_menu_texts_rects(rendered_texts):
    rects = []
    x_coord = 0

    max_length = max(len(rendered_texts[0]), len(rendered_texts[1]), len(rendered_texts[2])) #Trova la lunghezza massima in modo da avere sempre abbastanza rettangoli per tutte le lettere
    for i in range(max_length):
        rects.append(pygame.Rect(0, 0, 0, 0))

    del rects
    return rects

    