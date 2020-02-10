PATH_TO_DIR = r'C:\Users\Ow me back\AppData\Local\atom\app-1.41.0\imgsteg'
import os
import time
#print(os.getcwd())
os.chdir(PATH_TO_DIR)
#print(os.getcwd())
from PIL import Image,ImageChops
from functools import partial
import numpy
import AESdome
import prngSteg
import hashlib
import Noise


def encodelsb(val,msgArr,index): #stores values in 2 lsb based on contents in index of msgArr and the current value of the pixel
    if(msgArr[index] == 1):
        val = set_bit(val,1)
        index += 1
    else:
        val = clear_bit(val,1)
        index += 1
    if(msgArr[index] == 1):
        val = set_bit(val,0)
        index += 1
    else:
        val = clear_bit(val,0)
        index += 1
    return val

def flipbits(val,n):  # Flip n least significant bits in val
    val = val^((1<<n)-1)
    #print(val)
    return val

def clearbits(val,n):  # Flip n least significant bits in val
    return val^((1<<n)-1)

def set_bit(value, bit): #sets bit in specified place
    return value | (1<<bit)

def clear_bit(value, bit): #clears bit in specified place
    return value & ~(1<<bit)

#print(clear_bit(9,0))
#print(set_bit(4,0))
'''
def modimage(im, func): # Apply specified function func to each pixel.
    px = im.load()  # Get the pixels in the image
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            print(str(i) + ',' + str(j))
            p = px[i,j] # get the r,g,b values for this pixel
            r = func(p[0])
            g = p[1]
            #print(g)
            b = p[2]
            px[i,j] = (r,g,b)
    #im.show()
    im.save('tmp.png') # You can save the modified image
'''
'''
def modiimage(im, size, msgArr, index): # Apply specified function func to each pixel.
    px = im.load()  # Get the pixels in the image
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if index == size:
                im.save('tmp1.png')
                return
            p = px[i,j] # get the r,g,b values for this pixel
            r = encodelsb(p[0], msgArr, index)
            g = p[1]
            b = p[2]
            px[i,j] = (r,g,b)
            #print(isnthset(r,1))
            #print(isnthset(r,0))
            index+=2
    #im.show()
    im.save('tmp1.png') # You can save the modified image
'''
'''
seed = 57895 # random seed for testing
message = "hello world, it's me, Justin!" # random message
result = generateNRandomPixels(message, seed, image)
# print(result)
randList = result
r = listOfRandomPixels(randList, image)
print(r)
print(len(r) == len(message)+1)
'''
'''
def modiimage(im, msg, seed): # Apply specified function func to each pixel.
    msgArr = AESdome.bitfield(int.from_bytes(msg,byteorder = 'big'))
    size = len(msgArr)
    index = 0
    #print(msgArr)
    #print(len(r))
    #print(len(msgArr))
    randList = prngSteg.generateNRandomPixels(size, seed, im)
    r = prngSteg.listOfRandomPixels(randList, im)
    px = im.load()  # Get the pixels in the image
    for x in r:
        i = x[1]
        j = x[0]
        #print(i)
        #print(j)
        #if index == size:
            #im.save('tmp1.png')
            #return
        #print(px[0,0])
        #print(px[i,j])
        p = px[i,j] # get the r,g,b values for this pixel
        r = encodelsb(p[0], msgArr, index)
        g = p[1]
        b = p[2]
        px[i,j] = (r,g,b)
        #print(isnthset(r,1))
        #print(isnthset(r,0))
        index+=2
    #im.show()
    im.save('tmp1.png') # You can save the modified image
'''
def modimagefields(im, msg, key):
    #print(im.format, im.size, im.mode)
    #print(im.size[0])
    #im.show()
    msgfield = 32 #sets first 32/2 or 16 pixels to store size of msg
    msgArr = AESdome.bitfield(int.from_bytes(msg,byteorder = 'big')) #converts into array of bits [0,0,0,1,0,1]etc...
    size = len(msgArr)
    if(size > 2**msgfield):
        return 'Message is too large to store in image'
    sizeindex = 0
    msgindex = 0
    sizeArr = AESdome.intasbits(size, msgfield) #converts the int to array of bits
    #print(msgArr)
    #print(len(r))
    #print(len(msgArr))
    seed = prngSteg.generateSeed(key)
    randList = prngSteg.generateNRandomPixels(size, seed, im)
    rl = prngSteg.listOfRandomPixels(randList, im)
    px = im.load()  # Get the pixels in the image
    for y in range(16): #storing size in first 16 pixels of image
        i = y
        j = 0
        p = px[i,j]
        r = encodelsb(p[0], sizeArr, sizeindex)
        g = p[1]
        b = p[2]
        px[i,j] = (r,g,b)
        sizeindex += 2

    for x in rl: #storing message in msgsize/2 random pixels (2lsb in each random pixel)
        i = x[1]
        j = x[0]
        #print(i)
        #print(j)
        #if index == size:
            #im.save('tmp1.png')
            #return
        #print(px[0,0])
        #print(px[i,j])
        p = px[i,j] # get the r,g,b values for this pixel
        r = encodelsb(p[0], msgArr, msgindex)
        msgindex += 2
        g = p[1]
        b = p[2]
        px[i,j] = (r,g,b)
        #print(isnthset(r,1))
        #print(isnthset(r,0))
    #im.show()
    im.save('tmp1.png') # You can save the modified image

def isnthset(val, n):
    n += 1
    if val & (1 << (n - 1)):
        return 1
    else:
        return 0

#print(isnthset(4,0))

def decodelsb(val, msgArr, index):
    msgArr.append(isnthset(val,1))
    msgArr.append(isnthset(val,0))
