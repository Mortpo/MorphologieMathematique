import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt

def saveimage(nomimage,image):
    CV.imwrite(nomimage , image)

#return image
#attention open CV charge en BGR et non RGB
def loadimage(path):
    return CV.imread(path)

    