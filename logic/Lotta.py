import pygame
import sys
import time
import random

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
poke_life = 100 #vita totale del pokemon del giocatore
player_pokemon1_img = pygame.image.load('graphics/Pokemon/Back/PIKACHU.png')
player_pokemon_rect = player_pokemon1_img.get_rect(center=(130, 400))
player_riq_img = pygame.image.load('graphics/UI/Battle/databox_normal.png')
player_riq_rect = player_riq_img.get_rect(center=(129, 260))
player_info_text = font.render(f"{name_gioc} Lvl {16} ", True, (0, 0, 0))
player_sex_img=pygame.image.load('graphics/sex/male.png')
player_sex_rect=player_sex_img.get_rect(center=(200, 240))

name_enemy = "PIKACHU"
enemy_hp = 40
enemy_tot_health = 40
enemy_pokemon_img = pygame.image.load('graphics/Pokemon/Front/PIKACHU.png')
enemy_pokemon_rect = enemy_pokemon_img.get_rect(center=(580, 250))
enemy_riq_img = pygame.image.load('graphics/UI/Battle/databox_normal_foe.png')
enemy_riq_rect = enemy_riq_img.get_rect(center=(599, 60))
enemy_info_text = font.render(f"{name_enemy} Lvl {16} ", True, (0, 0, 0))
enemy_sex_img=pygame.image.load('graphics/sex/female.png')
enemy_sex_rect=enemy_sex_img.get_rect(center=(670, 50))

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

message_img=pygame.image.load('graphics/UI/Battle/overlay_message.png')
message_rect=message_img.get_rect(center=(300,400))
# Definisci i bottoni
attack_button = pygame.Rect(400, 360, 150, 50)
bag_button = pygame.Rect(560, 360, 150, 50)
run_button = pygame.Rect(400, 420, 150, 50)
poke_button = pygame.Rect(560, 420, 150, 50)

move1_button = pygame.Rect(400, 360, 150, 50)
move2_button = pygame.Rect(560, 360, 150, 50)
move3_button = pygame.Rect(400, 420, 150, 50)
move4_button = pygame.Rect(560, 420, 150, 50)

pokemon1_button = pygame.Rect(50,340,200,60)
pokemon2_button = pygame.Rect(260,340,200,60)
pokemon3_button = pygame.Rect(470, 340, 200, 60)
pokemon4_button = pygame.Rect(50, 410, 200, 60)
pokemon5_button = pygame.Rect(260, 410, 200, 60)
pokemon6_button = pygame.Rect(470, 410, 200, 60)

health_button = pygame.Rect(400, 360, 150, 100)
pokeballz_button = pygame.Rect(560, 360, 150, 100)


