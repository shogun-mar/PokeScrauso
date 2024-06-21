import pygame
from os import path
from classes.gameState import GameState
from settings import *

def render_settings_menu(game):
    game.fake_screen.blit(game.settings_background_image, (0,0))
    game.fake_screen.blit(game.save_button, game.save_button_rect)
    game.fake_screen.blit(game.restore_button, game.restore_button_rect)
    game.fake_screen.blit(game.discard_button, game.discard_button_rect)
    game.fake_screen.blit(game.mute_button, game.mute_button_rect) if game.current_volume_status else game.fake_screen.blit(game.unmute_button, game.unmute_button_rect)
    for i in range(len(game.modified_keybinds_images_values)):
        game.fake_screen.blit(game.modified_keybinds_images_values[i], game.settings_menu_images_rects[i])
        game.fake_screen.blit(game.settings_menu_rendered_texts[i], game.settings_menu_rendered_texts_rects[i])

def get_configuration_images(keybinds):
        images = {}  # Dictionary with key names as keys and images as values
        for key, value in keybinds.items():
            #Convert the pygame key constant to its string representation
            key_name = pygame.key.name(value)
            #Construct the file path
            file_path = path.join("graphics", "UI", "menus", "icons", "keys", f"{key_name}.png")
            # Check if the file exists
            if path.isfile(file_path):
                # Load the image and convert it to a format suitable for fast blitting
                image = pygame.image.load(file_path).convert_alpha()
                # Add the image to the dictionary
                images[key] = image
        return images

def handle_settings_input(game, key):
    if game.modyfing_keybind == False:   
        if key == PAUSE_KEY:
            game.game_state = GameState.START_MENU
        elif key == SAVE_SETTINGS_KEY:
            #Salva le impostazioni
            save_configuration()
        elif key == RESTORE_SETTINGS_KEY:
            #Ripristina le impostazioni
            set_default_configuration(game.modified_keybinds)
        elif key == DISCARD_SETTINGS_KEY:
            #Scarta le impostazioni
            #TODO
            print("Scarta le impostazioni") #Placeholder
            #discard_configuration()
        elif key == MUTE_KEY:
            print("Muta il gioco")
            #Muta il gioco
            game.current_volume_status = not game.current_volume_status
    else:
        if key == PAUSE_KEY: # If the user presses the escape key, the process is interrupted
            game.modyfing_keybind = False
            game.modified_keybinds_images_values[game.last_clicked_index].set_alpha(255)
        elif key in ACCEPTABLE_KEYBINDS:
            desired_dict_key = list(game.modified_keybinds.keys())[game.last_clicked_index] # This line gets the key of the dictionary that corresponds to the last clicked index
            game.modified_keybinds_images_values[game.last_clicked_index] = game.key_images[pygame.key.name(key)] # This line updates the image of the keybind at the last clicked index with the new key
            game.modified_keybinds[desired_dict_key] = key # This line updates the dictionary with the new key
            game.modyfing_keybind = False # Correctly setting modifying_keybind to False to indicate the process is complete
                
def handle_settings_input_mouse(game):
    if game.save_button_rect.collidepoint(pygame.mouse.get_pos()):
        #Salva le impostazioni
        save_configuration()
    elif game.restore_button_rect.collidepoint(pygame.mouse.get_pos()):
        #Ripristina le impostazioni
        game.modified_keybinds = set_default_configuration()
    elif game.discard_button_rect.collidepoint(pygame.mouse.get_pos()):
        #Scarta le impostazioni
        #TODO
        print("Scarta le impostazioni") #Placeholder
        #discard_configuration()
    elif game.mute_button_rect.collidepoint(pygame.mouse.get_pos()):
        print("Muta il gioco")
        #Muta il gioco
        game.current_volume_status = not game.current_volume_status
    else:
        for i in range(len(game.settings_menu_images_rects)):
            if game.settings_menu_images_rects[i].collidepoint(pygame.mouse.get_pos()):
                if (game.last_clicked_index is not None and game.last_clicked_index != i) or game.modifying_keybind == False: # Se c'è una Surface precedentemente selezionata, ripristina la sua opacità
                    game.modified_keybinds_images_values[game.last_clicked_index].set_alpha(255)
                game.modified_keybinds_images_values[i].set_alpha(128) # Imposta l'opacità della Surface appena selezionata
                game.last_clicked_index = i # Aggiorna l'indice dell'ultima Surface cliccata
                game.modyfing_keybind = True # Imposta la variabile di stato a True
                break

def render_texts(texts, font, color):
    settings_menu_rendered_texts = []
    for text in texts:
        rendered_text = font.render(text, True, color)
        settings_menu_rendered_texts.append(rendered_text)
    return settings_menu_rendered_texts

def get_settings_menu_texts_rects(game, settings_menu_rendered_texts):
    rects = []
    for i in range(len(settings_menu_rendered_texts)):
        corresponding_midright = game.settings_menu_images_rects[i].midright
        new_midleft = (corresponding_midright[0] + 10, corresponding_midright[1])
        rects.append(settings_menu_rendered_texts[i].get_rect(midleft = new_midleft)) 
    return rects

def get_settings_menu_rects(game, keybind_images):
    rects = []
    for i in range(len(keybind_images)):
        if i%2!=0: x_coord = game.half_w
        else: x_coord = 50 
        if i%2==0: y_coord = i*25 + 50
        rects.append(keybind_images[i].get_rect(topleft = (x_coord, y_coord)))
    return rects