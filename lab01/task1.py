# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
#import matplot
import matplotlib.pyplot as plt
from numpy import asarray

# Read the image from file.
im = Image.open('Beginnings.jpg')
# # Show the image.
im.show()
# # Convert image to gray scale.
im_gray = ImageOps.grayscale(im)
# # Show the grayscale image.
im_gray.show()
#create numpy matrix with pixel values from image
image = Image.open("Beginnings.jpg")

imageArr = np.array(image)

print (imageArr.shape)
grayImagePixels = asarray(im_gray)

rows, cols = grayImagePixels.shape


#nested loops to compute the maximum pixel in the matrix
height, width, channels = imageArr.shape

# Initialize a variable to store the maximum pixel value
maxPixel = 0

# Loop through each pixel value in the matrix
for i in range(height):
    for j in range(width):
        for k in range(channels):
            pixelValue = imageArr[i, j, k]

            # Check if the current pixel value is greater than the current maximum
            if pixelValue > maxPixel:
                maxPixel = pixelValue

# Print the maximum pixel value
print("Maximum Pixel Value:", maxPixel)

matrixNew = np.zeros(shape =(cols,rows))
matrixRows, matrixCols = matrixNew.shape
counterImageRow = matrixRows -1
counterImageCol = 0

for i in range (0,rows):
    for j in range (0, cols):
        matrixNew[counterImageRow,counterImageCol] = grayImagePixels[i,j]
        counterImageRow -= 1
    counterImageRow = matrixRows-1
    counterImageCol += 1

newImage=Image.fromarray(np.uint8(matrixNew))

newImage.show()
newImage.save("counter-clockWise-beginnings.tif")

# create nwe matrix to rotate clockWise

newClockWise = np.zeros(shape=(cols,rows))

clockRows,clockCols = newClockWise.shape

colIndex = clockCols -1
for i in range(0,rows):
    for j in range(0,cols):
        newClockWise[j,colIndex]= grayImagePixels [i,j]
    colIndex -= 1

clockWiseImage = Image.fromarray(np.uint8(newClockWise))

clockWiseImage.show()

clockWiseImage.save("clockWise-Beginnings.tif")

# find max pixel value of clockwize image
maxPixelClock = newClockWise[0,0]
for i in range(0,clockRows):
    for j in range(0,clockCols):
        if newClockWise[i,j] >= maxPixelClock:
            maxPixelClock = newClockWise[i,j]

print ("Maximum Pixel Value (Clockwise):", maxPixelClock)






