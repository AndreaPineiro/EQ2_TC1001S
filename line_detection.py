import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution

def line_detection(image, verbose=False):
    # Definimos el filtro para la detección de líneas horizontal
    kernel = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]])

    # Realizamos la convolución con la imagen y el kernel anterior
    image_lines_x = convolution(image, kernel, False)

    # Se muestra la imagen con la detección de líneas horizontales.
    if verbose:
        plt.imshow(image_lines_x, cmap='gray')
        plt.title("Horizontal Lines")
        plt.show()

    kernel = (kernel.T)
    image_lines_y = convolution(image, kernel, False)

    if verbose:
        plt.imshow(image_lines_y, cmap='gray')
        plt.title("Vertical Lines")
        plt.show()

    return

if __name__ == '__main__':
    image = cv2.imread("turquia.jpg")
    line_detection(image, verbose=True)