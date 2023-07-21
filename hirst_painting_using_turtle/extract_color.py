import colorgram as cg

color_list = cg.extract("image.jpg", 60)
color_palette = []

for count in range(len(color_list)):
    r = (color_list[count]).rgb.r
    g = (color_list[count]).rgb.g
    b = (color_list[count]).rgb.b
    rgb = (r, g, b)
    color_palette.append(rgb)


print(color_palette)
