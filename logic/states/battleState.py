import settings
from logic.states.gameState import GameState
from pygame.draw import rect

PLAYER_POKEMON_MAX_HP = None
ENEMY_POKEMON_MAX_HP = None

green = (0, 255, 0)
orange = (255, 165, 0)
red = (255, 0, 0)

def init_battle(game, random_pokemon):
    global PLAYER_POKEMON_MAX_HP, ENEMY_POKEMON_MAX_HP
    print("BATTLE INITIALIZING")
    game.player_pokemon = random_pokemon
    #game.player_pokemon = game.players.squad[0]
    game.enemy_pokemon = random_pokemon
    PLAYER_POKEMON_MAX_HP = game.player_pokemon.stats['max_hp']
    ENEMY_POKEMON_MAX_HP = game.enemy_pokemon.stats['max_hp']
    print("BATTLE INITIALIZED")

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
    game.fake_screen.blit(game.player_pokemon.sprite_back, (25, 300))

def render_enemy_pokemon(game):
    game.fake_screen.blit(game.enemy_pokemon.sprite_front, (450, 130))

def render_ui(game):
    draw_health_bars(game)
    game.fake_screen.blit(game.databox_player, (0, 180)) #Databox del giocatore
    game.fake_screen.blit(game.databox_enemy, (485, 60)) #Databox del nemico
    draw_pokemon_info(game)

def draw_health_bars(game):
    game.fake_screen.blit(game.current_player_health_bar, game.current_player_health_bar_rect) #Disegna la barra di vita del proprio pokèmon a schermo
    game.fake_screen.blit(game.current_enemy_health_bar, game.current_enemy_health_bar_rect)#Disegna la barra di vita del pokèmon nemico a schermo

def draw_pokemon_info(game):
    game.fake_screen.blit(game.player_pokemon.battle_name, (20, 195))
    game.fake_screen.blit(game.enemy_pokemon.battle_name, (505, 75))
    game.fake_screen.blit()

def update_health_bar(game): #Funzione per "tirare" indietro la barra di vita del giocatore e del nemico
    pass                     #Sposta il rettangolo a sinistra o destra a seconda della barra di vita e della differenza della vita corrente rispetto a quella del pokèmon
                             #Cambia anche il colore della barra di vita a seconda della vita del pokèmon (100%-50% verde, 50%-25% arancione, 25%-0% rosso)