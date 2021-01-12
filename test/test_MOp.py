import MorphologicalOperations as MOp
import Outils
import Seuillage
import cv2 as CV
import numpy as np

srcPicture = Outils.loadimage("test.jpg")
srcPicture = Seuillage.grayscale(srcPicture)
srcPicture = Seuillage.binarisation(srcPicture,124)
#kernel = np.ones(((3,3)),dtype="uint8")

kernel = np.array([[0,1,0],[1,1,1],[0,1,0]])

def test_erode_3x3Kernel_True():
    expected = CV.erode(srcPicture,kernel)
    result = MOp.erode(srcPicture,kernel,1,1)
    comparison = result == expected

    assert comparison.all()

def test_dilate_3x3Kernel_True():
    expected = CV.dilate(srcPicture,kernel)
    result = MOp.dilate(srcPicture,kernel,1,1)
    comparison = result == expected

    assert comparison.all()