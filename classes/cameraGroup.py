import pygame
from settings import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.display_surface = screen

        #Dimensions
        self.half_w = self.display_surface.get_width() // 2
        self.half_h = self.display_surface.get_height() // 2

        #Camera offset
        self.offset = pygame.math.Vector2() 

        #Camera zoom
        self.zoom_scale = INITIAL_ZOOM
        self.internal_surface_size = INTERNAL_SURFACE_SIZE #Per garantire che la camera possa zoomare si fanno tutte le operazioni di draw su una superficie interna che verrà poi scalata
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_surface_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size) #
        self.internal_offset = pygame.math.Vector2(0,0)
        self.internal_offset.x = self.internal_surface_size_vector.x // 2 - self.half_w
        self.internal_offset.y = self.internal_surface_size_vector.y // 2 - self.half_h

        #Ground
        self.ground_surf = pygame.image.load("graphics/world_sprites/1.png").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

    def keyboard_zoom_control(self):
        keys = pygame.key.get_pressed()
        if keys[ZOOM_UP_KEY] and self.zoom_scale < ZOOM_SCALE_LIMITS[1]:
            self.zoom_scale += ZOOM_SCALING_VELOCITY
        elif keys[ZOOM_DOWN_KEY] and self.zoom_scale > ZOOM_SCALE_LIMITS[0]:
            self.zoom_scale -= ZOOM_SCALING_VELOCITY


    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def custom_draw(self, player):

        self.keyboard_zoom_control()
        self.center_target_camera(player)

        self.internal_surface.fill(BACKGROUND_COLOR)

        #Terreno
        ground_offset = self.ground_rect.topleft + self.offset + self.internal_offset
        self.internal_surface.blit(self.ground_surf, ground_offset)
        
        #Elementi attivi
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surface.blit(sprite.image, offset_pos)

        scaled_surface = pygame.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center = (self.half_w, self.half_h))

        self.display_surface.blit(scaled_surface, scaled_rect)