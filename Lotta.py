import pygame
import sys
class Button:
    def __init__(self, x, y, width, height, color, text=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.disabled=False

while True:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
        def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.text:
            font = pygame.font.Font(None, 32)
            text_surface = font.render(self.text, True, (255, 255, 255))
            win.blit(text_surface, (self.x + (self.width - text_surface.get_width()) / 2,
                                    self.y + (self.height - text_surface.get_height()) / 2))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False
    def is_disable(self):
        return self.disabled
    def set_disable(self):
        self.disabled=not self.disabled

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((720, 480))
font=pygame.font.Font(None,24)
color=pygame.color.Color(180, 40, 69, 255)
current_screen="main"

background_battle=pygame.image.load('graphics/battle/Background_battle.png')
#pokemon giocatore
name_gioc=""#Pokemon.name
player_pokemon_img=pygame.image.load('graphics/Gen 4 Pokemon Back/3 HGSS-B.png')
player_pokemon_rect = player_pokemon_img.get_rect(center=(130, 400))

#pokemon nemico
name_enemy=""#Pokemon.name
enemy_pokemon_img=pygame.image.load('graphics/HGSS/25 HGSS.png ')
enemy_pokemon_rect = enemy_pokemon_img.get_rect(center=(580, 220))
# Definisci i bottoni

attack_button = Button(400, 360, 150, 50, color, "Attacco")
bag_button = Button(560, 360, 150, 50, color, "Borsa")
run_button = Button(400, 420, 150, 50, color, "Fuga")
poke_button = Button(560, 420, 150, 50, color, "Pokémon")

mov1_button=Button(400, 360, 150, 50, color, "Azione")
mov2_button=Button(560, 360, 150, 50, color, "FogliaErba")
mov3_button=Button(400, 420, 150, 50, color, "smerda")
mov4_button=Button(560, 420, 150, 50, color, "Fuma")

rim_button=Button(400, 360, 150, 100, color, "Rimedi")
pokeballs_button=Button(560, 360, 150, 100, color, "Pokéball")

pokemon1_button=Button(330,360,120,50,color,"Pokémon 1")
pokemon2_button=Button(460,360,120,50,color,"Pokémon 2")
pokemon3_button=Button(590,360,120,50,color,"Pokémon 3")
pokemon4_button=Button(330,420,120,50,color,"Pokémon 4")
pokemon5_button=Button(460,420,120,50,color,"Pokémon 5")
pokemon6_button=Button(590,420,120,50,color,"Pokémon 6")



running=True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running=False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if attack_button.is_over(pos):
                print("Attacco")
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                current_screen = "attack"
                
            elif bag_button.is_over(pos):
                print("Borsa")
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                current_screen = "bag"
                
            elif run_button.is_over(pos):
                print("Fuga")
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                current_screen = "run"
                
            elif poke_button.is_over(pos):
                print("Pokémon")
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                current_screen = "poke"
                
            if mov1_button.is_over(pos) and not mov1_button.is_disable():
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                selected_move = "Azione" #Pokemon.moves1
                current_screen = "move_selected"
            elif mov2_button.is_over(pos) and not mov2_button.is_disable():
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                selected_move = "FogliaErba" #Pokemon.moves2
                current_screen = "move_selected"
            elif mov3_button.is_over(pos) and not mov3_button.is_disable():
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                selected_move = "Smerda" #Pokemon.moves3
                current_screen = "move_selected"
            elif mov4_button.is_over(pos) and not mov4_button.is_disable():
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
                selected_move = "Fuma" #Pokemon.moves4
                current_screen = "move_selected"
            elif rim_button.is_over(pos)  and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Rimedi"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
            elif pokeballs_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokéball"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
            elif pokemon1_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokémon 1"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
            elif pokemon2_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokémon 2"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
            elif pokemon3_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokémon 3"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
            elif pokemon4_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokémon 4"
                """ mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable() """
            elif pokemon5_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokémon 5"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()
            elif pokemon6_button.is_over(pos) and(not mov1_button.is_disable() and not mov2_button.is_disable() and not mov3_button.is_disable() and not mov4_button.is_disable()):
                current_screen="Pokémon 6"
                mov1_button.set_disable()
                mov2_button.set_disable()
                mov3_button.set_disable()
                mov4_button.set_disable()

            
            

    screen.blit(background_battle,(0,0))
    screen.blit(player_pokemon_img,player_pokemon_rect)
    screen.blit(enemy_pokemon_img,enemy_pokemon_rect)
    
    

    player_info_text = font.render(f"{name_gioc} Lvl {1000}", True, (0, 0, 0))
    screen.blit(player_info_text, (50, 280))
    pygame.draw.rect(screen, (0,255,0), (50, 300, 100, 10))

    # Disegna nome e livello del Pokémon nemico
    enemy_info_text = font.render(f"{name_enemy} Lvl {104}", True, (0, 0, 0))
    screen.blit(enemy_info_text, (500, 60))
    pygame.draw.rect(screen, (0,255,0), (500, 80, 104, 10))
    
    
    
    
    if current_screen == "main":
        attack_button.draw(screen)
        bag_button.draw(screen)
        run_button.draw(screen)
        poke_button.draw(screen)
    elif current_screen == "attack":
        mov1_button.draw(screen)
        mov2_button.draw(screen)
        mov3_button.draw(screen)
        mov4_button.draw(screen)
    
    elif current_screen == "bag":
        rim_button.draw(screen)
        pokeballs_button.draw(screen)
    elif current_screen=="poke":
        pokemon1_button.draw(screen)
        pokemon2_button.draw(screen)
        pokemon3_button.draw(screen)
        pokemon4_button.draw(screen)
        pokemon5_button.draw(screen)
        pokemon6_button.draw(screen)


    elif current_screen=="run":
        message = f"scampato pericolo!! ^.^ "
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))

    elif current_screen == "move_selected":
        message = f"{name_gioc} usa {selected_move}"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100)) 
    elif current_screen=="Pokéball":
        message = f"Non hai Pokéball"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Rimedi":
        message = f"Non hai rimedi"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Pokémon 1":
        message = f"Non hai altri Pokémon"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Pokémon 2":
        message = f"Non hai altri Pokémon"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Pokémon 3":
        message = f"Non hai altri Pokémon"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Pokémon 4":
        message = f"Non hai altri Pokémon"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Pokémon 5":
        message = f"Non hai altri Pokémon"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))
    elif current_screen=="Pokémon 6":
        message = f"Non hai altri Pokémon"
        panel = font.render(message, True, (0, 0, 0))
        screen.blit(panel, (400, 360,300,100))

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()