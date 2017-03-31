from skimage.filters import roberts
from matplotlib import pyplot as plt
from numpy import*
from Read import readImage

def EdgeDetector (x):
    return roberts(x)

def EdgePlot(x):
    fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                           figsize=(8, 4))

    ax[0].imshow(x, cmap=plt.cm.gray)
    ax[0].set_title('Roberts Edge Detection')
    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()

def prepare(i):
    temp = readImage(i)
    temp = temp.convert('1')  # Convert to black&white
    A = array(temp)  # Creates an array, white pixels==True and black pixels==False
    return A