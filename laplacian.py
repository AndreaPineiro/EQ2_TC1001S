import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
from convolution import convolution

def laplacian(image, verbose=False):
    #se define el kernel usado para este filtro
    kernel = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, -16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])

    #se hace la convolucion usando el kernel declarado
    image_lap = convolution(image, kernel, False)

    #se muestra la imagen
    if verbose:
        plt.imshow(image_lap, cmap='gray')
        plt.title('laplacian')
        plt.show()

    return image



