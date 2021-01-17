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


labelspace = Label(frame, text="      ")
labelspace.grid(column=1, row=0)
labelspace2 = Label(frame, text="      ")
labelspace2.grid(column=3, row=0)

labelchoice = Label(frame, text="Choisir le kernel ", justify=LEFT, padx=20)
labelchoice.grid(column=2, row=0)

rb1 = Radiobutton(frame, text="Rect Kernel", variable=RadioButtonValue, value=0, command=ShowChoice)
rb1.grid(column=2, row=1)

rb2 = Radiobutton(frame, text="Cross Kernel", variable=RadioButtonValue, value=1, command=ShowChoice)
rb2.grid(column=2, row=2)

rb2 = Radiobutton(frame, text="Ellipse Kernel", variable=RadioButtonValue, value=2, command=ShowChoice)
rb2.grid(column=2, row=3)

entryBValue = Entry(frame, width=7, text="122")
entryBValue.grid(column=0, row=3)
entryBValue.insert(0, "122")


def binarise():
    global image
    value = int(entryBValue.get())
    if value > 255:
        value = 255
    if value < 0:
        value = 0
    image = BW.binarisation(image, value)
    renderimage(image * 255)


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
    image = MOp.erode(image, kernel)
    renderimage(image * 255)


def dilatation():
    global image
    global kernel
    image = MOp.dilate(image, kernel)
    renderimage(image * 255)


def ouverture():
    global image
    global kernel
    image = MOp.open(image, kernel)
    renderimage(image * 255)


def fermeture():
    global image
    global kernel
    image = MOp.close(image, kernel)
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


def lantuejoul():
    global image
    global kernel
    image = MOp.lantuejoul(image, kernel) 
    renderimage(image*255)


def Homothopique():
    global image
    global kernel
    image = MOp.homotopique(image) 
    renderimage(image * 255)


button_Import = ttk.Button(frame, text='Import Image', command=importimage)
button_Import.grid(column=0, row=0)

button_GrayScale = ttk.Button(frame, text='BW Image', command=grayscale)
button_GrayScale.grid(column=0, row=1)

button_Binarise = ttk.Button(frame, text='Binarise Image', command=binarise)
button_Binarise.grid(column=0, row=2)

button_Erosion = ttk.Button(frame, text='Erode Image', command=erosion)
button_Erosion.grid(column=4, row=0)

button_Dilate = ttk.Button(frame, text='Dilate Image', command=dilatation)
button_Dilate.grid(column=4, row=1)

button_Open = ttk.Button(frame, text='Open Image', command=ouverture)
button_Open.grid(column=4, row=2)

button_Close = ttk.Button(frame, text='Close Image', command=fermeture)
button_Close.grid(column=4, row=3)

button_thin = ttk.Button(frame, text='Thin Image', command=thin)
button_thin.grid(column=4, row=4)

button_thick = ttk.Button(frame, text='Thick Image', command=thick)
button_thick.grid(column=4, row=5)

buttonLantuejoul = Button(frame, text="Lantuejoul", command=lantuejoul)
buttonLantuejoul.grid(column=0, row=5)

buttonHomotopique = Button(frame, text="Homothopique", command=Homothopique)
buttonHomotopique.grid(column=2, row=5)


# print(selection, "f")
pas.mainloop()


