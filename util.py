import cv2
import numpy as np
import os, sys
import PIL.Image as Image


def normalize(X, low, high, dtype=None):
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    # normalize to [0...1].
    X = X - float(minX)
    X = X / float((maxX - minX))
    # scale to [low...high].
    X = X * (high - low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)


def read_images(sz=None):
    X, y = [], []
    images = [1, 2, 3, 4, 5, 6]

    for i in images:
        path = 'exercise-' + `i` + '.jpg'

        img = cv2.imread(path, 0) # Read image

        X.append(np.asarray(img, dtype=np.uint8))
        cv2.imshow(path, img)
        k = cv2.waitKey(0)
        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()

    return [X, images]


def asRowMatrix(X):
    if len(X) == 0:
        return np.array([])
    mat = np.empty((0, X[0].size), dtype=X[0].dtype)
    for row in X:
        mat = np.vstack((mat, np.asarray(row).reshape(1, -1)))
    return mat


def asColumnMatrix(X):
    if len(X) == 0:
        return np.array([])
    mat = np.empty((X[0].size, 0), dtype=X[0].dtype)
    for col in X:
        mat = np.hstack((mat, np.asarray(col).reshape(-1, 1)))
    return mat
