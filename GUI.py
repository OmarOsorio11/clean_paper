from tkinter import filedialog
import cv2
from tkinter import *
from PIL import Image, ImageTk

#GUI 
def Create_GUI():
    def button_trigger():
        global file_path 
        global imgCv
        file_path = filedialog.askopenfilename(initialdir="/",
        title="Open File",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        entry.insert(0,file_path)
        imgCv=OpenImg(file_path)
        mask=ClearImg(imgCv,150)
        #print(mask)
        ConvertidorImgCvTk(mask)

    def slider_changed_calcular():  
        global mask
        mask=ClearImg(imgCv,Scala.get())
        #print(mask)
        ConvertidorImgCvTk(mask)

    def save_img():
        
        fname = filedialog.asksaveasfilename (title = u'save file ', filetypes = [("PNG", ".png")])
        cv2.imwrite(fname+'.png',mask)

    #covertidor img cv-> tk img
    def ConvertidorImgCvTk(img):
        
        #Rearrang the color channel
        
        #b,g,r = cv2.split(img)
        #img = cv2.merge((r,g,b))

        #img = cv2.merge((img,img,img))
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(im) 
        panelA=Label(image=imgtk)
        panelA.image = imgtk
        panelA.place(x=60, y=150, width=1500, height=900)
        print("ok")

    root = Tk()
    panelA = None
    root.configure(background='white')
    root.geometry('1500x800')
    
    
    
    

    #Widgets 
    label=Label(root,text="Image: ")
    label.place(x=60, y=40, width=100, height=30)
    
    entry=Entry(root)
    entry.place(x=220, y=40, width=200, height=30)
    
    button = Button(root,text="Select Image", command=button_trigger)
    button.place(x=440, y=40, width=100, height=30)

    
    label2=Label(root,text="Parametro: ")
    label2.place(x=660, y=40, width=100, height=30)
    Scala = Scale(root, from_=0, to=255, orient=HORIZONTAL)
    Scala.place(x=780, y=30, width=200, height=50)
    button2 = Button(root,text="Filter", command=slider_changed_calcular)
    button2.place(x=1000, y=40, width=100, height=30)

    button3 = Button(root,text="Save", command=save_img)
    button3.place(x=1120, y=40, width=100, height=30)

    
    root.mainloop()
    
    #Eventos 
    
# abriendo imagen 
def OpenImg(archivoURL):
    image=cv2.imread(archivoURL,1)
    return image

#Analizando img 

def ClearImg(image,parametro):
    imageWhitMask=filterPixel(image,parametro)
    return imageWhitMask


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







def main():
    Create_GUI()

file_path=""
main()