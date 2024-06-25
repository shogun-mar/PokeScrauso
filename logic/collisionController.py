from PIL import Image

class CollisionController:
    def __init__(self, camera_group, player):
        #Load images
        first_level_first_zone = Image.open("graphics/collision_maps/1_1.png")
        first_level_second_zone = Image.open("graphics/collision_maps/1_2.png")
        first_level_third_zone = Image.open("graphics/collision_maps/1_3.png")
        first_level_fourth_zone = Image.open("graphics/collision_maps/1_4.png")
        self.first_level_maps = [first_level_first_zone, first_level_second_zone, first_level_third_zone, first_level_fourth_zone]

        #Assigning istances of other classes
        self.camera_group = camera_group
        self.player = player

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

        print("Desired coords:", desired_coords[0], desired_coords[1], "Pixel color:", pixel_color)
        if pixel_color == (0, 183, 239, 255): #Colore che segna il cambio di zona
            if self.player.verse == "right" or self.player.verse == "down":
                self.camera_group.zone_num += 1
            else: self.camera_group.zone_num -= 1 
            
        elif pixel_color == (34, 177, 76, 255): #Colore che segna la presenza di un cespuglio
            print("Cespuglio")
            pass
        
        
        elif pixel_color == (0,0,0,0) or pixel_color == (0,0,0,255): #Se il pixel è trasparente o nero
            return False
    
        return True