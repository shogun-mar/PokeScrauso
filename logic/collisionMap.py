from PIL import Image

#Load images
first_level_first_zone = Image.open("graphics/first_level/1_1.png")
first_level_second_zone = Image.open("graphics/first_level/1_2.png")
first_level_third_zone = Image.open("graphics/first_level/1_3.png")

def allow_movement(desired_coord, level)