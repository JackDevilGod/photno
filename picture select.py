# import required libraries
import os
from compare_functions import *


def main():
    directory = input("input folder of the images")
    lst_file_names = os.listdir(directory)

    count = 1
    offset = 1

    while count + offset < len(lst_file_names):
        img1 = cv2.imread(os.path.join(directory, lst_file_names[count]))
        img2 = cv2.imread(os.path.join(directory, lst_file_names[count + offset]))
        if (mse(img1, img2) < 50 and
                histogram(img1, img2) < 50):
            os.remove(os.path.join(directory, lst_file_names[count + offset]))
            offset += 1
        else:
            count = count + offset
            offset = 1


if __name__ == "__main__":
    main()
