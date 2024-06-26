from pygame import image, sprite

class Bush(sprite.Sprite):
    def __init__(self, camera_group, pos):
        # Call the parent class (Sprite) constructor
        super.__init__(camera_group)
        self.pos = pos
        self.sprite = image.load("graphics/world_sprites/bush_half.png").convert_alpha()
        self.rect = self.sprite.get_rect(topleft = pos)

    def has_player_inside(self, player_rect):
        return self.rect.colliderect(player_rect)