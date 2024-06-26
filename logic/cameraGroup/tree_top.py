from pygame import image, sprite

class TreeTop(sprite.Sprite):
    def __init__(self, camera_group, pos):
        # Call the parent class (Sprite) constructor
        super.__init__(camera_group)
        self.pos = pos
        self.sprite = image.load("graphics/world_sprites/tree_top.png").convert_alpha()
        self.rect = self.sprite.get_rect(topleft = pos)