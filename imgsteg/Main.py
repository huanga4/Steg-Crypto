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
import ImageSteg
import prngSteg

key = "This_key_for_demo_purposes_only!"
plaintext = "Text may be any length you wish, no padding is required"
ciphertext = AESdome.encryptmsg(plaintext, key) #cipher text as array of bits
#print(ciphertext)
#print(msgasbits)
msgasbits = AESdome.bitfield(int.from_bytes(ciphertext,byteorder = 'big'))
seed = 57895 # random seed for testing

IMAGE_FILE = 'waterfall.png'# Enter the name of your image here.
#im = Image.open(IMAGE_FILE)
#index = 0 #???????
#msg = 'yullo'
#msgasbits = AESdome.tobits(msg)
#msgasbytes = AESdome.bittobytes()
print(ciphertext)
print(len(ciphertext))
print(len(msgasbits))
#ImageSteg.modimage(Image.open(IMAGE_FILE), partial(ImageSteg.flipbits,n = 2))
#ImageSteg.modiimage(Image.open(IMAGE_FILE), ciphertext, seed)
'''
ImageSteg.modimagefields(Image.open(IMAGE_FILE), ciphertext, key)

print('banana')

#decmsg = ImageSteg.bitsfromimage(Image.open('tmp1.png'), len(msgasbits), seed)
#decrypted = AESdome.decryptmsg(decmsg, key, len(ciphertext))
#print(decrypted)

#decmsg = ImageSteg.bitsfromimgfields(Image.open('tmp1.png'), seed, key)
#decrypted = AESdome.decryptmsg(decmsg, key, len(ciphertext))
IMAGE_FILE_1 = 'tmp1.png'
decrypted = ImageSteg.bitsfromimgfields(Image.open(IMAGE_FILE_1),key)
print(decrypted)
print(ImageSteg.isDiff(Image.open(IMAGE_FILE),Image.open(IMAGE_FILE_1)))
'''

ImageSteg.modimagefieldsnoise(Image.open(IMAGE_FILE), ciphertext, key)

print('banana')

#decmsg = ImageSteg.bitsfromimage(Image.open('tmp1.png'), len(msgasbits), seed)
#decrypted = AESdome.decryptmsg(decmsg, key, len(ciphertext))
#print(decrypted)

#decmsg = ImageSteg.bitsfromimgfields(Image.open('tmp1.png'), seed, key)
#decrypted = AESdome.decryptmsg(decmsg, key, len(ciphertext))
IMAGE_FILE_1 = 'tmp1.png'
decrypted = ImageSteg.bitsfromimgfieldsnoise(Image.open(IMAGE_FILE_1),key)
print(decrypted)
print(ImageSteg.isDiff(Image.open(IMAGE_FILE),Image.open(IMAGE_FILE_1)))

#print(key)
#print (decmsg)
#print(AESdome.frombits(decmsg))
#print (checkbits(bitsfromimage(Image.open('tmp1.png'), len(msgasbits), index),bitsfromimage(Image.open('tmp1.png'), len(msgasbits), index)))
