from PIL import Image
from PIL import Imagefilter

sister = Image.open("sister.jpg")
blur = sister.filter(Imagefilter.BLUR)
detail = sister.filter(Imagefilter.DETAIL)
edges = sister.filter(Imagefilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()
