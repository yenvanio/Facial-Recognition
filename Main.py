from Plot import plotImage, plotChannel
from Read import readImage, readSrc
from Convert import convert, ych, cbch, crch
from Binary import binaryConversion, binaryMorphology
from Edge import EdgeDetector, EdgePlot, prepare, combine

img = readImage(4)
copy = readSrc(4)
edge_array = prepare(4)

img = img.convert('YCbCr')
ycbcr = convert(img)

cbChannel = cbch(img)
crChannel = crch(img)

copy = binaryConversion(copy, cbChannel, crChannel)
copy = binaryMorphology(copy)

edge = EdgeDetector(edge_array)
# combine(copy, edge)
