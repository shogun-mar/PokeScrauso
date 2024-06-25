import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Define screen constants
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Pokémon Battle Menu"
HEALTH_BAR_WIDTH = 98
HEALTH_BAR_HEIGHT = 7
TRAINER_IMAGE_DELAY = 0.1  # Delay between trainer images in seconds

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
font = pygame.font.Font("graphics/fonts/PressStart2P.ttf", 12)

# Load Pokémon images
name_gioc = "PIKACHU"
life_point = 100
poke_life = 100
player_pokemon_img = pygame.image.load('graphics/Pokemon/Back/PIKACHU.png')
player_pokemon_rect = player_pokemon_img.get_rect(center=(130, 400))
player_riq_img = pygame.image.load('graphics/UI/Battle/databox_normal.png')
player_riq_rect = player_riq_img.get_rect(center=(129, 260))
player_info_text = font.render(f"{name_gioc} Lvl {1000} ", True, (0, 0, 0))

name_enemy = "PIKACHU"
enemy_hp = 40
enemy_tot_health = 40
enemy_pokemon_img = pygame.image.load('graphics/Pokemon/Front/PIKACHU.png')
enemy_pokemon_rect = enemy_pokemon_img.get_rect(center=(580, 250))
enemy_riq_img = pygame.image.load('graphics/UI/Battle/databox_normal_foe.png')
enemy_riq_rect = enemy_riq_img.get_rect(center=(599, 60))
enemy_info_text = font.render(f"{name_enemy} Lvl {104} ", True, (0, 0, 0))

# Load battle background
battle_background = pygame.image.load('graphics/battle/Background_battle.png')
pokeball_images = []
for i in range(18):
    pokeball_image = pygame.image.load(f'graphics/Gen 3 Pinball Pokeballs/Gen3 Pinball Pokeballs {i}.png')
    pokeball_images.append(pokeball_image)

pygame.mixer.init()
pokemon_cry = pygame.mixer.Sound('sounds/cries/26.ogg')
pokeball_x = 200
pokeball_y = 300
pokeball_animation_speed = 3.65
pokeball_frame = 0
pokeball_index = 2
pokemon_animation_speed = 2
pokemon_frame = 0
pokemon_index = 0

trainer_images=[]
trainer_img=pygame.image.load('graphics/battle/FRLG Trainer Backs 01.png')
trainer_images.append(trainer_img)
trainer_img=pygame.image.load('graphics/battle/FRLG Trainer Backs 04.png')
trainer_images.append(trainer_img)
trainer_img=pygame.image.load('graphics/battle/FRLG Trainer Backs 05.png')
trainer_images.append(trainer_img)
trainer_index=0
trainer_image_counter = 0
trainer_image_timer = time.time()


# Definisci i bottoni
attack_button = pygame.Rect(400, 360, 150, 50)
bag_button = pygame.Rect(560, 360, 150, 50)
run_button = pygame.Rect(400, 420, 150, 50)
poke_button = pygame.Rect(560, 420, 150, 50)

move1_button = pygame.Rect(400, 360, 150, 50)
move2_button = pygame.Rect(560, 360, 150, 50)
move3_button = pygame.Rect(400, 420, 150, 50)
move4_button = pygame.Rect(560, 420, 150, 50)

pokemon1_button = pygame.Rect(250,360,150,50)
pokemon2_button = pygame.Rect(410,360,150,50)
pokemon3_button = pygame.Rect(570, 360, 150, 50)
pokemon4_button = pygame.Rect(250, 420, 150, 50)
pokemon5_button = pygame.Rect(410, 420, 150, 50)
pokemon6_button = pygame.Rect(570, 420, 150, 50)

health_button = pygame.Rect(400, 360, 150, 100)
pokeballz_button = pygame.Rect(560, 360, 150, 100)



def draw_button(button, text, color):
    
     # Crea una superficie trasparente
    surface = pygame.Surface((button.width, button.height))
    surface.set_alpha(128)  # setta la trasparenza
    surface.fill(color)

    # Disegna il testo del pulsante
    font = pygame.font.Font("graphics/fonts/PressStart2P.ttf",12)
    text_surface = font.render(text, True, (255,255,255))
    surface.blit(text_surface, (10, 10))

    # Disegna la superficie sullo schermo
    screen.blit(surface, (button.x, button.y))

wild_pokemon_enter_frame = 0
wild_pokemon_max_frames = 30  # Numero di frame per l'animazione di entrata
wild_pokemon_position = enemy_pokemon_img.get_rect(midbottom=(SCREEN_WIDTH + 100, battle_background.get_rect().y))  # Posizione iniziale fuori dallo schermo

