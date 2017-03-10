from subspace import pca
from util import normalize, asRowMatrix, read_images

if __name__ == '__main__':

    # read images
    [X, y] = read_images()

    #do a pca
    [D, W, mu] = pca(asRowMatrix(X), y)

