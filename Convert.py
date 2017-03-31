import numpy as np
from PIL import Image

Y = 0
Cb = 1
Cr = 2

def convert(img):
    img = img.convert('YCbCr')
    return np.array(img)

def crch(img):
    YCbCr = list(img.getdata())
    imYCbCr = np.reshape(YCbCr, (img.size[1], img.size[0], 3))
    imYCbCr = imYCbCr.astype(np.uint8)
    # Cr is the red-difference chroma component (changes in red colorfulness)
    return Image.fromarray(imYCbCr[:, :, Cr], "L")

def cbch(img):
    YCbCr = list(img.getdata())
    imYCbCr = np.reshape(YCbCr, (img.size[1], img.size[0], 3))
    imYCbCr = imYCbCr.astype(np.uint8)
    #Cb is the blue-difference chroma component (changes in blue colorfulness)
    return Image.fromarray(imYCbCr[:, :, Cb], "L")



def ych(img):
    YCbCr = list(img.getdata())
    imYCbCr = np.reshape(YCbCr, (img.size[1], img.size[0], 3))
    imYCbCr = imYCbCr.astype(np.uint8)
    # Y is luminosity or light from picture removed so a grayscale
    return Image.fromarray(imYCbCr[:, :, Y], "L")  # L is for 8-bit pixels (mode)

