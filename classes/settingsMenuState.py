import pygame
from os import path
from classes.gameState import GameState
from settings import *

def render_settings_menu(self):
    self.fake_screen.blit(self.settings_background_image, (0,0))
    self.fake_screen.blit(self.save_button, self.save_button_rect)
    self.fake_screen.blit(self.restore_button, self.restore_button_rect)
    self.fake_screen.blit(self.discard_button, self.discard_button_rect)
    self.fake_screen.blit(self.mute_button, self.mute_button_rect) if self.current_volume_status else self.fake_screen.blit(self.unmute_button, self.unmute_button_rect)
    for i in range(len(self.modified_keybinds_images_values)):
        self.fake_screen.blit(self.modified_keybinds_images_values[i], self.settings_menu_images_rects[i])
        self.fake_screen.blit(self.settings_menu_rendered_texts[i], self.settings_menu_rendered_texts_rects[i])

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

def handle_settings_input(self, key):   
    if key == PAUSE_KEY:
        self.game_state = GameState.START_MENU
    elif key == SAVE_SETTINGS_KEY:
        #Salva le impostazioni
        save_configuration()
    elif key == RESTORE_SETTINGS_KEY:
        #Ripristina le impostazioni
        set_default_configuration()
    elif key == DISCARD_SETTINGS_KEY:
        #Scarta le impostazioni
        #TODO
        print("Scarta le impostazioni") #Placeholder
        #discard_configuration()
    elif key == MUTE_KEY:
        print("Muta il gioco")
        #Muta il gioco
        self.current_volume_status = not self.current_volume_status

def handle_settings_input_mouse(self):
    if self.save_button_rect.collidepoint(pygame.mouse.get_pos()):
        #Salva le impostazioni
        save_configuration()
    elif self.restore_button_rect.collidepoint(pygame.mouse.get_pos()):
        #Ripristina le impostazioni
        set_default_configuration()
    elif self.discard_button_rect.collidepoint(pygame.mouse.get_pos()):
        #Scarta le impostazioni
        #TODO
        print("Scarta le impostazioni") #Placeholder
        #discard_configuration()
    elif self.mute_button_rect.collidepoint(pygame.mouse.get_pos()):
        print("Muta il gioco")
        #Muta il gioco
        self.current_volume_status = not self.current_volume_status
    else:
        for i in range(len(self.settings_menu_images_rects)):
            if self.settings_menu_images_rects[i].collidepoint(pygame.mouse.get_pos()):
                clicked_image = self.modified_keybinds_images_values[i]
                clicked_image.set_alpha(128)
                #Cambia il tasto
                #TODO
                print("Cambia il tasto") #Placeholder
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