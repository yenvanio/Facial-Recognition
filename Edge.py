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

# def combine(copy, edge):
#     img1 = Image.fromarray(copy)
#     img2 = Image.fromarray(edge)
#
#     img = img1.paste(img2, (0,0))
#
#     plt.imshow(img)
#     plt.show()
