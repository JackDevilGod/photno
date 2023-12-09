def mse(first, second):
    # load the input images
    img1 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(first)))]) + str(first) + '.png')
    img2 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(second)))]) + str(second) + '.png')

    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    meanse = err/(float(h*w))
    return meanse


def histogram(first, second):
    # Load two images for comparison
    image1 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(first)))]) + str(first) + '.png')
    image2 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(second)))]) + str(second) + '.png')

    # Calculate histograms for both images
    hist1 = cv2.calcHist([image1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

    # Normalize histograms (optional)
    hist1 = cv2.normalize(hist1, hist1)
    hist2 = cv2.normalize(hist2, hist2)

    # Compare histograms using Chi-Square distance
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
