"""from skimage import metrics
import cv2

img1 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(1)))]) + str(1) + '.png')
img2 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(2)))]) + str(2) + '.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

similarity_index, _ = metrics.structural_similarity(img1, img2, full=True)

print(similarity_index)"""

import cv2
import matplotlib.pyplot as plt

# Load two images for comparison
image1 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(1)))]) + str(1) + '.png')
image2 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(11)))]) + str(11) + '.png')

# Calculate histograms for both images
hist1 = cv2.calcHist([image1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
hist2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

# Normalize histograms (optional)
hist1 = cv2.normalize(hist1, hist1)
hist2 = cv2.normalize(hist2, hist2)

# Compare histograms using Chi-Square distance
similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
print(similarity)