# Funzione per l'animazione di entrata del Pokémon selvatico
def animate_wild_pokemon_entrance():
    global wild_pokemon_enter_frame, wild_pokemon_position
    if wild_pokemon_enter_frame < wild_pokemon_max_frames:
        # Calcola la nuova posizione per creare un effetto di movimento
        wild_pokemon_position.x -= (SCREEN_WIDTH + 100) / wild_pokemon_max_frames
        screen.blit(enemy_pokemon_img, wild_pokemon_position)
        wild_pokemon_enter_frame += 1
    else:
        # L'animazione è finita, il Pokémon selvatico è pronto per la battaglia
        screen.blit(enemy_pokemon_img, wild_pokemon_position)


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
pokemon_drawn = False
pokeball_drawn=False





# Main loop
while running:
    #ciclo eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if attack_button.collidepoint(event.pos) and not battle_mode and not pokemon_mode:
                battle_mode = True
            elif move1_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 1 selezionata!")
            elif move2_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 2 selezionata!")
            elif move3_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 3selezionata!")
            elif move4_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 4 selezionata!")
            elif poke_button.collidepoint(event.pos) and not pokemon_mode and not battle_mode and not bag_mode and not run_mode:
                pokemon_mode = True
            elif pokemon1_button.collidepoint(event.pos) and pokemon_mode:
                print("Pokémon 1 selezionato!")
                poke1_mode=True
            elif pokemon2_button.collidepoint(event.pos) and pokemon_mode:
                print("Pokémon 2 selezionato!")
                poke2_mode=True
            elif pokemon3_button.collidepoint(event.pos) and pokemon_mode:
                print("Pokémon 3 selezionato!")
                poke3_mode=True
            elif pokemon4_button.collidepoint(event.pos) and pokemon_mode:
                print("Pokémon 4 selezionato!")
                poke4_mode=True
            elif pokemon5_button.collidepoint(event.pos) and pokemon_mode:
                print("Pokémon 5 selezionato!")
                poke5_mode=True
            elif pokemon6_button.collidepoint(event.pos) and pokemon_mode:
                print("Pokémon 6 selezionato!")
                poke6_mode=True
                
            elif bag_button.collidepoint(event.pos) and not bag_mode and not pokemon_mode and not battle_mode and not run_mode:
                bag_mode = True
            elif health_button.collidepoint(event.pos) and bag_mode:
                print("Rimedio selezionato!")
                health_mode=True
            elif pokeballz_button.collidepoint(event.pos) and bag_mode:
                print("Pokéball selezionata!")
                pokeballz_mode=True
            elif run_button.collidepoint(event.pos) and not run_mode and not pokemon_mode and not battle_mode and not bag_mode :
                print("fuga")
                
                run_mode=True
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            battle_mode=False
            pokemon_mode=False
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

    player_life=font.render(f"{life_point}/{poke_life}", True,(0,0,0))
    # Disegna lo sfondo
    screen.blit(battle_background, (0, 0))
    if not pokemon_drawn:
    # Update trainer animation
        if not pokeball_drawn:
            if trainer_index >= len(trainer_images):
                trainer_index = 0

            # Display trainer image with delay
            if time.time() - trainer_image_timer > TRAINER_IMAGE_DELAY:
                trainer_image_counter += 1
                trainer_image_timer = time.time()
                if trainer_image_counter >= len(trainer_images):
                    trainer_image_counter = 0
                    pokeball_drawn = True

            # Draw trainer
            screen.blit(trainer_images[trainer_image_counter], (100, 300))
        # Update Poké Ball animation
            pokeball_x += pokeball_animation_speed
            if pokeball_x > 250:
                pokeball_animation_speed = -pokeball_animation_speed
            if pokeball_x < 200:
                pokeball_animation_speed =-pokeball_animation_speed

    # Dopo l'animazione del trainer e della Poké Ball, inizia l'animazione del Pokémon selvatico
    if pokeball_drawn and not pokemon_drawn:
        animate_wild_pokemon_entrance()
        # Draw Poké Ball
        screen.blit(pokeball_images[pokeball_frame], (pokeball_x, pokeball_y))
    if pokeball_index == len(pokeball_images) - 1:
        # Update Pokémon animation
        pokemon_frame += 1
        if pokemon_frame >= player_pokemon_img.get_width():
            pokemon_frame = 0

        
        

    # Draw Pokémon
    if pokeball_index == len(pokeball_images) - 1:
    
        screen.blit(player_pokemon_img, player_pokemon_rect)
        pokemon_drawn=True
# Update indices
    pokeball_index += 1
    if pokeball_index >= len(pokeball_images):
        pokeball_index = 0

    pokemon_index += 1
    if pokemon_index >= player_pokemon_img.get_width():
        pokemon_index = 0

