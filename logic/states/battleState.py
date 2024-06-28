import settings
import pygame
from logic.states.gameState import GameState
from random import randint

PLAYER_POKEMON_MAX_HP = None
ENEMY_POKEMON_MAX_HP = None

player_level_icon_relative_pos = (0, 0)
enemy_level_icon_relative_pos = (0, 0)
player_level_text_relative_pos = (0, 0)
enemy_level_text_relative_pos = (0, 0)

hp_text = None
hp_rect = None

def init_battle(game, random_pokemon):
    pygame.font.init() #Da togliere messo per debugging
    global PLAYER_POKEMON_MAX_HP, ENEMY_POKEMON_MAX_HP, \
    player_level_icon_relative_pos, enemy_level_icon_relative_pos, \
    player_level_text_relative_pos, enemy_level_text_relative_pos, \
    hp_text, hp_text_rect
    game.player_pokemon = random_pokemon[0]
    #game.player_pokemon = game.players.squad[0]
    game.enemy_pokemon = random_pokemon[1]
    game.battle_overlay_command_text = game.battle_command_font.render("What will " + game.player_pokemon.name + " do?", True, (0, 0, 0))
    PLAYER_POKEMON_MAX_HP = game.player_pokemon.stats['max_hp']
    ENEMY_POKEMON_MAX_HP = game.enemy_pokemon.stats['max_hp']
    hp_text = game.battle_ui_font.render(str(game.player_pokemon.stats['hp']) + "/" + str(PLAYER_POKEMON_MAX_HP), True, (0, 0, 0))
    hp_text_rect = hp_text.get_rect(center = (140, 140))
    player_level_icon_relative_pos =  (game.player_pokemon.rendered_name.get_width() + 40, 99)
    enemy_level_icon_relative_pos = (game.enemy_pokemon.rendered_name.get_width() + 520, 75)
    player_level_text_relative_pos = (player_level_icon_relative_pos[0] + 30, player_level_icon_relative_pos[1] + 2) #+2 per centrare il testo
    enemy_level_text_relative_pos = (enemy_level_icon_relative_pos[0] + 30, enemy_level_icon_relative_pos[1] + 2) 

def handle_battle_input(game, key):
    if game.player_interacted_with_dialogue_box == False and key == settings.INTERACTION_KEY and game.beginning_battle_animation_finished == True: #Ultima condizione solamente per evitare che venga soddisfatto l'if prima della fine dell'animazione
        game.player_interacted_with_dialogue_box = True
    elif game.show_end_dialogue == True and key == settings.INTERACTION_KEY:
        game.game_state = GameState.GAMEPLAY
        game.show_end_dialogue = False

def handle_battle_input_mouse(game, mouse_pos):
    if game.player_interacted_with_dialogue_box == True:
        if game.fight_button_rect.collidepoint(mouse_pos):
            if game.player_pokemon.level == game.enemy_pokemon.level:
                hit_probability = 50
            elif game.player_pokemon.level > game.enemy_pokemon.level:
                hit_probability = 75
            else:
                hit_probability = 25
            if randint(1, 100) <= hit_probability:
                print("Hit successful")
                game.enemy_pokemon.stats['hp'] -= 10 #randint(1, 5) * game.player_pokemon.level
                if game.enemy_pokemon.stats['hp'] <= 0:
                    game.show_end_dialogue = True
                else:
                    update_health_bars(game)
        elif game.flee_button_rect.collidepoint(mouse_pos):
            if game.player_pokemon.level == game.enemy_pokemon.level:
                flee_probability = 50
            elif game.player_pokemon.level > game.enemy_pokemon.level:
                flee_probability = 75
            else:
                flee_probability = 25
            if randint(1, 100) <= flee_probability:
                print("Flee successful")
                game.game_state = GameState.GAMEPLAY

def render_battle(game):
    game.fake_screen.blit(game.battle_background, (0, 0))
    render_enemy_pokemon(game)
    if game.beginning_battle_animation_finished == False and game.show_end_dialogue == False: game.fake_screen.blit(game.beginning_battle_animation_image, (25, 244))
    else: 
        render_player_pokemon(game)
        if game.player_interacted_with_dialogue_box == True : render_ui(game)
    draw_dialogue(game)

