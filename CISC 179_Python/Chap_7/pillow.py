from PIL import Image

img = Image.open("bucky.jpg")
print(img.size)
print(img.format)

img.show()
