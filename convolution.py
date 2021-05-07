# Se importan todas las librerías necesarias
import numpy as np
from random import *
import cv2
import matplotlib.pyplot as plt

# La función de convolución recibe la imagen y el kernel
def convolution(image, kernel, verbose=False):
    # Si tiene 3 dimensiones la convierte en escala de grises.
    if len(image.shape) == 3:
        print("Found 3 Dimensions: {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Chanel. Shape {}".format(image.shape))
    else:
        print("Image Shape: {}".format(image.shape))

    # Si verbose esta true se imprime la imagen estándar.
    if verbose:
        plt.imshow(image, cmap='gray')
        plt.title("Original Image")
        plt.show()

    # Se obtienen los tamaños de la matriz imagen
    image_row, image_col = image.shape
    # Se obtienen los tamaños de la matriz kernel
    kernel_row, kernel_col = kernel.shape
    
    # Se crea una matriz vacía de respuesta, con el mismo tamaño de la imagen anterior
    res = np.zeros(image.shape)

    # Se obtiene el padding que debe haber de alto y ancho para tener el mismo tamaño de la imagen anterior
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    # Creamos una matriz con la imagen y el padding, y colocamos los valores de la imagen en el centro.
    padded_image = np.zeros((image_row + (pad_height*2), image_col + (pad_width*2)))
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    if verbose:
        plt.imshow(padded_image, cmap='gray')
        plt.title("Padded Image")
        plt.show()
    
    # Este ciclo itera para recorrer cada una de las casillas en la matriz del resultado
    for matrix_row in range (image_row):
        for matrix_col in range (image_col):
            #np.sum suma el resultado después de hacer la multiplicacion de ambas matrices.
            res[matrix_row, matrix_col] = np.sum(kernel * padded_image[matrix_row: matrix_row + kernel_row, matrix_col: matrix_col + kernel_col])
    
    # Se realiza el plot de la Imagen usando el Kernel
    if verbose:
        plt.imshow(res, cmap='gray')
        plt.title("Blur Image using {}X{} Gaussian Kernel".format(kernel_row, kernel_col))
        plt.show()

    return res

if __name__ == '__main__':
    # Se obtiene la imagen con cv2 y se inicializa la matriz del kernel
    image = cv2.imread("turquia.jpg")
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Se manda llamar la función de convolucion con la imagen y el kernel
    image = convolution(image, kernel, verbose=True)