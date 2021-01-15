from cv2 import erode
from cv2 import dilate
import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils
import ArithmeticOperations as AOp
import Seuillage as BW
import MorphologicalOperations as MOp

#init
img = np.zeros((100, 400), dtype='uint8')
font = CV.FONT_HERSHEY_SIMPLEX
CV.putText(img, '+ X -', (5, 70), font, 4, (255), 10, CV.LINE_AA)

'''srcPicture = Outils.loadimage("data/image.jpg")
CV.imshow("srcPicture",srcPicture)
srcPicture = BW.grayscale(srcPicture)
BWPicture = BW.binarisation(srcPicture,124)'''


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


BWPicture = BW.binarisation(img, 10)
#BWPicture= AOp.inverseBinaryColor(BWPicture)
CV.imshow('original', BWPicture*255)
kX,kY,kP = kernel.shape
bwX , bwY = BWPicture.shape
tmp = BWPicture.copy()
testdiff =  BWPicture.copy()

#traitement
for a in range(0):
    for i in range(kX):
        
        for x in range(bwX):
            for y in range(bwY):
                valide = True
                if BWPicture[x][y] == 1:
                    
                    for j in range(kY):
                        for k in range(kP):
                            if kernel[i][j][k] != 2:
                                if x+j-1 > 0 and y+k-1 > 0 and x+j-1 < bwX and y+k-1 < bwY:
                                    if kernel[i][j][k] != BWPicture[x+j-1][y+k-1] :
                                        valide = False
                                        break
                                else:
                                    
                                    
                                    if ((x+j-1) <= 0 or (y+k-1) <= 0 or (x+j-1) >= bwX or (y+k-1) >= bwY):
                                        #print(x,y)
                                        valeurPassePartout = kernel[i][j][k]
                                    else:
                                        valeurPassePartout = BWPicture[x+j-1][y+k-1]
                                    
                                    if kernel[i][j][k] != valeurPassePartout :
                                        valide = False
                                        break

                                    
                                        
                    if valide:
                        tmp[x][y] = 0   
        BWPicture=tmp.copy()
    print(a)

kernel2 = np.array([[ 1, 1, 1],[1, 1, 1],[ 1, 1, 1]], dtype='uint8')
resultV1 = MOp.lantuejoul(testdiff,12,kernel2,1,1)

resultV2 = MOp.homotopique(testdiff)


CV.imshow('resultV1', resultV1*255)
CV.imshow('resultV2', resultV2*255)
CV.imshow('Diff', AOp.subTwoImages( resultV1 , resultV2)*255)

CV.waitKey(0)
