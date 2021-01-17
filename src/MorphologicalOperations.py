import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import ArithmeticOperations as AOp
import Outils
import Seuillage as BW

# Fonction erosion, param : image binaire, param : matrice d'erosion , retour image


def erode(binaryPicture, kernel):
    pictureX, pictureY = binaryPicture.shape
    matrixX, matrixY = kernel.shape
    centerX, centerY = 1, 1

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
                        if binaryPicture[i+x-centerX][j+y-centerY] != kernel[x][y] and kernel[x][y]==1:
                            valide = False
                    if not valide:
                        break
            if valide:
                result[i][j] = 1
            else:
                result[i][j] = 0
    return result


def dilate(binaryPicture, kernel):

    pictureX, pictureY = binaryPicture.shape
    matrixX, matrixY = kernel.shape
    centerX, centerY = 1, 1

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

def open(binaryPicture, kerne):
    result = dilate(erode(binaryPicture, kernel), kernel)
    return result

def close(binaryPicture, kernel):
    result = erode(dilate(binaryPicture, kernel), kernel)
    return result

def thinning(binaryPicture):

    kernel = np.array(
    [[[1, 1, 1], [2, 1, 2], [0, 0, 0]], 
    [[1, 1, 2], [1, 1, 0], [2, 0, 0]],
    [[1, 2, 0], [1, 1,0], [1, 2, 0]], 
    [[2, 0, 0], [1, 1, 0], [1,1, 2]], 
    [[0, 0, 0], [ 2, 1, 2], [1, 1,1]],
    [[0, 0, 2], [0, 1, 1], [2, 1, 1]], 
    [[0, 2, 1], [0, 1, 1], [0, 2, 1]],
    [[2, 1, 1], [0, 1, 1], [0, 0, 2]]]
    )
    kX,kY,kP = kernel.shape
    bwX , bwY = binaryPicture.shape
    tmp = binaryPicture.copy()
    
    for i in range(kX):
        
        for x in range(bwX):
            for y in range(bwY):
                valide = True
                if binaryPicture[x][y] == 1:
                    
                    for j in range(kY):
                        for k in range(kP):
                            if kernel[i][j][k] != 2:
                                if x+j-1 > 0 and y+k-1 > 0 and x+j-1 < bwX and y+k-1 < bwY:
                                    if kernel[i][j][k] != binaryPicture[x+j-1][y+k-1] :
                                        valide = False
                                        break
                                else:
                                    
                                    
                                    if ((x+j-1) <= 0 or (y+k-1) <= 0 or (x+j-1) >= bwX or (y+k-1) >= bwY):
                                        valeurPassePartout = kernel[i][j][k]
                                    else:
                                        valeurPassePartout = binaryPicture[x+j-1][y+k-1]
                                    
                                    if kernel[i][j][k] != valeurPassePartout :
                                        valide = False
                                        break

                                    
                                        
                    if valide:
                        tmp[x][y] = 0   
        binaryPicture=tmp.copy()

    return binaryPicture


def thickening(binaryPicture):

    kernel = np.array(
    [[[1, 1, 1], [2, 0, 2], [0, 0, 0]], 
    [[1, 1, 2], [1, 0, 0], [2, 0, 0]],
    [[1, 2, 0], [1, 0,0], [1, 2, 0]], 
    [[2, 0, 0], [1, 0, 0], [1,1, 2]], 
    [[0, 0, 0], [ 2, 0, 2], [1, 1,1]],
    [[0, 0, 2], [0, 0, 1], [2, 1, 1]], 
    [[0, 2, 1], [0, 0, 1], [0, 2, 1]],
    [[2, 1, 1], [0, 0, 1], [0, 0, 2]]]
    )
    kX,kY,kP = kernel.shape
    bwX , bwY = binaryPicture.shape
    tmp = binaryPicture.copy()
    
    for i in range(kX):
        
        for x in range(bwX):
            for y in range(bwY):
                valide = True
                if binaryPicture[x][y] == 0:
                    
                    for j in range(kY):
                        for k in range(kP):
                            if kernel[i][j][k] != 2:
                                if x+j-1 > 0 and y+k-1 > 0 and x+j-1 < bwX and y+k-1 < bwY:
                                    if kernel[i][j][k] != binaryPicture[x+j-1][y+k-1] :
                                        valide = False
                                        break
                                else:
                                    
                                    
                                    if ((x+j-1) <= 0 or (y+k-1) <= 0 or (x+j-1) >= bwX or (y+k-1) >= bwY):
                                        valeurPassePartout = kernel[i][j][k]
                                    else:
                                        valeurPassePartout = binaryPicture[x+j-1][y+k-1]
                                    
                                    if kernel[i][j][k] != valeurPassePartout :
                                        valide = False
                                        break

                                    
                                        
                    if valide:
                        tmp[x][y] = 1   
        binaryPicture=tmp.copy()

    return binaryPicture

def lantuejoul(binaryPicture,indice,kernel):

    centerX, centerY = 1, 1
    union = np.zeros((binaryPicture.shape))

    for i in range(indice):
        eroded = erode(binaryPicture,kernel,centerX,centerY)
        opened = open(eroded,kernel,centerX,centerY)
        subpic = AOp.subTwoImages(eroded,opened)
        union = AOp.addTwoImages(union,subpic,1)
        binaryPicture = eroded
    return union

def homotopique(binaryPicture):
    i=0
    kernel = np.array([[ 1, 1, 1],[1, 1, 1],[ 1, 1, 1]], dtype='uint8')
    eroded = binaryPicture.copy()
    while (CV.countNonZero(eroded)!=0) and i<20:
        tmp = binaryPicture.copy()
        i+=1
        binaryPicture = thinning(binaryPicture)
        eroded = erode(binaryPicture,kernel,1,1)
        print(i)
    return tmp 