from PIL import Image
from logic.player import Player

#Load images
first_level_first_zone = Image.open("graphics/first_level/1_1.png")
first_level_second_zone = Image.open("graphics/first_level/1_2.png")
first_level_third_zone = Image.open("graphics/first_level/1_3.png")

first_level_images = [first_level_first_zone, first_level_second_zone, first_level_third_zone]

def allow_movement(desired_coord, level_num, zone_num):
    if level_num == 1:
        level = first_level_images
    #Aggiungi altri elif per altri livelli TODO
    else:
        raise Exception("Level not found")

    if zone_num == 1: zone = level[0]
    elif zone_num == 2: zone = level[1]
    elif zone_num == 3: zone = level[2]
    else: raise Exception("Zone not found")

    coor

    if zone.getpixel(desired_coord) == (0,0,0,255) or :

    return False

        