def draw_button(button, text, color, alpha,image_path,ispokemon):
    surface = pygame.Surface((button.width, button.height))
    # Crea una superficie trasparente se necessario
    if alpha is not None:
        surface.set_alpha(alpha)  # Imposta la trasparenza

    # Riempi la superficie con il colore
    surface.fill(color)

    # Carica e disegna l'immagine sul bottone, se un percorso immagine è fornito
    if image_path is not None:
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image,(70, 50))
        image_rect=image.get_rect(center=(button.width // 8, button.height // 2.75))
        surface.blit(image, image_rect)  # Assicurati di usare topleft per posizionare l'immagine correttamente
    if not ispokemon:
        # Disegna il testo del pulsante
        font = pygame.font.Font("graphics/fonts/PressStart2P.ttf", 12)
        if color != (255, 255, 255):
            text_surface = font.render(text, True, (255, 255, 255))
        else:
            text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(button.width // 2, button.height // 2))  # Centra il testo nel bottone
        surface.blit(text_surface, text_rect.topleft)
    else:
        # Disegna il testo del pulsante
        font = pygame.font.Font("graphics/fonts/PressStart2P.ttf", 12)
        if color != (255, 255, 255):
            text_surface = font.render(text, True, (255, 255, 255))
        else:
            text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(button.width // 1.5, button.height // 4))
        surface.blit(text_surface, text_rect.topleft)
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

# Define enemy actions
enemy_actions = ["Attack","Heal"]

#stati
battle_mode=False
pokemon_mode = False
bag_mode=False
run_mode=False
health_mode=False
pokeballz_mode=False
move1_mode=False
mov2_mode=False
mov3_mode=False
mov4_mode=False
poke1_mode=False
poke2_mode=False
poke3_mode=False
poke4_mode=False
poke5_mode=False
poke6_mode=False
running=True
pokemon_drawn = False
pokeball_drawn=False
player_turn=True


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
                move1_mode=True
            elif move2_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 2 selezionata!")
                mov2_mode=True
            elif move3_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 3selezionata!")
                mov3_mode=True
            elif move4_button.collidepoint(event.pos) and battle_mode:
                print("Mossa 4 selezionata!")
                mov4_mode=True
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
    
    screen.blit(player_pokemon1_img, player_pokemon_rect)
       

    screen.blit(player_riq_img,player_riq_rect)
    screen.blit(player_sex_img,player_sex_rect)
        
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
    screen.blit(player_info_text, (10, 238))
    screen.blit(player_life,(104,272))
        
    #alt+11 = ♂  alt+12 = ♀
        # Disegna i pulsanti
    if player_turn and not battle_mode and not pokemon_mode and not bag_mode and not run_mode and not health_mode and not pokeballz_mode and not poke1_mode and not poke2_mode and not poke3_mode and not poke4_mode and not poke5_mode and not poke6_mode:
        draw_button(attack_button, 'FIGHT', (104, 4, 4),128,None,False)
        draw_button(bag_button, 'BAG', (128,69,10),128,None,False)
        draw_button(run_button, 'RUN', (10, 69, 128),128,None,False)
        draw_button(poke_button, 'POKéMON', (10,128,69),128,None,False)
    elif battle_mode:
        draw_button(move1_button, 'Move 1',(71, 82, 99),128,None,False)
        draw_button(move2_button,'Move 2',(71, 82, 99),128,None,False)
        draw_button(move3_button, 'Move 3',(71, 82, 99),128,None,False)
        draw_button(move4_button, 'Move 4',(71, 82, 99),128,None,False)
        if move1_mode:
            message = "Pikachu usa Tuono!"
            text = font.render(message, True, (0, 0, 0))
            text_rect = text.get_rect(center=(200, 400))
            screen.blit(message_img, message_rect)
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(500)  # Riduci il tempo di attesa per rendere l'animazione più fluida

            # Muovi il Pokémon del giocatore in avanti
            player_pokemon_rect.x -= 20  # Assumi che player_pokemon_rect sia il rettangolo che delimita il Pokémon del giocatore
            screen.blit(player_pokemon1_img, player_pokemon_rect)  # Assumi che player_pokemon_img sia l'immagine del Pokémon del giocatore
            # Scurisci il Pokémon nemico
            enemy_pokemon_img.set_alpha(100)  # Assumi che 100 renda l'immagine visibilmente più scura
            screen.blit(enemy_pokemon_img, enemy_pokemon_rect)  # Ridisegna con l'alpha ridotto
            pygame.display.flip()
            pygame.time.wait(200)

            # Ripristina lo stato originale
            player_pokemon_rect.x += 20  # Muovi il Pokémon del giocatore indietro
            enemy_pokemon_img.set_alpha(255)  # Ripristina l'alpha dell'immagine del Pokémon nemico
            # Qui dovresti ridisegnare lo sfondo, il Pokémon del giocatore e il Pokémon nemico per ripristinare completamente la scena
            screen.blit(battle_background, (0,0))  # Assumi che tu abbia un'immagine di sfondo da ridisegnare
            screen.blit(player_pokemon1_img, player_pokemon_rect)
            screen.blit(enemy_pokemon_img, enemy_pokemon_rect)
            pygame.display.flip()
            pygame.time.wait(500)

            enemy_hp-=10
            move1_mode=False
            battle_mode=False
            player_turn=False
        elif mov2_mode:
            message = "Pikachu usa Tuono!"
            text=font.render(message,True,(0,0,0))
            text_rect=text.get_rect(center=(200,400))
            screen.blit(message_img,message_rect)
            screen.blit(text,text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            enemy_hp-=20
            mov2_mode=False
            battle_mode=False
            player_turn=False
        elif mov3_mode:
            message = "Pikachu usa Fulmine!"
            text=font.render(message,True,(0,0,0))
            text_rect=text.get_rect(center=(200,400))
            screen.blit(message_img,message_rect)
            screen.blit(text,text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            enemy_hp-=30
            mov3_mode=False
            battle_mode=False
            player_turn=False
        elif mov4_mode:
            message = "Pikachu usa Fulmine!"
            text=font.render(message,True,(0,0,0))
            text_rect=text.get_rect(center=(200,400))
            screen.blit(message_img,message_rect)
            screen.blit(text,text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            enemy_hp-=40
            mov4_mode=False
            battle_mode=False
            player_turn=False
    
    elif pokemon_mode:
        draw_button(pokemon1_button, f"{name_gioc}",(128, 126, 124),None,'graphics/Gen 1-6 Icons/26.png',True)
        draw_button(pokemon2_button, "Ditto",(128, 126, 124),None,'graphics/Gen 1-6 Icons/4.png',True)
        draw_button(pokemon3_button, "Charmender",(128, 126, 124),None,'graphics/Gen 1-6 Icons/292.png',True)
        draw_button(pokemon4_button, "Infernape",(128, 126, 124),None,'graphics/Gen 1-6 Icons/650.png',True)
        draw_button(pokemon5_button, "Pichu",(128, 126, 124),None,'graphics/Gen 1-6 Icons/500.png',True)
        draw_button(pokemon6_button, "Oshawott",(128, 126, 124),None,'graphics/Gen 1-6 Icons/104.png',True)
        
        if poke1_mode:
            messages = [f"{name_gioc} è il momento di rientrare...", "Pietro I choose you!"]
            initial_y = 380  # Posizione Y iniziale per il primo messaggio
            screen.blit(message_img,message_rect)
            for i, message in enumerate(messages):
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(290, initial_y + (i * 20)))
                screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            poke1_mode=False
            pokemon_mode=False
            player_turn=False

        elif poke2_mode:
            messages = [f"{name_gioc} è il momento di rientrare...", "Pietro I choose you!"]
            initial_y = 380  # Posizione Y iniziale per il primo messaggio
            screen.blit(message_img,message_rect)
            for i, message in enumerate(messages):
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(290, initial_y + (i * 20)))
                screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            poke2_mode=False
            pokemon_mode=False
            player_turn=False
        
        elif poke3_mode:
            messages = [f"{name_gioc} è il momento di rientrare...", "Pietro I choose you!"]
            initial_y = 380  # Posizione Y iniziale per il primo messaggio
            screen.blit(message_img,message_rect)
            for i, message in enumerate(messages):
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(290, initial_y + (i * 20)))
                screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            poke3_mode=False
            pokemon_mode=False
            player_turn=False
        
        elif poke4_mode:
            messages = [f"{name_gioc} è il momento di rientrare...", "Pietro I choose you!"]
            initial_y = 380  # Posizione Y iniziale per il primo messaggio
            screen.blit(message_img,message_rect)
            for i, message in enumerate(messages):
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(290, initial_y + (i * 20)))
                screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            poke4_mode=False
            pokemon_mode=False
            player_turn=False
        
        elif poke5_mode:
            messages = [f"{name_gioc} è il momento di rientrare...", "Pietro I choose you!"]
            initial_y = 380  # Posizione Y iniziale per il primo messaggio
            screen.blit(message_img,message_rect)
            for i, message in enumerate(messages):
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(290, initial_y + (i * 20)))
                screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            poke5_mode=False
            pokemon_mode=False
            player_turn=False
        
        elif poke6_mode:
            messages = [f"{name_gioc} è il momento di rientrare...", "Pietro I choose you!"]
            initial_y = 380  # Posizione Y iniziale per il primo messaggio
            screen.blit(message_img,message_rect)
            for i, message in enumerate(messages):
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(290, initial_y + (i * 20)))
                screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            poke6_mode=False
            pokemon_mode=False
            player_turn=False
        
    elif bag_mode:
        draw_button(health_button, 'Health',(71, 82, 99),128,None,False)
        draw_button(pokeballz_button, 'Pokéball',(71, 82, 99),128,None,False)

        if health_mode:
            message = "Pikachu usa Pozione!"
            text=font.render(message,True,(0,0,0))
            text_rect=text.get_rect(center=(200,400))
            screen.blit(message_img,message_rect)
            screen.blit(text,text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            if life_point<poke_life:
            # Heal enemy
                life_point+=20
            
            health_mode=False
            player_turn=False
            bag_mode=False
        
        elif pokeballz_mode:
            message = "Pikachu usa Pokéball!"
            text=font.render(message,True,(0,0,0))
            text_rect=text.get_rect(center=(200,400))
            screen.blit(message_img,message_rect)
            screen.blit(text,text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            pokeballz_mode=False
            player_turn=False
            bag_mode=False
        
    elif run_mode:
        message = "danger escaped!! ^.^ "
        text=font.render(message,True,(0,0,0))
        text_rect=text.get_rect(center=(200,400))
        screen.blit(message_img,message_rect)
        screen.blit(text,text_rect)
        running=False 
    
    elif not player_turn:    
        enemy_action = random.choice(enemy_actions)
        if enemy_action == "Attack":
            enemy_moves=random.randint(1,4)
            if enemy_moves==1:
                message = "Enemy Pikachu attacks!"
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(200, 400))
                screen.blit(message_img, message_rect)
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(500)

                # Deal damage to player
                life_point -= 10
            elif enemy_moves==2:
                message = "Enemy Pikachu attacks!"
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(200, 400))
                screen.blit(message_img, message_rect)
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(500)

                # Deal damage to player
                life_point -= 20
            elif enemy_moves==3:
                message = "Enemy Pikachu attacks!"
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(200, 400))
                screen.blit(message_img, message_rect)
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(500)

                # Deal damage to player
                life_point -= 30
            elif enemy_moves==4:
                message = "Enemy Pikachu attacks!"
                text = font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=(200, 400))
                screen.blit(message_img, message_rect)
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(500)

                # Deal damage to player
                life_point -= 40
        
        elif enemy_action == "Heal":
            message = "Enemy Pikachu heals!"
            text = font.render(message, True, (0, 0, 0))
            text_rect = text.get_rect(center=(200, 400))
            screen.blit(message_img, message_rect)
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(500)
            if enemy_hp<enemy_tot_health:
            # Heal enemy
                enemy_hp += 10
            
        player_turn=True

    #pygame.draw.rect(screen, (0,255,0), (607, 68, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    screen.blit(enemy_pokemon_img,enemy_pokemon_rect)
    screen.blit(enemy_riq_img,enemy_riq_rect)
    screen.blit(enemy_info_text, (490, 44))
    screen.blit(enemy_sex_img,enemy_sex_rect)
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

    pygame.display.flip()
    
    #life_point -= 1
    #enemy_hp-=1
    if enemy_hp<=0:
        #life_point = 0
        message = f"{name_enemy} DEATH X_X"
        text=font.render(message,True,(0,0,0))
        text_rect=text.get_rect(center=(200,400))
        screen.blit(message_img,message_rect)
        screen.blit(text,text_rect)
        running = False
        pygame.display.flip()
    elif life_point<=0:
        message = f"{name_gioc} DEATH X_X"
        text=font.render(message,True,(0,0,0))
        text_rect=text.get_rect(center=(200,400))
        screen.blit(message_img,message_rect)
        screen.blit(text,text_rect)
        running = False
        pygame.display.flip()


pygame.time.delay(1000)
pygame.quit()
sys.exit()