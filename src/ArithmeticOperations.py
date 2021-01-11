import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils


def addTwoImages(picture1, picture2, maxvalue):

    if len(picture1.shape) !=len(picture2.shape):
        raise Exception('Not same dimension')
    if len(picture1.shape) > 3 or len(picture2.shape) > 3 or len(picture1.shape) < 2 or len(picture2.shape) < 2:
        raise Exception('Bad dimension')

    if len(picture1.shape) == 3:
        picture1X, picture1Y, profondeur1 = picture1.shape
        picture2X, picture2Y, profondeur2 = picture2.shape

        if profondeur1 == profondeur2 and picture1X == picture2X and picture1Y == picture2Y:
            result = np.zeros(
                (((picture1X, picture1Y, profondeur1))), dtype='uint8')
            for i in range(picture1X):
                for j in range(picture1Y):
                    for k in range(profondeur1):
                        result[i][j][k] = (int(picture1[i][j][k]) + int(picture2[i][j][k])) if(
                            int(picture1[i][j][k]) + int(picture2[i][j][k])) < maxvalue else maxvalue
            return result
        else:
            raise Exception(
                'Bad Picture Dimension')

    else: #Sans profondeur len(picture1.shape)=2
        picture1X, picture1Y = picture1.shape
        picture2X, picture2Y = picture2.shape

        if  picture1X == picture2X and picture1Y == picture2Y:
            result = np.zeros(((picture1X, picture1Y)), dtype='uint8')
            for i in range(picture1X):
                for j in range(picture1Y):
                        result[i][j] = (int(picture1[i][j]) + int(picture2[i][j])) if(
                            int(picture1[i][j]) + int(picture2[i][j])) < maxvalue else maxvalue
            return result
        else:
            raise Exception(
                'Bad Picture Dimension')



def subTwoImages(picture1, picture2):

    if len(picture1.shape) !=len(picture2.shape):
        raise Exception('Not same dimension')
    if len(picture1.shape) > 3 or len(picture2.shape) > 3 or len(picture1.shape) < 2 or len(picture2.shape) < 2:
        raise Exception('Bad dimension')

    if len(picture1.shape) == 3:
        picture1X, picture1Y, profondeur1 = picture1.shape
        picture2X, picture2Y, profondeur2 = picture2.shape

        if profondeur1 == profondeur2 and picture1X == picture2X and picture1Y == picture2Y:
            result = np.zeros(
                (((picture1X, picture1Y, profondeur1))), dtype='uint8')
            for i in range(picture1X):
                for j in range(picture1Y):
                    for k in range(profondeur1):
                        result[i][j][k] = (int(picture1[i][j][k]) - int(picture2[i][j][k])) if(
                            int(picture1[i][j][k]) - int(picture2[i][j][k])) > 0 else 0
            return result
        else:
            raise Exception(
                'Bad Picture Dimension')

    else: #Sans profondeur len(picture1.shape)=2
        picture1X, picture1Y = picture1.shape
        picture2X, picture2Y = picture2.shape

        if  picture1X == picture2X and picture1Y == picture2Y:
            result = np.zeros(((picture1X, picture1Y)), dtype='uint8')
            for i in range(picture1X):
                for j in range(picture1Y):
                        result[i][j] = (int(picture1[i][j]) - int(picture2[i][j])) if(
                            int(picture1[i][j]) - int(picture2[i][j])) > 0 else 0
            return result
        else:
            raise Exception(
                'Bad Picture Dimension')
