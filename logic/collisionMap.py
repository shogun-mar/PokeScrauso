from logic.cameraGroup import CameraGroup
from PIL import Image

#Load images
first_level_first_zone = Image.open("graphics/collision_maps/1_1.png")
first_level_second_zone = Image.open("graphics/collision_maps/1_2.png")
first_level_third_zone = Image.open("graphics/collision_maps/1_3.png")
first_level_maps = [first_level_first_zone, first_level_second_zone, first_level_third_zone]

#Offsets
camera_group_offset = None
internal_camera_group_offset = None

def get_offsets(camera_group_instance):
    global camera_group_offset, internal_camera_group_offset
    camera_group_offset = camera_group_instance.offset
    internal_camera_group_offset = camera_group_instance.internal_offset

#Check if the player can move to the desired coordinates
def allow_movement(desired_coords):

    if CameraGroup.level_num == 1:
        level = first_level_maps
    #Aggiungi altri elif per altri livelli TODO
    else:
        raise Exception("Level not found") #Da togliere messe per debugging

    if CameraGroup.zone_num == 1: zone = level[0]
    elif CameraGroup.zone_num == 2: zone = level[1]
    elif CameraGroup.zone_num == 3: zone = level[2]
    else: raise Exception("Zone not found") #Da togliere messe per debugging

    x_coord = desired_coords[0] + camera_group_offset.x + internal_camera_group_offset.x
    y_coord = desired_coords[1] + camera_group_offset.y + internal_camera_group_offset.y
    #x_coord = ((desired_coord[0] - 720) + settings.PLAYER_SPEED) * (-1)
    #y_coord = ((desired_coord[1] - 490) + settings.PLAYER_SPEED) * (-1)
    #pixel_color = zone.getpixel((x_coord, y_coord))

    print("Coords:",desired_coords, "-Offset:", camera_group_offset, "-Internal offset:", internal_camera_group_offset, "-Calc coords:", x_coord, y_coord)#, "-Pixel color:", pixel_color)
    return True
    if pixel_color == (0,0,0,0) or pixel_color == (0,0,0,255): #Se il pixel è trasparente o nero
        return False
    return True