def render_player_pokemon(game):
    game.fake_screen.blit(game.player_pokemon.sprite_back, (25, 195))

def render_enemy_pokemon(game):
    game.fake_screen.blit(game.enemy_pokemon.sprite_front, (450, 130))

def render_ui(game):
    draw_health_bars(game)
    game.fake_screen.blit(game.databox_player, (0, 84)) #Databox del giocatore
    game.fake_screen.blit(game.databox_enemy, (485, 60)) #Databox del nemico
    game.fake_screen.blit(game.fight_button_surf, game.fight_button_rect)
    game.fake_screen.blit(game.flee_button_surf, game.flee_button_rect)
    draw_pokemon_info(game)

def draw_health_bars(game):
    game.fake_screen.blit(game.player_current_health_bar, game.player_current_health_bar_rect) #Disegna la barra di vita del proprio pokèmon a schermo
    game.fake_screen.blit(game.enemy_current_health_bar, game.enemy_current_health_bar_rect)   #Disegna la barra di vita del pokèmon nemico a schermo

def draw_pokemon_info(game):
    game.fake_screen.blit(game.player_pokemon.rendered_name, (20, 99))
    game.fake_screen.blit(game.enemy_pokemon.rendered_name, (505, 75))
    game.fake_screen.blit(game.battle_level_icon, player_level_icon_relative_pos)
    game.fake_screen.blit(game.battle_level_icon, enemy_level_icon_relative_pos)
    game.fake_screen.blit(game.player_pokemon.level_surf, player_level_text_relative_pos)
    game.fake_screen.blit(game.enemy_pokemon.level_surf, enemy_level_text_relative_pos)
    game.fake_screen.blit(hp_text, hp_text_rect)

def draw_dialogue(game):
    if game.player_interacted_with_dialogue_box == False: 
        game.fake_screen.blit(game.battle_overlay_message_surf, (0, 384))
        game.fake_screen.blit(game.beginning_battle_text_surf, (60, 420))
    else:
        game.fake_screen.blit(game.battle_overlay_command_surf, (0, 384))
        game.fake_screen.blit(game.battle_overlay_command_text, (30, 425))

    if game.show_end_dialogue == True: 
        game.fake_screen.blit(game.battle_overlay_message_surf, (0, 384))
        game.fake_screen.blit(game.end_battle_text_surf, (60, 420))      
        

def update_health_bars(game): #Funzione per "tirare" indietro la barra di vita del giocatore e del nemico
                             #Sposta il rettangolo a sinistra o destra a seconda della barra di vita e della differenza della vita corrente rispetto a quella del pokèmon
                             #Cambia anche il colore della barra di vita a seconda della vita del pokèmon (100%-50% verde, 50%-25% arancione, 25%-0% rosso)
    player_hp_percentage = game.player_pokemon.stats['hp'] / PLAYER_POKEMON_MAX_HP
    if player_hp_percentage > 0.5:
        game.player_current_health_bar = game.player_health_bars[0]
    elif player_hp_percentage > 0.25 and player_hp_percentage <= 0.5:
        game.player_current_health_bar = game.player_health_bars[1]
    else:
        game.player_current_health_bar = game.player_health_bars[2]
    game.player_current_health_bar_rect.width = int(96 * player_hp_percentage)
    game.player_current_health_bar = pygame.transform.scale(game.player_current_health_bar, (int(96 * player_hp_percentage), 8))

    enemy_hp_percentage = game.enemy_pokemon.stats['hp'] / ENEMY_POKEMON_MAX_HP
    if enemy_hp_percentage > 0.5:
        game.enemy_current_health_bar = game.enemy_health_bars[0]
    elif enemy_hp_percentage > 0.25 and enemy_hp_percentage <= 0.5:
        game.enemy_current_health_bar = game.enemy_health_bars[1]
    else:
        game.enemy_current_health_bar = game.enemy_health_bars[2]
    game.enemy_current_health_bar_rect.width = int(96 * enemy_hp_percentage)
    game.enemy_current_health_bar = pygame.transform.scale(game.enemy_current_health_bar, (int(96 * enemy_hp_percentage), 8))
                            