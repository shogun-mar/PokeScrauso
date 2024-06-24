from PIL import Image

class CollisionController:
    def __init__(self, camera_group_instance):
        #Load images
        first_level_first_zone = Image.open("graphics/collision_maps/1_1.png")
        first_level_second_zone = Image.open("graphics/collision_maps/1_2.png")
        first_level_third_zone = Image.open("graphics/collision_maps/1_3.png")
        first_level_fourth_zone = Image.open("graphics/collision_maps/1_4.png")
        self.first_level_maps = [first_level_first_zone, first_level_second_zone, first_level_third_zone, first_level_fourth_zone]

        #Offsets
        self.camera_group_offset = None
        self.internal_camera_group_offset = None

        #Camera group instance
        self.camera_group = camera_group_instance

    def get_offsets(self, camera_group_instance):
        self.camera_group_offset = camera_group_instance.offset
        self.internal_camera_group_offset = camera_group_instance.internal_offset

    #Check if the player can move to the desired coordinates
    def allow_movement(self, desired_coords):

        level_num = self.camera_group.level_num

        if level_num == 1:
            level = self.first_level_maps
        #Aggiungi altri elif per altri livelli TODO
        else:
            raise Exception("Level not found") #Da togliere messe per debugging

        zone_num = self.camera_group.zone_num

        if zone_num == 1: zone = level[0]
        elif zone_num == 2: zone = level[1]
        elif zone_num == 3: zone = level[2]
        elif zone_num == 4: zone = level[3]
        else: raise Exception("Zone not found") #Da togliere messe per debugging

        x_coord = desired_coords[0]
        y_coord = desired_coords[1]
        #pixel_color = zone.getpixel((x_coord, y_coord))

        #print("Coords:",desired_coords, "-Offset:", camera_group_offset, "-Internal offset:", internal_camera_group_offset, "-Calc coords:", x_coord, y_coord)#, "-Pixel color:", pixel_color)
        return True
        if pixel_color == (0,0,0,0) or pixel_color == (0,0,0,255): #Se il pixel è trasparente o nero
            return False
        return True