# Suona il verso del Pokémon
    if pokeball_index == len(pokeball_images) - 1:
        pokemon_cry.play()
    
    #screen.blit(player_pokemon_img, player_pokemon_rect)
    screen.blit(player_riq_img,player_riq_rect)
        
    health_bar_color_gioc = (0,255,0)
    if (life_point/poke_life)*100< 50:
        health_bar_color_gioc = (255, 128, 0)  # arancione
    if (life_point/poke_life)*100< 20:
        health_bar_color_gioc = (255,0,0)

    health_bar_surface_gioc = pygame.Surface((HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    health_bar_surface_gioc.fill(health_bar_color_gioc)
    health_bar_surface_gioc.fill((0,0,0), (0, 0, HEALTH_BAR_WIDTH - (life_point / poke_life) * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    screen.blit(health_bar_surface_gioc, (100, 257))

    pygame.draw.rect(screen, (72, 139, 240), (6.5, 290, 192, 6))
    #screen.blit(player_pokemon_img,player_pokemon_rect)
    screen.blit(player_info_text, (50, 238))
    screen.blit(player_life,(104,272))
        
    #alt+11 = ♂  alt+12 = ♀
        # Disegna i pulsanti
    if not battle_mode and not pokemon_mode and not bag_mode and not run_mode and not health_mode and not pokeballz_mode and not poke1_mode and not poke2_mode and not poke3_mode and not poke4_mode and not poke5_mode and not poke6_mode:
        draw_button(attack_button, 'FIGHT', (104, 4, 4))
        draw_button(bag_button, 'BAG', (128,69,10))
        draw_button(run_button, 'RUN', (10, 69, 128))
        draw_button(poke_button, 'POKéMON', (10,128,69))
    elif battle_mode:
        draw_button(move1_button, 'Move 1',(71, 82, 99))
        draw_button(move2_button,'Move 2',(71, 82, 99))
        draw_button(move3_button, 'Move 3',(71, 82, 99))
        draw_button(move4_button, 'Move 4',(71, 82, 99))
    elif pokemon_mode:
        draw_button(pokemon1_button, 'Pokémon 1',(71, 82, 99))
        draw_button(pokemon2_button, 'Pokémon 2',(71, 82, 99))
        draw_button(pokemon3_button, 'Pokémon 3',(71, 82, 99))
        draw_button(pokemon4_button, 'Pokémon 4',(71, 82, 99))
        draw_button(pokemon5_button, 'Pokémon 5',(71, 82, 99))
        draw_button(pokemon6_button, 'Pokémon 6',(71, 82, 99))
    elif poke1_mode:
        message = f"{name_gioc} è il momento di rientrare...  \n Pietro scelgote!"
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
    elif poke2_mode:
        message = f"{name_gioc} è il momento di rientrare... \n  Pietro scelgote!"
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
    elif poke3_mode:
        message = f"{name_gioc} è il momento di rientrare... \n Pietro scelgote!"
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
    elif poke4_mode:
        message = f"{name_gioc} è il momento di rientrare... \n Pietro scelgote!"
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
    elif poke5_mode:
        message = f"{name_gioc} è il momento di rientrare...  \n Pietro scelgote!"
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
    elif poke6_mode:
        message = f"{name_gioc} è il momento di rientrare... \n Pietro scelgote!"
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
    elif bag_mode:
        draw_button(health_button, 'Health',(71, 82, 99))
        draw_button(pokeballz_button, 'Pokéball',(71, 82, 99))
    #elif health_mode:
        
    #elif pokeballz_mode:
        
    elif run_mode:
        message = "scampato pericolo!! ^.^ "
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
        
        running=False 
            
    screen.blit(enemy_riq_img,enemy_riq_rect)
    #pygame.draw.rect(screen, (0,255,0), (607, 68, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    screen.blit(enemy_pokemon_img,enemy_pokemon_rect)
    screen.blit(enemy_info_text, (500, 44))
    health_bar_color_enemy = (0,255,0)
    if (enemy_hp/enemy_tot_health)*100< 50:
        health_bar_color_enemy = (255, 128, 0)  # arancione
    if (enemy_hp/enemy_tot_health)*100< 25:
        health_bar_color_enemy = (255,0,0)

    health_bar_surface_enemy = pygame.Surface((HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    health_bar_surface_enemy.fill(health_bar_color_enemy)
    health_bar_surface_enemy.fill((0,0,0), (0, 0, HEALTH_BAR_WIDTH - (enemy_hp /enemy_tot_health) * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    screen.blit(health_bar_surface_enemy, (607, 68))


    pygame.time.Clock().tick(10)

    pygame.display.update()
    
    #life_point -= 1
    #enemy_hp-=1
    if life_point <=0 or enemy_hp<=0:
        #life_point = 0
        message = "DEATH X_X"
        panel = font.render(message, True, (0, 0, 0))
        
        
        screen.fill((255,255,255),(400,360,310,120))
        screen.blit(panel, (400, 360,300,100))
        running = False
        pygame.display.update()
    


pygame.time.delay(1000)
pygame.quit()
sys.exit()