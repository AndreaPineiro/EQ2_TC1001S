import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution

def line_detection(image, verbose=False):
    # Líneas Horizontales
    print('\n')
    print("LÍNEAS HORIZONTALES")
    # Definimos el filtro para la detección de líneas horizontal
    kernel = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]])
    
    # Realizamos la convolución con la imagen y el kernel anterior
    image_lines_x = convolution(image, kernel, False)

    # Se muestra la imagen con la detección de líneas horizontales.
    if verbose:
        plt.imshow(image_lines_x, cmap='gray')
        plt.title("Horizontal Lines")
        plt.show()

    # Líneas verticales
    print('\n')
    print("LÍNEAS VERTICALES")
    kernel = (kernel.T)
    image_lines_y = convolution(image, kernel, False)

    if verbose:
        plt.imshow(image_lines_y, cmap='gray')
        plt.title("Vertical Lines")
        plt.show()

    # Líneas a 45°
    print('\n')
    print("LÍNEAS 45°")
    kernel = np.array([[-1, -1, 2], [-1, 2, -1], [2, -1, -1]])
    image_lines_45_dgrs = convolution(image, kernel, False)

    if verbose:
        plt.imshow(image_lines_45_dgrs, cmap='gray')
        plt.title("45 Degree Lines")
        plt.show()

    # Líneas 135°
    print('\n')
    print("LÍNEAS 135°")
    kernel = np.fliplr(kernel)
    image_lines_135_dgrs = convolution(image, kernel, False)

    if verbose:
        plt.imshow(image_lines_135_dgrs, cmap='gray')
        plt.title("135 Degree Lines")
        plt.show()

    # Obtenemos las líneas juntando las imágenes anteriores.
    print('\n')
    print("LINE DETECTION")
    image_final = image_lines_x + image_lines_y + image_lines_45_dgrs + image_lines_135_dgrs

    if verbose:
        plt.imshow(image_final, cmap='gray')
        plt.title("Line Detection")
        plt.show()

    return

if __name__ == '__main__':
    image = cv2.imread("turquia.jpg")
    line_detection(image, verbose=True)