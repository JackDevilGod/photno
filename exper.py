import cv2
import numpy as np

img1 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(1)))]) + str(1) + '.png')
img2 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(505)))]) + str(505) + '.png')

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

h, w = img1.shape
diff = cv2.subtract(img1, img2)
err = np.sum(diff**2)
meanse = err/(float(h*w))
print(meanse)
