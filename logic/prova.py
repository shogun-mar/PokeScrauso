import pygame
import sys


# Definisci le costanti per lo schermo
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Pokémon Battle Menu" 
HEALTH_BAR_WIDTH=98
HEALTH_BAR_HEIGHT=7
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
font=pygame.font.Font("graphics/fonts/PressStart2P.ttf",12)

# Define battle animation constants
BATTLE_ANIMATION_FRAMES = 10
BATTLE_ANIMATION_SPEED = 3

# Define Pokémon animation constants
POKEMON_ANIMATION_FRAMES = 2
POKEMON_ANIMATION_SPEED = 2

# Define Poké Ball animation constants
POKEBALL_ANIMATION_FRAMES = 18
POKEBALL_ANIMATION_SPEED = 3.65

# Create a dictionary to store the battle animation frames
battle_animation_frames = {}

# Create a dictionary to store the Pokémon animation frames
pokemon_animation_frames = {}

# Create a dictionary to store the Poké Ball animation frames
pokeball_animation_frames = {}

# Load the battle animation frames
for i in range(BATTLE_ANIMATION_FRAMES):
    battle_animation_frame = pygame.image.load(f'graphics/battle_animation/{i}.png')
    battle_animation_frames[i] = battle_animation_frame

# Load the Pokémon animation frames
for i in range(POKEMON_ANIMATION_FRAMES):
    pokemon_animation_frame = pygame.image.load(f'graphics/Gen 4 Pokemon Back/{i}.png')
    pokemon_animation_frames[i] = pokemon_animation_frame

# Load the Poké Ball animation frames
for i in range(POKEBALL_ANIMATION_FRAMES):
    pokeball_animation_frame = pygame.image.load(f'graphics/pokeball_animation/{i}.png')
    pokeball_animation_frames[i] = pokeball_animation_frame

# Initialize the battle animation variables
battle_animation_frame_index = 0
battle_animation_speed = BATTLE_ANIMATION_SPEED

# Initialize the Pokémon animation variables
pokemon_animation_frame_index = 0
pokemon_animation_speed = POKEMON_ANIMATION_SPEED

# Initialize the Poké Ball animation variables
pokeball_animation_frame_index = 0
pokeball_animation_speed = POKEBALL_ANIMATION_SPEED
#stati
battle_mode=False
pokemon_mode = False
bag_mode=False
run_mode=False
health_mode=False
pokeballz_mode=False
poke1_mode=False
poke2_mode=False
poke3_mode=False
poke4_mode=False
poke5_mode=False
poke6_mode=False
running=True
# Main loop
while running:
    #... (rest of the code remains the same until here)

    # Update battle animation
    battle_animation_frame_index += battle_animation_speed
    if battle_animation_frame_index >= BATTLE_ANIMATION_FRAMES:
        battle_animation_frame_index = 0

    # Draw battle animation
    screen.blit(battle_animation_frames[int(battle_animation_frame_index)], (200, 200))

    # Update Pokémon animation
    pokemon_animation_frame_index += pokemon_animation_speed
    if pokemon_animation_frame_index >= POKEMON_ANIMATION_FRAMES:
        pokemon_animation_frame_index = 0

    # Draw Pokémon animation
    screen.blit(pokemon_animation_frames[int(pokemon_animation_frame_index)], (300, 300))

    # Update Poké Ball animation
    pokeball_animation_frame_index += pokeball_animation_speed
    if pokeball_animation_frame_index >= POKEBALL_ANIMATION_FRAMES:
        pokeball_animation_frame_index = 0

    # Draw Poké Ball animation
    screen.blit(pokeball_animation_frames[int(pokeball_animation_frame_index)], (400, 400))

    #... (rest of the code remains the same until here)
pygame.quit()
sys.exit()