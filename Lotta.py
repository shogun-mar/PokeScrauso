import pygame
import sys

# Inizializza Pygame
pygame.init()

# Definisci le costanti per lo schermo
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Pokémon Battle Menu" 

# Crea lo schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Carica le immagini dei Pokémon
name_gioc="DITTO"
player_pokemon_img = pygame.image.load('graphics/Gen 4 Pokemon Back/3 HGSS-B.png')
player_pokemon_rect = player_pokemon_img.get_rect(center=(130, 400))
player_riq_img=pygame.image.load('graphics/UI/Battle/databox_normal.png')
player_riq_rect=player_riq_img.get_rect(center=(129,260))


name_enemy="PIKACHU"
enemy_pokemon_img = pygame.image.load('graphics/HGSS/25 HGSS.png ')
enemy_pokemon_rect = enemy_pokemon_img.get_rect(center=(580, 220))
enemy_riq_img=pygame.image.load('graphics/UI/Battle/databox_normal_foe.png')
enemy_riq_rect=enemy_riq_img.get_rect(center=(599,60))

# Carica lo sfondo della battaglia
battle_background = pygame.image.load('graphics/battle/Background_battle.png')

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

font=pygame.font.Font(None,24)

def draw_button(button, text, color):
    
     # Crea una superficie trasparente
    surface = pygame.Surface((button.width, button.height))
    surface.set_alpha(128)  # setta la trasparenza
    surface.fill(color)

    # Disegna il testo del pulsante
    font = pygame.font.Font(None, 32)
    text_surface = font.render(text, True, (255,255,255))
    surface.blit(text_surface, (10, 10))

    # Disegna la superficie sullo schermo
    screen.blit(surface, (button.x, button.y))

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
                print("Mossa 3 selezionata!")
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
    
    
    # Disegna lo sfondo
    screen.blit(battle_background, (0, 0))

    # Disegna i Pokémon
    screen.blit(player_riq_img,player_riq_rect)
    pygame.draw.rect(screen, (0,255,0), (100, 257, 98, 7))
    pygame.draw.rect(screen, (72, 139, 240), (6.5, 290, 192, 6))
    screen.blit(player_pokemon_img,player_pokemon_rect)

    screen.blit(enemy_riq_img,enemy_riq_rect)
    pygame.draw.rect(screen, (0,255,0), (607, 68, 97, 7))
    screen.blit(enemy_pokemon_img,enemy_pokemon_rect)
 #alt+11 = ♂  alt+12 = ♀
    # Disegna i pulsanti
    if not battle_mode and not pokemon_mode and not bag_mode and not run_mode and not health_mode and not pokeballz_mode and not poke1_mode and not poke2_mode and not poke3_mode and not poke4_mode and not poke5_mode and not poke6_mode:
        draw_button(attack_button, 'LOTTA', (104, 4, 4))
        draw_button(bag_button, 'BORSA', (128,69,10))
        draw_button(run_button, 'FUGA', (10, 69, 128))
        draw_button(poke_button, 'POKéMON', (10,128,69))
    elif battle_mode:
        draw_button(move1_button, 'Mossa 1',(71, 82, 99))
        draw_button(move2_button, 'Mossa 2',(71, 82, 99))
        draw_button(move3_button, 'Mossa 3',(71, 82, 99))
        draw_button(move4_button, 'Mossa 4',(71, 82, 99))
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
        draw_button(health_button, 'Rimedio',(71, 82, 99))
        draw_button(pokeballz_button, 'Pokéball',(71, 82, 99))
    #elif health_mode:
        
    #elif pokeballz_mode:
        
    elif run_mode:
        message = "scampato pericolo!! ^.^ "
        panel = font.render(message, True, (0, 0, 0))
        panel_rect = panel.get_rect(center = (400, 360))
        screen.blit(panel, panel_rect)
        
        running=False 
        


 # Disegna nome e livello del Pokémon del giocatore
    
    
    # player_info_text = font.render(f"{name_gioc} Lvl {1000} ", True, (0, 0, 0))
    # screen.blit(player_info_text, (50, 260))
    

    # Disegna nome e livello del Pokémon nemico
    # enemy_info_text = font.render(f"{name_enemy} Lvl {104} ", True, (0, 0, 0))
    # screen.blit(enemy_info_text, (500, 60))
    # pygame.draw.rect(screen, (0,255,0), (500, 80, 104, 10))
    
    pygame.time.Clock().tick(60)

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()
sys.exit()