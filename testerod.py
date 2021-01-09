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
                    inequal = False
                    if binaryPicture[0][0][0] != erodeMatrix[x][y] :
                        result[i][j][0] = 0
                        inequal = True
            if inequal == False:
                result[i][j][0] = 1

plt.imshow(binaryPicture,cmap='binary')
plt.show()
plt.imshow(result,cmap='binary')
plt.show()
                
