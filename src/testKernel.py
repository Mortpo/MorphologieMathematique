import MorphologicalOperations as MOp
import Outils
import Seuillage
import cv2 as CV
import numpy as np

srcPicture = Outils.loadimage("data/image.jpg")
CV.imshow('srcPicture',srcPicture)
srcPicture = Seuillage.grayscale(srcPicture)
srcPicture = Seuillage.binarisation(srcPicture,124)

kernel = np.array([[ 0, 1, 0],[1, 1, 1],[ 0, 1, 0]], dtype='uint8')

expected = CV.erode(srcPicture,kernel)
result = MOp.erode(srcPicture,kernel,1,1)

CV.imshow('expected',expected*255)
CV.imshow('result',result*255) 

CV.waitKey(0)