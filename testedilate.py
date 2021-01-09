from cv2 import erode
from cv2 import dilate
import numpy as np
import matplotlib.pyplot as plt
import Outils
import ArithmeticOperations as AOp
import Seuillage as BW
import MorphologicalOperations as MOp


lena = Outils.loadimage("image.jpg")
lena = BW.grayscale(lena)

binaryPicture =  BW.binarisation(lena,125)
kernel = np.uint8(np.ones((3,3)))
centerX,centerY=1,1

result = MOp.close(binaryPicture,kernel,centerX,centerY)

plt.figure(0)
plt.imshow(binaryPicture,cmap='binary')
plt.figure(1)
plt.imshow(result,cmap='binary')
plt.figure(2)
dilate = dilate(binaryPicture,kernel,iterations = 1)
erode = erode(dilate,kernel,iterations = 1)
plt.imshow(erode,cmap='binary')

plt.show()

                
