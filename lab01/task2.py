from PIL import Image, ImageOps
from MyImageFunctions import *
import numpy as np
from numpy import asarray

image = Image.open("Watertower.tif")
image.show()
grayImagePixels = asarray(image)
rows,cols = grayImagePixels.shape

print("image mode:", image.mode)

inverseMatrix = myImageInverse(grayImagePixels)

inverseImage = Image.fromarray((np.uint8(inverseMatrix)))

inverseImage.show()

inverseImage.save("inverse-watertower.tif")