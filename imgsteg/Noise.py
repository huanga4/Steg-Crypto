PATH_TO_DIR = r'C:\Users\Ow me back\AppData\Local\atom\app-1.41.0\imgsteg'
import os
import time
#print(os.getcwd())
os.chdir(PATH_TO_DIR)
#print(os.getcwd())
from PIL import Image,ImageChops
from functools import partial
import numpy
import random
import AESdome
import prngSteg

#loading image
image = Image.open("waterfall.png")

#getting pixels
pixels = image.load()
# check to make sure red is the smallest value of compared to green and blue by a difference of atleast 50
# changing the input value of threshold, changes how many pixels will be returned and how effective noise checking should be
# a higher threshold mean higher noise detection
def pixelSelection(image, threshold):
    goodPixels = list() # new list to store the good pixels - ones that meet the criteria of having the r value being the lowest
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # skip first 16 pixels
            if(i == 0):
                j
            # skipping pixels
            p = pixels[i,j] # get the r,g,b values for this pixel
            r = p[0]
            g = p[1]
            b = p[2]
            if(g-r >= threshold and b-r >= threshold): # making sure the r-value is the lower than both b and g by atleast the threshold value
                goodPixels.append([i,j])
    for k in range(16): # check to see if any of the first 16 pixels are in the list - if yes, remove
        if(goodPixels.count([0,k]) > 0):
            goodPixels.remove([0,k])
    return goodPixels

# the NEW function that will return an array of randomized pixels to be used
def randWithNoise(size, seed, im):
    threshold = 50
    random.seed(seed) # set the seed to use for the PRNG
    goodPixels = pixelSelection(image, threshold) # get all the good pixels using the threshold value
    random.shuffle(goodPixels) # shuffle using the seed
    sizePixels = []
    if(size > len(goodPixels)):
        return 'Size larger than valid pixels'
    for x in range(size//2): #size//2 since 2 values are stored in 2 lsb of each red pixel
        sizePixels.append(goodPixels[x])
    return sizePixels

# ----- testing here -----
'''
message = "hello world, it's me, Justin!" # random message
seed = prngSteg.generateSeed(message)
result = randWithNoise(50, seed, image)
print(result)
'''
