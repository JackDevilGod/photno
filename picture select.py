# import required libraries
import cv2
import numpy as np
import os
from functions import *

amount_picutes = int(input("how many images are there"))
count = 1
offset = 1
# 50% match is 124.5
while count < amount_picutes:
    if mse(count, count + offset) < 25 and histogram(count, count + offset) < 50:
        os.remove('1-' + "".join(["0" for _ in range(5 - len(str(count + offset)))]) + str(count + offset) + '.png')
        offset += 1
    else:
        count = count + offset
        offset = 1

    if count + offset >= amount_picutes:
        count = amount_picutes
