import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def gaussian_function (x, sigma): 
	return 1 / (np.sqrt(2 * np.pi) * sigma) * np.e ** (-(np.power((x/sigma), 2) / 2))

def gaussian_kernel(size, sigma=1, verbose=False):
    g_kernel_1d = np.linspace(-(size // 2), size // 2, size);
    for i in range(size):
        g_kernel_1d[i] = gaussian_function(g_kernel_1d[i], sigma)
    print(g_kernel_1d)

kernel_size = int(input('Ingrese el tamaño del kernel: '));
gaussian_kernel(kernel_size, sigma=np.sqrt(kernel_size), verbose=False);
