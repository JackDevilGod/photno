import cv2
import numpy as np


def mse(img1, img2):
    """
    an image comparing algorithm i copied from the internet
    :param img1:
    :param img2:
    :param folder:
    :return:
    """
    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    meanse = err/(float(h*w))
    return meanse


def histogram(img1, img2):
    """
    a histogram image compare algorithm i copied from the internet
    :param img1:
    :param img2:
    :return:
    """
    # Load two images for comparison

    # Calculate histograms for both images
    hist1 = cv2.calcHist([img1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([img2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

    # Normalize histograms (optional)
    hist1 = cv2.normalize(hist1, hist1)
    hist2 = cv2.normalize(hist2, hist2)

    # Compare histograms using Chi-Square distance
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
