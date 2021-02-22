import random

de = ("%02x" % random.randint(0, 255))
re = ("%02x" % random.randint(0, 255))
we = ("%02x" % random.randint(0, 255))
ge = "#"
color = ge + de + re + we
print(color)


def get_complementary(color):
    color = color[1:]
    color = int(color, 16)
    comp_color = 0xFFFFFF ^ color
    comp_color = "#%06X" % comp_color
    return comp_color


print(get_complementary(color))