'''
def bitsfromimage(im, size, seed):
    index = 0
    randList = prngSteg.generateNRandomPixels(size, seed, im)
    r = prngSteg.listOfRandomPixels(randList, im)
    msgArr = [];
    px = im.load()  # Get the pixels in the image

    for y in range(16): #storing size in first 16 pixels of image
        i = y
        j = 0
        p = px[i,j]
        r = encodelsb(p[0], sizeArr, sizeindex)
        g = p[1]
        b = p[2]
        px[i,j] = (r,g,b)
        sizeindex += 2

    for x in r:
        i = x[1]
        j = x[0]
        #if index == size:
            #return msgArr
        p = px[i,j] # get the r,g,b values for this pixel
        decodelsb(p[0], msgArr, index)
        index+=2
    return msgArr
    #im.show()
    #im.save('.png') # You can save the modified image
'''
def bitsfromimgfields(im, key):
    index = 0
    msgfield = 32
    sizeArr = [];
    msgArr = [];
    px = im.load()  # Get the pixels in the image
    sizeindex = 0
    msgindex = 0
    for y in range(16): #storing size in first 16 pixels of image
        i = y
        j = 0
        p = px[i,j]
        decodelsb(p[0], sizeArr, sizeindex)
        sizeindex += 2

    #needs generateNRandomPixels needs to exclude first 16 pixels, we will reserve that for getting size of msg
    size = AESdome.bitsasint(sizeArr)
    #print(size)
    seed = prngSteg.generateSeed(key)
    randList = prngSteg.generateNRandomPixels(size, seed, im)
    r = prngSteg.listOfRandomPixels(randList, im)

    for x in r:
        i = x[1]
        j = x[0]
        #if index == size:
            #return msgArr
        p = px[i,j] # get the r,g,b values for this pixel
        decodelsb(p[0], msgArr, msgindex)
        msgindex+=2

    decrypted = AESdome.decryptmsg(msgArr, key, size//8) #size//8 represents bytssize as integer
    return decrypted
    #im.show()
    #im.save('.png') # You can save the modified image

def changeone(image):
    im = Image.open(image)
    px = im.load()
    p = px[0,0]
    r = p[0]
    r = clear_bit(r,1)
    r = clear_bit(r,0)
    px[0,0] = (r,p[1],p[2])
    im.save('tmp4.png')

def isDiff(image1, image2):
    diff = ImageChops.difference(image1, image2)
    if diff.getbbox():
        return True #if different return true
    else:
        return False #if same return false

def checkbits(bitArr, bitArr1):
    for x in bitArr:
        if(bitArr[x] != bitArr1[x]):
            return False
    return True

def modimagefieldsnoise(im, msg, key):
    #print(im.format, im.size, im.mode)
    #print(im.size[0])
    #im.show()
    msgfield = 32 #sets first 32/2 or 16 pixels to store size of msg
    msgArr = AESdome.bitfield(int.from_bytes(msg,byteorder = 'big')) #converts into array of bits [0,0,0,1,0,1]etc...
    size = len(msgArr)
    if(size > 2**msgfield):
        return 'Message is too large to store in image'
    sizeindex = 0
    msgindex = 0
    sizeArr = AESdome.intasbits(size, msgfield) #converts the int to array of bits
    threshold = 50
    #print(msgArr)
    #print(len(r))
    #print(len(msgArr))
    seed = prngSteg.generateSeed(key)
    rl = Noise.randWithNoise(size, seed, im)
    px = im.load()  # Get the pixels in the image
    for y in range(16): #storing size in first 16 pixels of image
        i = y
        j = 0
        p = px[i,j]
        r = encodelsb(p[0], sizeArr, sizeindex)
        g = p[1]
        b = p[2]
        px[i,j] = (r,g,b)
        sizeindex += 2

    for x in rl: #storing message in msgsize/2 random pixels (2lsb in each random pixel)
        i = x[0]
        j = x[1]
        #print(i)
        #print(j)
        #if index == size:
            #im.save('tmp1.png')
            #return
        #print(px[0,0])
        #print(px[i,j])
        p = px[i,j] # get the r,g,b values for this pixel
        r = encodelsb(p[0], msgArr, msgindex)
        msgindex += 2
        g = p[1]
        b = p[2]
        px[i,j] = (r,g,b)
        #print(isnthset(r,1))
        #print(isnthset(r,0))
    #im.show()
    im.save('tmp1.png') # You can save the modified image

def bitsfromimgfieldsnoise(im, key):
    index = 0
    msgfield = 32
    sizeArr = [];
    msgArr = [];
    threshold = 50
    px = im.load()  # Get the pixels in the image
    sizeindex = 0
    msgindex = 0
    for y in range(16): #storing size in first 16 pixels of image
        i = y
        j = 0
        p = px[i,j]
        decodelsb(p[0], sizeArr, sizeindex)
        sizeindex += 2

    #needs generateNRandomPixels needs to exclude first 16 pixels, we will reserve that for getting size of msg
    size = AESdome.bitsasint(sizeArr)
    #print(size)
    seed = prngSteg.generateSeed(key)
    rl = Noise.randWithNoise(size, seed, im)

    for x in rl:
        i = x[0]
        j = x[1]
        #if index == size:
            #return msgArr
        p = px[i,j] # get the r,g,b values for this pixel
        decodelsb(p[0], msgArr, msgindex)
        msgindex+=2

    decrypted = AESdome.decryptmsg(msgArr, key, size//8) #size//8 represents bytssize as integer
    return decrypted
    #im.show()
    #im.save('.png') # You can save the modified image
