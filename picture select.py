# import required libraries
import os
from compare_functions import *


def main():
    directory = input("input folder of the images")
    lst_file_names = os.listdir(directory)

    count = 1
    offset = 1
    # 50% match is 124.5 histogram
    while count < len(lst_file_names):
        img1 = cv2.imread(directory + lst_file_names[count])
        img2 = cv2.imread('1-' + "".join(["0" for _ in range(5 - len(str(second)))]) + str(second) + '.png')
        if (mse(lst_file_names[count], lst_file_names[count + offset], directory) < 25 and
                histogram(lst_file_names[count], lst_file_names[count + offset], directory) < 50):
            os.remove(lst_file_names[count + offset])
            offset += 1
        else:
            count = count + offset
            offset = 1


if __name__ == "__main__":
    main()
