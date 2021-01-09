import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils

def addTwoImages(picture1,picture2,maxvalue):
    picture1X , picture1Y, profondeur1 = picture1.shape
    picture2X , picture2Y, profondeur2 = picture2.shape

    if profondeur1 == profondeur2 and picture1X == picture2X and picture1Y == picture2Y :
        result = np.uint8(np.zeros(((picture1X,picture1Y,profondeur1))))
        for i in range(picture1X):
                for j in range(picture1Y):
                    for k in range(profondeur1):
                        result[i][j][k] = (int(picture1[i][j][k]) + int(picture2[i][j][k])) if(int(picture1[i][j][k]) + int(picture2[i][j][k])) < maxvalue else  maxvalue
  
        return result
    else:
        raise Exception('Error in equation profondeur1 == profondeur2 and picture1X == picture2X and picture1Y == picture2Y')

def subTwoImages(picture1,picture2):
    picture1X , picture1Y, profondeur1 = picture1.shape
    picture2X , picture2Y, profondeur2 = picture2.shape

    if profondeur1 == profondeur2 and picture1X == picture2X and picture1Y == picture2Y :
        result = np.uint8(np.zeros(((picture1X,picture1Y,profondeur1))))
        for i in range(picture1X):
                for j in range(picture1Y):
                    for k in range(profondeur1):
                        result[i][j][k] = (int(picture1[i][j][k]) - int(picture2[i][j][k])) if(int(picture1[i][j][k]) - int(picture2[i][j][k])) > 0 else  0
  
        return result
    else:
        raise Exception('Error in equation profondeur1 == profondeur2 and picture1X == picture2X and picture1Y == picture2Y')
