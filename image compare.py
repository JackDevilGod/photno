from skimage import metrics
from skimage import io


def compare_ssim(image1, image2):
    img1 = io.imread(image1)
    img2 = io.imread(image2)

    # Use structural_similarity() function
    similarity = metrics.structural_similarity(img1, img2)
    return similarity


print(compare_ssim(r"",
                   r""))
