from PIL import Image

baby = Image.open("baby.jpg")
square_baby = baby.resize((250, 250))
flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby = baby.transpose(Image.ROTATE_90)

baby.show()
square_baby.show()
flip_baby.show()
flip_baby.show()