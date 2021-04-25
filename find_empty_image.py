# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:53:42 2021

@author: 12033
"""

import cv2
import os
import numpy as np

image_path = r"C:\Users\12033\Desktop\Detectron2-Apr24\train"

for file in os.listdir(image_path):
    image = os.path.join(image_path,file)
    im = cv2.imread(image, 0)

    if np.max(im) is None:
        print(file)
        

        
    