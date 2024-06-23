from PIL import Image
from settings import  *

#Load images
first_level_first_zone = Image.open("graphics/collision_maps/1_1.png")
first_level_second_zone = Image.open("graphics/collision_maps/1_2.png")
first_level_third_zone = Image.open("graphics/collision_maps/1_3.png")
first_level_maps = [first_level_first_zone, first_level_second_zone, first_level_third_zone]

def allow_movement(desired_coord, level_num, zone_num):
    if level_num == 1:
        level = first_level_maps
    #Aggiungi altri elif per altri livelli TODO
    else:
        raise Exception("Level not found") #Da togliere messe per debugging

    if zone_num == 1: zone = level[0]
    elif zone_num == 2: zone = level[1]
    elif zone_num == 3: zone = level[2]
    else: raise Exception("Zone not found") #Da togliere messe per debugging

    x_coord = ((desired_coord[0] - 720) + PLAYER_SPEED) * (-1)
    y_coord = ((desired_coord[1] - 480) + PLAYER_SPEED) * (-1)
    print("Coordinates: ", x_coord," ", y_coord)
    print("Pixel: ", zone.getpixel((x_coord, y_coord)))

    if zone.getpixel((x_coord, y_coord)) == (0,0,0,0) or zone.getpixel((x_coord, y_coord)) == (0,0,0,255): #Se il pixel è trasparente o nero
        return False
    else:
        return True