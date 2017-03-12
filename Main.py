import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import copy


img = Image.open("exercise-4.jpg")
img = img.convert('YCbCr')
ycbcr = np.array(img)

Y = 0
Cb = 1
Cr = 2

YCbCr = list(img.getdata())
imYCbCr = np.reshape(YCbCr, (img.size[1], img.size[0], 3))
imYCbCr = imYCbCr.astype(np.uint8)

yChannel = Image.fromarray(imYCbCr[:,:,Y], "L") #L is for 8-bit pixels (mode)
cbChannel = Image.fromarray(imYCbCr[:,:,Cb], "L")
crChannel = Image.fromarray(imYCbCr[:,:,Cr], "L")

plt.imshow(cbChannel)
plt.imshow(crChannel)
plt.show()

#Show images with effect of each channel
# yChannel.show()
# cbChannel.show()
# crChannel.show()







