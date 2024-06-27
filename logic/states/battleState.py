import settings
from logic.states.gameState import GameState
from pygame.draw import rect

HEALTH_BAR_WIDTH = 100
HEALTH_BAR_HEIGHT = 7

PLAYER_POKEMON_MAX_HP = None
ENEMY_POKEMON_MAX_HP = None

green = (0, 255, 0)
orange = (255, 165, 0)
red = (255, 0, 0)

def init_battle(game, random_pokemon):
    global PLAYER_POKEMON_MAX_HP, ENEMY_POKEMON_MAX_HP
    game.player_pokemon = game.players.squad[0]
    game.enemy_pokemon = random_pokemon
    PLAYER_POKEMON_MAX_HP = game.player_pokemon.stats['max_hp']
    ENEMY_POKEMON_MAX_HP = game.enemy_pokemon.stats['max_hp']

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
    pass

def render_enemy_pokemon(game):
    pass

def render_ui(game):
    game.fake_screen.blit(game.databox_player, (0, 180)) #Databox del giocatore
    game.fake_screen.blit(game.databox_enemy, (485, 60)) #Databox del nemico
    draw_health_bars(game)

def draw_health_bars(game):
    current_pokemon_player_hp = game.player_pokemon.stats['hp']
    pokemon_player_hp_percentage = current_pokemon_player_hp / PLAYER_POKEMON_MAX_HP
    pokemon_player_hp_bar_width = HEALTH_BAR_WIDTH * pokemon_player_hp_percentage
    pokemon_player_hp_bar_color = get_health_bar_color(pokemon_player_hp_percentage)
    rect(game.fake_screen, pokemon_player_hp_bar_color, (95, 220, pokemon_player_hp_bar_width, HEALTH_BAR_HEIGHT)) #Disegna la barra di vita del proprio pokèmon a schermo
    current_pokemon_enemy_hp = game.enemy_pokemon.stats['hp']
    pokemon_enemy_hp_percentage = current_pokemon_enemy_hp / ENEMY_POKEMON_MAX_HP
    pokemon_enemy_hp_bar_width = HEALTH_BAR_WIDTH * pokemon_enemy_hp_percentage
    pokemon_enemy_hp_bar_color = get_health_bar_color(pokemon_enemy_hp_percentage)
    rect(game.fake_screen, pokemon_enemy_hp_bar_color, (580, 100, pokemon_enemy_hp_bar_width, HEALTH_BAR_HEIGHT)) #Disegna la barra di vita del pokèmon nemico a schermo

def interpolate_color(color1, color2, factor): # Function to interpolate between two colors
        return (
            int(color1[0] + (color2[0] - color1[0]) * factor),
            int(color1[1] + (color2[1] - color1[1]) * factor),
            int(color1[2] + (color2[2] - color1[2]) * factor)
        )

def get_health_bar_color(percentage):
    if percentage > 0.5:
        # Scale factor between 100% and 50% for green to orange
        factor = (percentage - 0.5) / (1 - 0.5)
        return interpolate_color(orange, green, factor)
    elif percentage > 0.25:
        # Scale factor between 50% and 25% for orange to red
        factor = (percentage - 0.25) / (0.5 - 0.25)
        return interpolate_color(red, orange, factor)
    else:
        # Below 25%, it's just red
        return red





