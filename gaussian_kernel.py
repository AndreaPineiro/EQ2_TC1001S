import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import convolution

# Regresa un valor de la función G(x) que servirá para el kernel
def gaussian_function (x, sigma): 
	return 1 / (np.sqrt(2 * np.pi) * sigma) * np.e ** (-(np.power((x/sigma), 2) / 2))

# Crea y devuelve el kernel de 2 dimensiones
def gaussian_kernel(size, sigma=1, verbose=False):
    g_kernel_1d = np.linspace(-(size // 2), size // 2, size);
    
    # Convierte los valores de g_kernel_1d a valores retornados por la funcion de gauss
    for i in range(size):
        g_kernel_1d[i] = gaussian_function(g_kernel_1d[i], sigma)
    
    # Hace el producto punto del 1d kernel y crea una matriz de 2x2 y cambia valores
    g_kernel_2d = np.outer(g_kernel_1d.T, g_kernel_1d.T)
    g_kernel_2d = g_kernel_2d * 1 / g_kernel_2d.max()
    
    # Despliega el kernel 2x2
    if verbose == True: 
        plt.imshow(g_kernel_2d)
        plt.title('Kernel de ( {}X{} )'.format(size, size))
        plt.show()
    
    return g_kernel_2d

# Funcion "main" para llamar a la funcion de gaussian kernel y define el sigma
def gaussian_blur(kernel_size, sigma=1, verbose=False):
    return gaussian_kernel(kernel_size, sigma=np.sqrt(kernel_size), verbose=False);
    
