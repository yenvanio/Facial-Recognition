from Plot import plotImage, plotChannel
from Read import readImage, readSrc
from Convert import convert, ych, cbch, crch
from Binary import binaryConversion, binaryMorphology
from Edge import EdgeDetector, EdgePlot, prepare, twoD

img = readImage(4)
copy = readSrc(4)
edge_array = prepare(4)

img = img.convert('YCbCr')
ycbcr = convert(img)

cbChannel = cbch(img)
crChannel = crch(img)

copy = binaryConversion(copy, cbChannel, crChannel)
copy = binaryMorphology(copy)

edge_array = twoD(edge_array)
edge = EdgeDetector(edge_array)

# cedge_array = twoD(copy)
# cedge = EdgeDetector(cedge_array)
# plotImage(cedge)

plotImage(copy)
plotImage(edge)

