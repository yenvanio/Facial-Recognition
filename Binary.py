import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from matplotlib import cm

white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 139]

def binaryConversion(a, cb, cr):
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

