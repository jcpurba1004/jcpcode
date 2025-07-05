from images import Image
image = Image("smokey.gif")
image.draw()
newImage = image.clone()
newImage.draw()
grayscale(newImage)
newImage.draw()
image.draw()
