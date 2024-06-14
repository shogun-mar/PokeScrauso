import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.display_surface = screen

        #Camera offset
        self.offset = pygame.math.Vector2() 

        #
        self.half_w = self.display_surface.get_width() // 2
        self.half_h = self.display_surface.get_height() // 2
 
        #Ground
        self.ground_surf = pygame.image.load("graphics/world_sprites/1.png").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def custom_draw(self, player):

        self.center_target_camera(player)

        #Terreno
        ground_offset = self.ground_rect.topleft + self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)
        
        #Elementi attivi
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)