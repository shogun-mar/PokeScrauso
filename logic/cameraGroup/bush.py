import pygame

class Bush(pygame.sprite.Sprite):
    def __init__(self, camera_group, pos, level_num, zone_num):
        # Call the parent class (Sprite) constructor
        super().__init__(camera_group)
        self.level_num = level_num
        self.zone_num = zone_num
        self.image = pygame.image.load("graphics/world_sprites/bush_half.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def has_player_inside(self, player_rect):
        return self.rect.colliderect(player_rect)