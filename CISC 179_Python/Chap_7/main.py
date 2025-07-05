from PIL import Image

sister = Image.open("sister.jpg")
girl = Image.open("girl.png")

area = (100, 100, 300, 334)
sister.paste(girl, area)

sister.show()
