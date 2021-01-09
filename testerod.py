import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils
import ArithmeticOperations as AOp
import Seuillage as BW

#result[i][j][0] = binaryPicture[i][j][0]

binaryPicture =  BW.binarisation(Outils.loadimage("test.jpg"),125)
erodeMatrix = np.ones((3,3))
centerX,centerY=1,1

pictureX , pictureY, profondeur = binaryPicture.shape
matrixX , matrixY = erodeMatrix.shape
if centerX > matrixX or centerY > matrixY:
    raise Exception('Error in equation centerX > matrixX or centerY > matrixY')

result =  np.uint8(np.zeros(((pictureX,pictureY,1))))
for i in range(pictureX):
    for j in range(pictureY):


            for x in range(matrixX):
                for y in range(matrixY):
                    valide = True
                    if ((i-centerX) <= 0) or ((j-centerY)<=0) or ((i+centerX) >= pictureX) or ((j+centerY)>=pictureY): #verifie si on est dedans l'image
                        valide = False
                    print(i, j , i+x-centerX ,i+y-centerY)
                    if valide == True and binaryPicture[i+x-centerX][i+y-centerY] != erodeMatrix[x][y] : #verifie si le filtre est vilidé
                        valide = False
            if valide == True:
                result[i][j][0] = 0
            else:
                result[i][j][0] = 1


plt.figure(0)
plt.imshow(binaryPicture,cmap='binary')
plt.figure(1)
plt.imshow(result,cmap='binary')
plt.show()

                
