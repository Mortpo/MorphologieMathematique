import ArithmeticOperations as AOp
import Outils
import Seuillage
import cv2 as CV
import numpy as np

srcPicture = Outils.loadimage("image.jpg")
binaryPicture = Seuillage.grayscale(srcPicture)
binaryPicture = Seuillage.binarisation(binaryPicture,124)

def test_addColorImg_True():
    expected = CV.add(srcPicture,srcPicture)
    result = AOp.addTwoImages(srcPicture,srcPicture,255)
    comparison = result == expected

    assert comparison.all()

def test_addBinaryImg_True():
    expected = CV.add(binaryPicture,binaryPicture)
    result = AOp.addTwoImages(binaryPicture,binaryPicture,255)
    comparison = result == expected

    assert comparison.all()

def test_subColorImg_True():
    expected = srcPicture-srcPicture
    result = AOp.subTwoImages(srcPicture,srcPicture)
    comparison = result == expected

    assert comparison.all()

def test_subBinaryImg_True():
    expected = binaryPicture-binaryPicture
    result = AOp.subTwoImages(binaryPicture,binaryPicture)
    comparison = result == expected

    assert comparison.all()