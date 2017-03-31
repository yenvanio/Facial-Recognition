import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def plotChannel(x):
    channel = np.asarray(x)
    plt.hist(channel)
    plt.show()

def plotImage(x):
    plt.imshow(x)
    plt.show()
