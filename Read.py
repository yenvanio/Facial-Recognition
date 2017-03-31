import cv2
from PIL import Image


def readImage(i):
    return Image.open("exercise-"+`i`+".jpg")

def readSrc(i):
    return cv2.imread("exercise-"+`i`+".jpg")


