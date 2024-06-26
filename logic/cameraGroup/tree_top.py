import pygame

class TreeTop(pygame.sprite.Sprite):
    def __init__(self, camera_group, pos, level_num, zone_num):
        # Call the parent class (Sprite) constructor
        super().__init__(camera_group)
        self.level_num = level_num
        self.zone_num = zone_num
        self.image = pygame.image.load("graphics/world_sprites/tree_top.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)