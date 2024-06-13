import pygame
import sys
from settings import *
from classes.player import Player

def draw_start_menu():
    fake_screen.blit(start_background, (0, 0))
    fake_screen.blit(start_button, start_button_rect)

def draw_pokedex_menu():
    pass

def draw_map_menu():
    pass

#Inizializzazione di Pygame e impostazione dello schermo
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
fake_screen = screen.copy()
clock = pygame.time.Clock()
pygame.display.set_caption("PokèScrauso")
pygame.display.set_icon(pygame.image.load("graphics/icon.png"))

#Variabili di gioco
start_menu = True
running = True

#Images
start_background = pygame.image.load("graphics/menus/backgrounds/startBackground.png").convert_alpha()

#Buttons
start_button = pygame.image.load("graphics/menus/buttons/startbutton.png").convert_alpha()
start_button_rect = start_button.get_rect(); start_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

# Start menu loop
while start_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Mette entrambe a false per uscire completamente dal gioco
            start_menu = False
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos): # Check if the mouse click is within the start button rectangle
                start_menu = False
        elif event.type == pygame.VIDEORESIZE: # Ridimensiona la superficie dello schermo
            screen = pygame.display.set_mode((event.w, event.h), flags, vsync=1)

    draw_start_menu()

    # Ridimensiona la superficie falsa e la disegna sulla finestra
    screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
    pygame.display.flip() # Completly update the display
    clock.tick(MAX_FPS)

#Objects initialization (inserita qui perchè non necessaria se l'utente chiude il gioco dal menù iniziale)
player = Player(0,0,'down') #Parametri arbitrari per testing, da sistemare

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == EXIT_KEY):
            running = False
        elif event.type == pygame.VIDEORESIZE: # Ridimensiona la superficie dello schermo
            screen = pygame.display.set_mode((event.w, event.h), flags, vsync=1)

    keys = pygame.key.get_pressed() # Restituisce una lista di tasti premuti 
    #Controlla i movimenti del giocatore
    if keys[pygame.K_w]:
        player.move_up()
    elif keys[pygame.K_s]:
        player.move_down()
    elif keys[pygame.K_a]:
        player.move_left()
    elif keys[pygame.K_d]:
        player.move_right()

    #Gestisce la comparsa dei menù
    if keys[POKEDEK_KEY]:
        draw_pokedex_menu()
    elif keys[MAP_KEY]:
        draw_map_menu()

    fake_screen.fill((0,0,0)) # Pulisce lo schermo

    # Ridimensiona la superficie falsa e la disegna sulla finestra
    screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
    pygame.display.flip()
    clock.tick(MAX_FPS)

pygame.quit()
sys.exit()