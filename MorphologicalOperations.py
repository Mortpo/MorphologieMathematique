import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils

#Fonction erosion, param : image binaire, param : matrice d'erosion , retour image
def erode(binaryPicture, erodeMatrix, centerX, centerY):
        pictureX , pictureY, profondeur = binaryPicture.shape
        matrixX , matrixY, profondeur = erodeMatrix.shape
        if centerX > matrixX or centerY > matrixY:
           raise Exception('Error in equation centerX > matrixX or centerY > matrixY')

#result[i][j][0] = binaryPicture[i][j][0]
        result =  np.uint8(np.zeros(((pictureX,pictureY,1))))
        for i in pictureX:
            for j in pictureY:
                if binaryPicture[i][j][0] == erodeMatrix[centerX][centerY]: 
                    for x in matrixX:
                        for y in matrixY:
                            if binaryPicture[i][j][0] == erodeMatrix[x][y] :
                                pass

                

        return result