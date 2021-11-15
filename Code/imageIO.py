import imageio
import numpy as np
import numpy.random as rnd
import scipy.ndimage as img
import matplotlib.pyplot as plt

import timeit, functools

def imageRead(imgname, pilmode='L', arrtype=np.float):
	"""
	read an image file into a numpy array

	imgname: str
		name of image file to be read
	pilmode: str
		for luminance / intesity images use 'L'
		for RGB color images use 'RGB'
	arrtype: numpy dtype
		use np.float, np.uint8, ...
	"""
	return imageio.imread(imgname, pilmode=pilmode).astype(arrtype)


def imageWrite(arrF, imgname, arrtype=np.uint8):
	"""
	write a numpy array as an image file
	the file type will be inferred from the suffix of imgname

	arrF: array_like
		array to be written
	imgname: str
		name of image file to be written
	arrtype: numpy dtype
		use np.float, np.uint8, ...
	"""
	imageio.imwrite(imgname, arrF.astype(arrtype))


def cut_into_tiles(arrF, tile_size_m=8, tile_size_n=8, max_offset_m=None, max_offset_n=None):
	"""
	Offset every tile by some random margin.
	Allow the tiles to leave the border, by first placing them
	on a larger image, which is then cut down.
	"""
	M, N = arrF.shape
	# Enlarge the canvas in order to freely place the tiles
	if max_offset_m is None:
		max_offset_m = tile_size_m
	if max_offset_n is None:
		max_offset_n = tile_size_n

	# Enlarge the canvas in order to freely place the tiles
	arrG_M = M + 2 * max_offset_m
	arrG_N = N + 2 * max_offset_n
	arrG = np.zeros((arrG_M, arrG_N))

	# Iterate over the image in tiled step size
	for i in range(0, M - tile_size_m, tile_size_m):
		for j in range(0, N - tile_size_n, tile_size_n):

			# Initialize a random offset strength of the current tile
			# Offset value 'max_offset_m' and 'max_offset_n' would yield in no offset,
			# since the target canvas is bigger by this amount!
			io = i + max_offset_m + rnd.randint(-max_offset_m, max_offset_m)
			jo = j + max_offset_n + rnd.randint(-max_offset_n, max_offset_n)

			# Cut the tile and place it with the offset in the returned image
			if arrF[i:i + tile_size_m, j:j + tile_size_n].shape != arrG[io:io + tile_size_m, jo:jo + tile_size_n].shape:
				print("Test")

			arrG[io:io + tile_size_m, jo:jo + tile_size_n] = arrF[i:i + tile_size_m, j:j + tile_size_n]

	# Cut down the enlarged canvas to the original size
	return arrG[max_offset_m:-max_offset_m, max_offset_n:-max_offset_n]


if __name__ == '__main__':
	tile_size_paris = [(8, 8), (32, 32), (32, 7)]
	filename = "../Code/Data/portrait.png"

	arrF = imageRead(filename)

	fig, axs = plt.subplots(1, len(tile_size_paris), figsize=(20, 20))

	for i, (m, n) in enumerate(tile_size_paris):
		# Execute the tile cutter
		arrG = cut_into_tiles(arrF, m, n)

		# Arrange the result
		ax = axs[i]
		ax.imshow(arrG, cmap='gray')
		ax.set_title(f"tile_cut(m={m}, n={n})", fontsize=30)
		ax.set_xticklabels([]);
		ax.set_yticklabels([])

		fig.tight_layout()



	M, N = arrF.shape
	# Enlarge the canvas in order to freely place the tiles
	max_offset_m = offset_strength_m * tile_size_m
	max_offset_n = offset_strength_n * tile_size_n

	# Enlarge the canvas in order to freely place the tiles
	arrG_M = M + 2 * max_offset_m
	arrG_N = N + 2 * max_offset_n
	arrG = np.zeros((arrG_M, arrG_N))