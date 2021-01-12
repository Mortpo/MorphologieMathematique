from cv2 import erode
from cv2 import dilate
import cv2 as CV
import numpy as np
import matplotlib.pyplot as plt
import Outils
import ArithmeticOperations as AOp
import Seuillage as BW
import MorphologicalOperations as MOp

img = np.zeros((100,400),dtype='uint8')
font = CV.FONT_HERSHEY_SIMPLEX
CV.putText(img,'TheAILearner',(5,70), font, 2,(255),5,CV.LINE_AA)
img1 = img.copy()

'''srcPicture = Outils.loadimage("image.jpg")
srcPicture = BW.grayscale(srcPicture)
srcPicture = BW.binarisation(srcPicture,125)'''

kernel = np.array([[0,0,0],[1,1,1],[0,0,0]])


thin = np.zeros(img1.shape,dtype='uint8')
img1 = BW.binarisation(img1,120)
img2= img.copy()

#result = MOp.thinning(img1,8,kernel,1,1)

for i in range(9):
    erode = MOp.erode(img1,kernel,1,1)
    openned = MOp.open(erode,kernel,1,1)
    subset = AOp.subTwoImages( erode,openned)
    img = AOp.addTwoImages(subset,img,1)
    img1 = erode.copy()




CV.imshow('original',img2)


CV.imshow('img',img*255) 


CV.waitKey(0)

'''
render = Outils.loadimage("data/image.jpg")
#render2 = CV.resize(render,(1200,1200))
render = BW.grayscale(render)
render= BW.binarisation(render,125)
render = render * 255
CV.imshow("fenetre",render)
CV.waitKey(0)
CV.destroyAllWindows()'''

'''plt.figure(0)
plt.imshow(expected,cmap='binary')   
plt.figure(1)
plt.imshow(result,cmap='binary')
plt.figure(2)
thin= CV.ximgproc.thinning(CV.cvtColor(lena, CV.COLOR_RGB2GRAY))
plt.imshow(thin,cmap='binary')'''

#plt.show()

                
