import pygame
from settings import *

class CameraGroup(pygame.sprite.Group):

    #Game variables as class attributes to simplify logic in collisionMap.py
    level_num = 1
    zone_num = 1

    def __init__(self, screen):
        super().__init__()
        self.display_surface = screen

        #Dimensions
        self.half_w = self.display_surface.get_width() // 2
        self.half_h = self.display_surface.get_height() // 2

        #Camera offset
        self.offset = pygame.math.Vector2()

        #Dichiarazione di variabili temporanee per gli offset
        self.offset_pos = None
         

        #Camera zoom
        self.zoom_scale = INITIAL_ZOOM
        self.internal_surface_size = INTERNAL_SURFACE_SIZE #Per garantire che la camera possa zoomare si fanno tutte le operazioni di draw su una superficie interna che verrà poi scalata
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_surface_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size) #
        self.internal_offset = pygame.math.Vector2(0,0)
        self.internal_offset.x = self.internal_surface_size_vector.x // 2 - self.half_w
        self.internal_offset.y = self.internal_surface_size_vector.y // 2 - self.half_h

        #Ground images
        self.ground_surf_1_1 = pygame.image.load("graphics/world_sprites/1_1.png").convert_alpha()
        self.ground_surf_1_2 = pygame.image.load("graphics/world_sprites/1_2.png").convert_alpha()
        self.ground_surf_1_3 = pygame.image.load("graphics/world_sprites/1_3.png").convert_alpha()
        self.ground_surf_1_4 = pygame.image.load("graphics/world_sprites/1_4.png").convert_alpha()
        self.ground_surfaces = [self.ground_surf_1_1, self.ground_surf_1_2, self.ground_surf_1_3, self.ground_surf_1_4]

        self.ground_rect_1_1 = self.ground_surf_1_1.get_rect(topleft = (0,0))
        self.ground_rect_1_2 = self.ground_surf_1_2.get_rect(topleft = (self.ground_rect_1_1.bottomleft[0] + 1055, self.ground_rect_1_1.bottomleft[1]))
        self.ground_rect_1_3 = self.ground_surf_1_3.get_rect(topleft = (self.ground_rect_1_2.bottomleft[0] + 95, self.ground_rect_1_2.bottomleft[1]))
        self.ground_rect_1_4 = self.ground_surf_1_4.get_rect(topleft = (self.ground_rect_1_3.bottomleft[0] + 500, self.ground_rect_1_3.bottomleft[1] - 500))
        self.ground_rects = [self.ground_rect_1_1, self.ground_rect_1_2, self.ground_rect_1_3, self.ground_rect_1_4]

        #Collision maps
        self.first_level_first_zone = pygame.image.load("graphics/collision_maps/1_1.png").convert_alpha()
        self.first_level_first_zone.set_alpha(128)
        self.first_level_second_zone = pygame.image.load("graphics/collision_maps/1_2.png").convert_alpha()
        self.first_level_second_zone.set_alpha(128)
        self.first_level_third_zone = pygame.image.load("graphics/collision_maps/1_3.png").convert_alpha()
        self.first_level_third_zone.set_alpha(128)
        self.first_level_maps = [self.first_level_first_zone, self.first_level_second_zone, self.first_level_third_zone]

        self.first_level_first_zone_rect = self.first_level_first_zone.get_rect(topleft = (0,0))
        self.first_level_second_zone_rect = self.first_level_second_zone.get_rect(topleft = (self.ground_rect_1_1.bottomleft[0] + 1055, self.ground_rect_1_1.bottomleft[1]))
        self.first_level_third_zone_rect = self.first_level_third_zone.get_rect(topleft = (self.ground_rect_1_2.bottomleft[0] + 95, self.ground_rect_1_2.bottomleft[1]))
        self.first_level_maps_rects = [self.first_level_first_zone_rect, self.first_level_second_zone_rect, self.first_level_third_zone_rect]

    def keyboard_zoom_control(self):
        keys = pygame.key.get_pressed()
        if keys[ZOOM_OUT_KEY] and self.zoom_scale < ZOOM_SCALE_LIMITS[1]:
            self.zoom_scale += ZOOM_SCALING_VELOCITY
        elif keys[ZOOM_IN_KEY] and self.zoom_scale > ZOOM_SCALE_LIMITS[0]:
            self.zoom_scale -= ZOOM_SCALING_VELOCITY

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw_ground_zones(self):
        for i, ground_surf in enumerate(self.ground_surfaces):
            offset = self.ground_rects[i].topleft + self.offset + self.internal_offset
            self.internal_surface.blit(ground_surf, offset)
    
        # Assuming first_level_maps contains the surfaces for first_level_maps_rects
        for i, map_surf in enumerate(self.first_level_maps):
            offset = self.first_level_maps_rects[i].topleft + self.offset + self.internal_offset
            self.internal_surface.blit(map_surf, offset)
    
    def calculate_new_player_relative_coords(self):

    def custom_draw(self, player):

        self.keyboard_zoom_control()
        self.center_target_camera(player)

        self.internal_surface.fill(BACKGROUND_COLOR)

        #Terreno
        self.draw_ground_zones()
        
        #Elementi attivi
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            self.offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            relative_pos = (sprite.rect.midbottom - self.offset + self.internal_offset) - (self.first_level_maps_rects[0].topleft + self.offset + self.internal_offset) 
            print("original coords:", sprite.rect.topleft, "with offset", relative_pos)
            self.internal_surface.blit(sprite.image, self.offset_pos)

        scaled_surface = pygame.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center = (self.half_w, self.half_h))
        self.display_surface.blit(scaled_surface, scaled_rect)

    def change_level(self, level_num):
        CameraGroup.level_num = level_num
    
    def change_zone(self, zone_num):
        CameraGroup.zone_num = zone_num