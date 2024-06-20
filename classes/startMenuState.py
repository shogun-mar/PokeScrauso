import pygame
from settings import *
from classes.gameState import GameState

def handle_start_menu_input(game, key):
        if key == INTERACTION_KEY: game.game_state = GameState.GAMEPLAY #Chiude il menu iniziale

def handle_start_menu_input_mouse(game):
    #Controllo interazione con il pulsante
    mouse_pos = pygame.mouse.get_pos()
    if game.new_game_button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]: 
            #Start new game
            #TODO
            game.game_state = GameState.GAMEPLAY

    elif game.load_save_button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            #Load save
            #TODO
            game.game_state = GameState.GAMEPLAY
        
    elif game.settings_button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            #Open settings
            game.game_state = GameState.SETTINGS_MENU

def render_start_menu(game):
    game.fake_screen.blit(game.start_background_image, (0,0))
    game.fake_screen.blit(game.start_text_image, game.start_text_image_rect)
    game.fake_screen.blit(game.new_game_button, game.new_game_button_rect)
    game.fake_screen.blit(game.load_save_button, game.load_save_button_rect)
    game.fake_screen.blit(game.settings_button, game.settings_button_rect)