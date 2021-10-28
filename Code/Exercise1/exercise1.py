from imageIO import *
from imageEmboss import *
import matplotlib.pyplot as plt


def experiments():
	arrF = imageRead('../Data/portrait.png')
	plt.imshow(arrF / 255, cmap='gray')
	plt.show()

	arrF = imageRead('../Data/asterixRGB.png', pilmode='RGB')
	plt.imshow(arrF / 255)
	plt.show()


def task_1():
	arrF = imageRead('../Data/portrait.png')

	mtds = [embossV1, embossV2, embossV3, embossV4]

	for i, mtd in enumerate(mtds):
		arrG = mtd(arrF)
		imageWrite(arrG, 't1-1-V%d.png' % (i + 1))


if __name__ == '__main__':
	# experiments()
	task_1()
