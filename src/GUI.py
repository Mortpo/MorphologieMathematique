from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import Seuillage as BW
import MorphologicalOperations as MOp
import Outils
import cv2 as CV
from tkinter.filedialog import askopenfilename

nbWindow = 0
image = 0
kernel = np.ones((3,3),dtype='uint8')




def renderimage(picture):
    global nbWindow
    CV.namedWindow(str(nbWindow), CV.WINDOW_NORMAL)
    CV.imshow(str(nbWindow), picture)
    nbWindow = nbWindow + 1


def importimage():
    global image
    filename = askopenfilename()
    image = Outils.loadimage(filename)
    renderimage(image)


def binarise():
    global image
    image = BW.binarisation(image, 128)
    renderimage(image*255)


def grayscale():
    global image
    image = BW.grayscale(image)
    renderimage(image)


def erosion():
    global image
    global kernel
    image = MOp.erode(image, kernel, 1, 1)
    renderimage(image*255)

def dilatation():
    global image
    global kernel
    image = MOp.dilate(image, kernel, 1, 1)
    renderimage(image*255)

def ouverture():
    global image
    global kernel
    image = MOp.open(image, kernel, 1, 1)
    renderimage(image*255)

def fermeture():
    global image
    global kernel
    image = MOp.close(image, kernel, 1, 1)
    renderimage(image*255)

#rajouter espace vide
pas = Tk()
pas.title("Morphologie Mathematique")
frame = ttk.Frame(pas)
frame.grid()

button_Import = ttk.Button(frame, text='Import Image', command=importimage)
button_Import.grid(column=0, row=0)

button_GrayScale = ttk.Button(
    frame, text='BW Image', command=grayscale)
button_GrayScale.grid(column=0, row=1)

button_Binarise = ttk.Button(frame, text='Binarise Image', command=binarise)
button_Binarise.grid(column=0, row=2)

button_Erosion = ttk.Button(frame, text='Erode Image', command=erosion)
button_Erosion.grid(column=2, row=0)

button_Dilate = ttk.Button(frame, text='Dilate Image', command=dilatation)
button_Dilate.grid(column=2, row=1)

button_Open = ttk.Button(frame, text='Open Image', command=ouverture)
button_Open.grid(column=2, row=2)

button_Close = ttk.Button(frame, text='Close Image', command=fermeture)
button_Close.grid(column=2, row=3)

button_thin = ttk.Button(frame, text='Thin Image', command="")
button_thin.grid(column=2, row=4)

button_thick = ttk.Button(frame, text='Thick Image', command="")
button_thick.grid(column=2, row=5)


pas.mainloop()