from imageIO import *
from imageEmboss import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
	arrF = imageRead('../Data/portrait.png')
	plt.imshow(arrF / 255, cmap='gray')
	plt.show()


	# arrF = imageRead('../Data/portrait.png')
	#
	# mtds = [embossV1, embossV2, embossV3, embossV4]
	#
	# for i, mtd in enumerate(mtds):
	# 	arrG = mtd(arrF)
	# 	imageWrite(arrG, 't1-1-V%d.png' % (i + 1))
