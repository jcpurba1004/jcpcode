average = (r + g + b) // 3
image.setPixel(x, y, (average, average, average))

def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
#        (r, g, b) = image.getPixel(x, y)
#        r = int(r * 0.299)
#        g = int(g * 0.587)
#        b = int(b * 0.114)
#        lum = r + g + b
#        image.setPixel(x, y, (lum, lum, lum))