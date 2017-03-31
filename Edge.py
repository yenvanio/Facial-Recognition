from skimage.filters import roberts
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from Read import readImage

def EdgeDetector (x):
    return roberts(x)

def EdgePlot(x):
    plt.imshow(x, cmap=plt.cm.gray)
    plt.show()

def prepare(i):
    temp = readImage(i)
    im_grey = temp.convert('L')
    array = np.array(im_grey)
    return array

def twoD(x):
    a = Image.fromarray(x)
    b = a.convert('L')
    c = np.array(b)
    return c
