import numpy as np
import scipy.ndimage as img


def embossV1(arrF):
	"""
	Slowest implementation: Using for loops to iterate through all
	pixels and computing the diagonal difference.
	:param arrF:
	:return:
	"""
	M, N = arrF.shape
	arrG = np.zeros((M, N))

	for i in range(1, M - 1):
		for j in range(1, N - 1):
			arrG[i, j] = 128 + arrF[i + 1, j + 1] - arrF[i - 1, j - 1]
			arrG[i, j] = np.maximum(0, np.minimum(255, arrG[i, j]))

	return arrG


def embossV2(arrF):
	"""
	Fastest implementation: Using numpy splicing to compute the desired
	values as difference between two shifted matrices.
	:param arrF:
	:return:
	"""
	M, N = arrF.shape
	arrG = np.zeros((M, N))

	arrG[1:M - 1, 1:N - 1] = 128 + arrF[2:, 2:] - arrF[:-2, :-2]
	arrG = np.maximum(0, np.minimum(255, arrG))

	return arrG


def embossV3(arrF):
	"""
	Traditional image processing implementation: Using a mask to iterate
	over the pixels and computing the desired values in one sweep.
	:param arrF:
	:return:
	"""
	mask = np.array([[-1, 0, 0],
					 [0, 0, 0],
					 [0, 0, +1]])

	arrG = 128 + img.correlate(arrF, mask, mode='reflect')
	arrG = np.maximum(0, np.minimum(255, arrG))

	return arrG


def embossV4(arrF):
	arrG = 128 + arrF[2:, 2:] - arrF[:-2, :-2]
	arrG[arrG < 0] = 0
	arrG[arrG > 255] = 255

	return arrG


if __name__ == '__main__':
	pass
