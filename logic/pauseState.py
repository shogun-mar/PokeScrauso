import pygame
from logic.gameState import GameState
import settings

def handle_pause_input(self, key):
    if key == settings.PAUSE_KEY:
        if self.game_state == GameState.GAMEPLAY:
            self.game_state = GameState.PAUSE
        else:
            self.game_state = GameState.GAMEPLAY

def render_pause(self):
        self.fake_screen.blit(self.darkened_surface, (0,0))
        font = pygame.font.Font(None, 36)  # Choose the font for the text
        text = font.render("Pause", True, (255, 255, 255))  # Create a surface with the text
        text_rect = text.get_rect(center=self.screen.get_rect().center)  # Get the rectangle of the text surface
        self.fake_screen.blit(text, text_rect)