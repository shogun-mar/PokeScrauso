from PIL import Image

class CollisionController:
    def __init__(self, camera_group):
        #Load images
        first_level_first_zone = Image.open("graphics/collision_maps/1_1.png")
        first_level_second_zone = Image.open("graphics/collision_maps/1_2.png")
        first_level_third_zone = Image.open("graphics/collision_maps/1_3.png")
        first_level_fourth_zone = Image.open("graphics/collision_maps/1_4.png")
        self.first_level_maps = [first_level_first_zone, first_level_second_zone, first_level_third_zone, first_level_fourth_zone]

        self.camera_group = camera_group

    #Check if the player can move to the desired coordinates
    def allow_movement(self, desired_coords):

        level_num = self.camera_group.level_num

        if level_num == 0:
            maps = self.first_level_maps
        #Aggiungi altri elif per altri livelli TODO
        else:
            raise Exception("self.maps not found") #Da togliere messe per debugging

        zone_num = self.camera_group.zone_num

        if zone_num == 0: zone = maps[0]
        elif zone_num == 1: zone = maps[1]
        elif zone_num == 2: zone = maps[2]
        elif zone_num == 3: zone = maps[3]
        else: raise Exception("Zone not found") #Da togliere messe per debugging

        pixel_color = zone.getpixel((desired_coords[0], desired_coords[1]))

        #print("Coords:",desired_coords, "-Offset:", self.camera_group_offset, "-Internal offset:", selfinternal_camera_group_offset, "-Calc coords:", x_coord, y_coord)#, "-Pixel color:", pixel_color)
        return True
        if pixel_color == (0,0,0,0) or pixel_color == (0,0,0,255): #Se il pixel è trasparente o nero
            return False
        return True