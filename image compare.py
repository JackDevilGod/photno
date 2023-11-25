# import required libraries
import cv2
import numpy as np
import os


def mse(first, second):
    # load the input images
    img1 = cv2.imread('1-' + "".join(["0" for _ in range(4 - first)]) + str(first) + '.png')
    img2 = cv2.imread('1-' + "".join(["0" for _ in range(4 - second)]) + str(second) + '.png')

    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    meanse = err/(float(h*w))
    return meanse


amount_picutes = int(input("how many images are there"))
count = 1
offset = 1
# 50% match is 124.5
while count < amount_picutes:
    if mse(count, count + offset) < 124.5:
        os.remove('1-' + "".join(["0" for _ in range(4 - count)]) + str(count) + '.png')
        offset += 1
    else:
        count = count + offset
        offset = 1

    if count + offset == amount_picutes:
        count = amount_picutes
