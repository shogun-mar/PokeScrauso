import pygame

class TreeTop(pygame.sprite.Sprite):
    def __init__(self, camera_group, pos):
        # Call the parent class (Sprite) constructor
        super().__init__(camera_group)
        self.image = pygame.image.load("graphics/world_sprites/tree_top.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)