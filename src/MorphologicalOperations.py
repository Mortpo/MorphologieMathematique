import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import ArithmeticOperations as AOp
import Outils
import Seuillage as BW

# Fonction erosion, param : image binaire, param : matrice d'erosion , retour image


def erode(binaryPicture, kernel, centerX, centerY):
    pictureX, pictureY = binaryPicture.shape
    matrixX, matrixY = kernel.shape

    if centerX > matrixX or centerY > matrixY:
        raise Exception(
            'Error in equation centerX > matrixX or centerY > matrixY')

    result = np.uint8(np.zeros((pictureX, pictureY)))
    for i in range(pictureX):
        for j in range(pictureY):
            valide = True

            for x in range(matrixX):
                for y in range(matrixY):

                    # verifie si on est dedans l'image
                    if ((i-centerX) < 0) or ((j-centerY) < 0) or ((i+centerX) > pictureX-1) or ((j+centerY) > pictureY-1) or ((i+x-centerX) > pictureX-1) or ((j+y-centerY) > pictureY-1):
                        valide = False
                    else:
                        # verifie si le filtre est validé
                        if binaryPicture[i+x-centerX][j+y-centerY] != kernel[x][y]:
                            valide = False
                    if not valide:
                        break
            if valide:
                result[i][j] = 1
            else:
                result[i][j] = 0
    return result


def dilate(binaryPicture, kernel, centerX, centerY):

    pictureX, pictureY = binaryPicture.shape
    matrixX, matrixY = kernel.shape

    if centerX > matrixX or centerY > matrixY:
        raise Exception(
            'Error in equation centerX > matrixX or centerY > matrixY')

    result = np.uint8(np.zeros((pictureX, pictureY)))
    for i in range(pictureX):
        for j in range(pictureY):

            if binaryPicture[i][j] == kernel[centerX][centerY]:

                for x in range(matrixX):
                    for y in range(matrixY):

                        if (i+x-centerX >= 0) and (j+y-centerY >= 0) and ((i+x-centerX)<pictureX)and ((j+y-centerY)<pictureY) : #verifie si on est dedans l'image
                            result[i+x-centerX][j+y-centerY] = 1

    return result

def open(binaryPicture, kernel, centerX, centerY):
    result = dilate(erode(binaryPicture, kernel, centerX, centerY), kernel, centerX, centerY)
    return result

def close(binaryPicture, kernel, centerX, centerY):
    result = erode(dilate(binaryPicture, kernel, centerX, centerY), kernel, centerX, centerY)
    return result

def thinning(binaryPicture, iteration, kernel, centerX, centerY):
    i=0
    img1 = binaryPicture.copy()
    thin = np.zeros(img1.shape,dtype='uint8')
    while (CV.countNonZero(img1)!=0 and i < iteration):
        i += 1
        eroded = erode(img1,kernel,1,1)
        openned = open(eroded,kernel,1,1)
        subset = AOp.subTwoImages( eroded,openned)
        thin = AOp.addTwoImages(subset,thin,1)
        img1 = eroded.copy()

    return thin