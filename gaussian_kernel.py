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

    g_kernel_2d = np.outer(g_kernel_1d.T, g_kernel_1d.T)
    print(g_kernel_2d)

    g_kernel_2d = g_kernel_2d * 1 / g_kernel_2d.max()
    print(g_kernel_2d)

    if verbose == True: 
        plt.imshow(g_kernel_2d)
        plt.title('Kernel de ( {}X{} )'.format(size, size))
        plt.show()
    
    return g_kernel_2d

def gaussian_blur(kernel_size, sigma=1, verbose=False):
    kernel = gaussian_kernel(kernel_size, sigma=np.sqrt(kernel_size), verbose=True);
    return kernel

kernel_size = int(input('Ingrese el tamaño del kernel: '));
gaussian_blur(kernel_size)