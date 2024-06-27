import settings
import pygame
from logic.states.gameState import GameState

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
    game.player_pokemon = random_pokemon
    #game.player_pokemon = game.players.squad[0]
    game.enemy_pokemon = random_pokemon
    PLAYER_POKEMON_MAX_HP = game.player_pokemon.stats['max_hp']
    ENEMY_POKEMON_MAX_HP = game.enemy_pokemon.stats['max_hp']
    hp_text = game.battle_font.render(str(game.player_pokemon.stats['hp']) + "/" + str(PLAYER_POKEMON_MAX_HP), True, (0, 0, 0))
    hp_text_rect = hp_text.get_rect(center = (140, 236))
    player_level_icon_relative_pos =  (game.player_pokemon.rendered_name.get_width() + 40, 195)
    enemy_level_icon_relative_pos = (game.enemy_pokemon.rendered_name.get_width() + 520, 75)
    player_level_text_relative_pos = (player_level_icon_relative_pos[0] + 30, player_level_icon_relative_pos[1] + 2) #+2 per centrare il testo
    enemy_level_text_relative_pos = (enemy_level_icon_relative_pos[0] + 30, enemy_level_icon_relative_pos[1] + 2) 

def handle_battle_input(game, key):
    pass

def handle_battle_input_mouse(game, mouse_pos):
    pass

def render_battle(game):
    game.fake_screen.blit(game.battle_background, (0, 0))
    render_enemy_pokemon(game)
    if game.beginning_battle_animation_finished == False: game.fake_screen.blit(game.beginning_battle_animation_image, (25, 340))
    else: 
        render_player_pokemon(game)
        render_ui(game)

def render_player_pokemon(game):
    game.fake_screen.blit(game.player_pokemon.sprite_back, (25, 280))

def render_enemy_pokemon(game):
    game.fake_screen.blit(game.enemy_pokemon.sprite_front, (450, 130))

def render_ui(game):
    draw_health_bars(game)
    game.fake_screen.blit(game.databox_player, (0, 180)) #Databox del giocatore
    game.fake_screen.blit(game.databox_enemy, (485, 60)) #Databox del nemico
    draw_pokemon_info(game)

def draw_health_bars(game):
    game.fake_screen.blit(game.player_current_health_bar, game.player_current_health_bar_rect) #Disegna la barra di vita del proprio pokèmon a schermo
    game.fake_screen.blit(game.enemy_current_health_bar, game.enemy_current_health_bar_rect)   #Disegna la barra di vita del pokèmon nemico a schermo

def draw_pokemon_info(game):
    game.fake_screen.blit(game.player_pokemon.rendered_name, (20, 195))
    game.fake_screen.blit(game.enemy_pokemon.rendered_name, (505, 75))
    game.fake_screen.blit(game.battle_level_icon, player_level_icon_relative_pos)
    game.fake_screen.blit(game.battle_level_icon, enemy_level_icon_relative_pos)
    game.fake_screen.blit(game.player_pokemon.level_surf, player_level_text_relative_pos)
    game.fake_screen.blit(game.enemy_pokemon.level_surf, enemy_level_text_relative_pos)
    game.fake_screen.blit(hp_text, hp_text_rect)

def update_health_bar(game): #Funzione per "tirare" indietro la barra di vita del giocatore e del nemico
    pass                     #Sposta il rettangolo a sinistra o destra a seconda della barra di vita e della differenza della vita corrente rispetto a quella del pokèmon
                             #Cambia anche il colore della barra di vita a seconda della vita del pokèmon (100%-50% verde, 50%-25% arancione, 25%-0% rosso)