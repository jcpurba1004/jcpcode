width = 2
height = 3
for y in range(height):
    for x in range(width):
        print((x, y), end = " ")
    print()

for y in range(height):
    for x in range(width):
#        <do something at position (x, y)>

#image = Image(150, 150)
#for y in range(image.getHeight()):
#    for x in range(image.getWidth()):
#        image.setPixel(x, y, (255, 0, 0))