from PIL import Image,ImageOps
import numpy as np
from numpy import asarray

def myImageInverse(inImage):
    rows,cols = inImage.shape
    matrix = np.zeros(shape = (rows,cols))

    for i in range(0,rows):
        for j in range(0,cols):
            matrix[i,j] = 255 - inImage[i,j]

    return matrix