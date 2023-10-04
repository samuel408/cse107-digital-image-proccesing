from PIL import Image, ImageOps
import numpy as np
from numpy import asarray

 #create empty numpy matrix(100 x 256)

emptyMatrix = np.zeros(shape = (100,256))

# fill matrix with values

rows,cols = emptyMatrix.shape

for i in range(0,rows):
  for j in range(0,cols):
    emptyMatrix[i,j] = j


#create grayscale image
grayScale = Image.fromarray(np.uint8(emptyMatrix))

#display image and save image

grayScale.show()
grayScale.save("gradiency-Image.tif")

# compute average pixel value

pixelValue = 0
for i in range(0,rows):
 for j in range(0,cols):
  pixelValue += emptyMatrix[i,j]

avg = pixelValue/ (rows*cols)
print("Average Pixel Value:", avg)


