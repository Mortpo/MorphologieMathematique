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

'''srcPicture = Outils.loadimage("image.jpg")
srcPicture = BW.grayscale(srcPicture)
srcPicture = BW.binarisation(srcPicture,125)'''

kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])


thin = np.zeros(img.shape,dtype='uint8')
BWPicture = BW.binarisation(img,120)
BWCopie= BWPicture.copy()


#result = MOp.thinning(img1,8,kernel,1,1)

for i in range(8):
    erode = MOp.dilate(BWPicture,kernel,1,1)
    openned = MOp.close(erode,kernel,1,1)
    subset = AOp.subTwoImages( erode,openned)
    BWCopie = AOp.addTwoImages(subset,BWCopie,1)
    BWPicture = erode.copy()




CV.imshow('original',img)


CV.imshow('img',BWCopie*255) 


result = MOp.thinning(AOp.inverseBinaryColor(BWCopie) ,8,kernel,1,1)

CV.imshow('result',AOp.addTwoImages(result,img,1)*255) 

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

                
