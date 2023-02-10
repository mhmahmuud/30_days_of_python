from random import choice
def list_of_rgb_colors(n):
    rgb_list = []
    for i in range(n):
        levels = range(32,256)
        rgb = "rgb" + str(tuple(choice(levels) for i in range(3)))
        rgb_list.append(rgb)
    return rgb_list

import random
def list_of_hexa_colors(n):
    list_hexa_colors = []
    for i in range(n):
        color = random.randrange(0, 2**24)
        hex_color = "#" + hex(color)
        list_hexa_colors.append(hex_color)       
    return list_hexa_colors