import pygame
from logic.states.gameState import GameState
import settings

def handle_gameplay_input(game, key):
        if key == settings.MAP_KEY: game.game_state = GameState.MAP #Apre la mappa
        elif key == settings.SQUAD_KEY: game.game_state = GameState.SQUAD_MENU #Apre il menu della squadra
        elif key == settings.INVENTORY_KEY: game.game_state = GameState.INVENTORY #Apre l'inventario
        elif key == settings.POKEDEX_KEY: game.game_state = GameState.POKEDEX #Apre il PokèDex
        elif key == settings.PAUSE_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            game.darkened_surface.blit(game.fake_screen, (0,0))
            game.darkened_surface.set_alpha(128)
            game.game_state = GameState.PAUSE #Apre il menu di pausa
        elif key == settings.HELP_KEY:
            #Prende screenshot dell'attuale schermata di gioco e la oscura
            game.darkened_surface = pygame.Surface(game.fake_screen.get_size())
            game.darkened_surface.blit(game.fake_screen, (0,0))
            game.darkened_surface.set_alpha(128) 
            game.game_state = GameState.HELP_MENU

def render_gameplay(game):
    game.camera_group.custom_draw(game.player)