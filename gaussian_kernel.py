import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def gaussian_function (x, sigma): 
	return 1 / (np.sqrt(2 * np.pi) * sigma) * np.e ** (-(np.power((x/sigma), 2) / 2))

print(gaussian_function(4, 1))