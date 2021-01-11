import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils


#Prend en paramètre une image de couleur et renvoie un tableau représentant une image de gris
def grayscale(picture):
    pictureX , pictureY, profondeur = picture.shape
    result =  np.zeros((pictureX,pictureY),dtype='uint8')
    #formule de luminosité Luminance = 0,2126 × Rouge + 0,7152 × Vert + 0,0722 × Bleu
    #attention open CV charge en BGR et non RGB
    for i in range(pictureX):
        for j in range(pictureY):
            result[i][j] = int(((picture[i][j][2])*0.2126 + (picture[i][j][1])*0.7152 + (picture[i][j][0])*0.0722) ) 
    return result

#Prend en paramètre une image de couleur et un seuil puis binarise en fonction du seuil
def binarisation(picture,threshold):
    pictureX , pictureY = picture.shape
    result = np.zeros((pictureX,pictureY),dtype='uint8')
    for i in range(pictureX):
        for j in range(pictureY):
            result[i][j] = 1 if picture[i][j]>threshold else 0
    return result
