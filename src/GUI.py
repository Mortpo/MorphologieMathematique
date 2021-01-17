from tkinter import *
from tkinter import ttk
import numpy as np
import Seuillage as BW
import MorphologicalOperations as MOp
import Outils
import cv2 as CV
from tkinter.filedialog import askopenfilename

nbWindow = 0
image = 0
kernel = np.ones((3, 3), dtype='uint8')

pas = Tk()
pas.configure(bg='white')
pas.title("Morphologie Mathematique")
frame = ttk.Frame(pas)
frame.grid()

RadioButtonValue = IntVar()
RadioButtonValue.set(0)

def ShowChoice():
    global kernel
    if RadioButtonValue.get() == 0:
        kernel = np.ones((3, 3), dtype='uint8')
    if RadioButtonValue.get() == 1:
        kernel = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype='uint8')
    if RadioButtonValue.get() == 2:
        kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype='uint8')


rb1 = Radiobutton(frame, text="Rect Kernel", variable=RadioButtonValue, value=0, command=ShowChoice)
rb1.grid(column=1, row=0)

rb2 = Radiobutton(frame, text="Cross Kernel", variable=RadioButtonValue, value=1, command=ShowChoice)
rb2.grid(column=1, row=1)

rb2 = Radiobutton(frame, text="Ellipse Kernel", variable=RadioButtonValue, value=2, command=ShowChoice)
rb2.grid(column=1, row=2)

root = Tk()
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

variable1 = StringVar()


def binarise():
    global image
    root.destroy()
    image = BW.binarisation(image, int(variable1.get()))
    renderimage(image * 255)


def search():
    ttk.Entry(mainframe, width=7, textvariable=variable1).grid(column=2, row=1)
    ttk.Label(mainframe, text="Value").grid(column=1, row=1)
    ttk.Button(mainframe, text="Binarise", command=binarise).grid(column=2, row=13)

    root.mainloop()


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


def grayscale():
    global image
    image = BW.grayscale(image)
    renderimage(image)


def erosion():
    global image
    global kernel
    image = MOp.erode(image, kernel, 1, 1)
    renderimage(image * 255)


def dilatation():
    global image
    global kernel
    image = MOp.dilate(image, kernel, 1, 1)
    renderimage(image * 255)


def ouverture():
    global image
    global kernel
    image = MOp.open(image, kernel, 1, 1)
    renderimage(image * 255)


def fermeture():
    global image
    global kernel
    image = MOp.close(image, kernel, 1, 1)
    renderimage(image * 255)


def thin():
    global image
    global kernel
    image = MOp.thinning(image)
    renderimage(image * 255)


def thick():
    global image
    global kernel
    image = MOp.thickening(image)
    renderimage(image * 255)

button_Import = ttk.Button(frame, text='Import Image', command=importimage)
button_Import.grid(column=0, row=0)

button_GrayScale = ttk.Button(frame, text='BW Image', command=grayscale)
button_GrayScale.grid(column=0, row=1)

button_Binarise = ttk.Button(frame, text='Binarise Image', command=search)
button_Binarise.grid(column=0, row=2)

button_Erosion = ttk.Button(frame, text='Erode Image', command=erosion)
button_Erosion.grid(column=2, row=0)

button_Dilate = ttk.Button(frame, text='Dilate Image', command=dilatation)
button_Dilate.grid(column=2, row=1)

button_Open = ttk.Button(frame, text='Open Image', command=ouverture)
button_Open.grid(column=2, row=2)

button_Close = ttk.Button(frame, text='Close Image', command=fermeture)
button_Close.grid(column=2, row=3)

button_thin = ttk.Button(frame, text='Thin Image', command=thin)
button_thin.grid(column=2, row=4)

button_thick = ttk.Button(frame, text='Thick Image', command=thick)
button_thick.grid(column=2, row=5)

# print(selection, "f")
pas.mainloop()


