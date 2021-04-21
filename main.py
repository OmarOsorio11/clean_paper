import cv2
import numpy
import tkinter
from tkinter import filedialog
def getFilePath():
    root = tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
    root.withdraw() #ahora se cierra 
    
    file_path=filedialog.askopenfilename(initialdir="/",
    title="Seleccionae Archivo",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
    return file_path
def filterPixel(img,p):
    #-- Convert to Gray Scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Selecting umbral
    
    height=len(gray[:,1])-1#Heigh
    width=len(gray[1,:])-1#Whit
    for i in range(0,height):
        for j in range(0,width):
            if (gray[i,j]>p):
                gray[i,j]=255
    return gray
#get file path 
print("Selecciona imagen a evaluea")
archivoURL=getFilePath()

#open image
image=cv2.imread(archivoURL,1)

#Filter Pixels


#infinity loop
while(True):
    print("Ingrese el parametro recomendado 150")
    parameter=int(input())
    #Show image whit mask
    imageWhitMask=filterPixel(image,parameter)
    cv2.imshow(archivoURL+"Real",image)
    cv2.imshow(archivoURL,imageWhitMask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Esta bien?\n1. Si\n2. No") 
    status=int(input())
    if (status==1):
        break
    
"""
cv2.imshow(archivoURL,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
