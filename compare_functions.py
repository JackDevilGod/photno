import cv2
import numpy as np


def mse(img1, img2):
    """
    an image comparing algorithm I copied from the internet
    :param img1:
    :param img2:
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
    a histogram image compare algorithm which compared the color distrubution
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


def detect_and_match_features(img1, img2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector
    orb = cv2.ORB.create()

    # Find the keypoints and descriptors with ORB
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Create a BFMatcher (Brute-Force Matcher)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort them in ascending order of distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Normalize the similarity score between 0 and 100
    total_keypoints = min(len(keypoints1), len(keypoints2))
    similarity_score = (len(matches) / total_keypoints) * 100

    return similarity_score
