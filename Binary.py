import numpy as np
from scipy import ndimage
from PIL import Image
import scipy as sp

def binaryConversion(a, cb, cr):

    white = [255, 255, 255]
    black = [0, 0, 0]

    for (x, y), pixel in np.ndenumerate(cb):
        if (pixel >= 105 and pixel <= 135):
            a[x, y, :] = white
        else:
            a[x, y, :] = black

    for (x, y), pixel in np.ndenumerate(cr):
        if (pixel >= 140 and pixel <= 165):
            a[x, y, :] = white
        else:
            a[x, y, :] = black

    return a

def binaryMorphology(x):
    ndimage.binary_closing(x).astype(np.int)
    ndimage.binary_dilation(x).astype(np.int)
    ndimage.binary_erosion(ndimage.binary_dilation(x)).astype(np.int)
    return x

def invert(x):
    converted = np.where(x == 255, 0, 255)
    return Image.fromarray(converted.astype(sp.uint8))