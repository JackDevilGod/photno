# import required libraries
import cv2
import numpy as np

n = 0
# load the input images
img1 = cv2.imread('1-' + "".join(["0" for _ in range(4-n)]) + str(n) + '.png')
img2 = cv2.imread('1-' + "".join(["0" for _ in range(4-n)]) + str(n) + '.png')

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img_1, img_2):
    h, w = img1.shape
    diff = cv2.subtract(img_1, img_2)
    err = np.sum(diff**2)
    meanse = err/(float(h*w))
    return meanse


# 50% match is 124.5
error = mse(img1, img2)
print(error)
