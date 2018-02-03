import cv2
import numpy as np
from Tkinter import *
import Tkinter
from tkFileDialog import askopenfilename
import tkMessageBox


def register():

    query = Tkinter.Toplevel()
    query.title("Enter Information")
    query.geometry('250x180+0+0')

    QL1 = Tkinter.Label(query, text="First Name:")
    QL1.grid(sticky=E)
    QE1 = Tkinter.Entry(query, bd=2)
    QE1.grid(row=0, column=1)

    QL2 = Tkinter.Label(query, text="Last Name:")
    QL2.grid(sticky=E)
    QE2 = Tkinter.Entry(query, bd=2)
    QE2.grid(row=1, column=1)

    QL3 = Tkinter.Label(query, text="SSN:")
    QL3.grid(sticky=E)
    QE3 = Tkinter.Entry(query, bd=2)
    QE3.grid(row=2, column=1)

    #self.btype = StringVar(query)
    #self.btype.set("A")

    QL4 = Tkinter.Button(query, text="capture", command=helloCallBack)
    QL4.grid(row=5, column=1, pady=10)
    #QE4 = Tkinter.OptionMenu(query, self.btype, "A", "B", "AB", "O")
    #QE4.config(bg="white")
    #QE4.grid(row=3, column=1, sticky=W)

    #self.gender = StringVar(query)
    #self.gender.set("Male")		

    QL5 = Tkinter.Button(query, text="browse", command=helloCallBack)
    QL5.grid(row=6, column=1, pady=10)
    #QE5 = Tkinter.OptionMenu(query, self.gender, "Male", "Female")
    #QE5.config(bg="white")
    #QE5.grid(row=4, column=1, sticky=W)

    button = Tkinter.Button(query, text="submit",bg="white")
    button.grid(row=8, column=1, pady=10)

def verify():
    tkMessageBox.showinfo( "Image", "Selec")
    filename = askopenfilename()
    im = cv2.imread(filename)
    img = cv2.medianBlur(im,5)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # detect circles
    gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 5)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,30.0,param1=50,param2=110,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))

    # draw mask
    mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)  # mask is only 
    for i in circles[0, :]:
        cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

    # get first masked value (foreground)
    fg = cv2.bitwise_and(img, img, mask=mask)


    #cv2.imshow("godady",fg)
    cv2.imwrite("p.png",fg)
    cv2.waitKey(0)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # detect circles
    gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 5)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2,100.0,param1=30,param2=150,minRadius=90,maxRadius=140)
    circles = np.uint16(np.around(circles))
    
    # draw mask
    mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)  # mask is only 
    for i in circles[0, :]:
        cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

    # get first masked value (foreground)
    fg = cv2.bitwise_and(img, img, mask=mask)


    #cv2.imshow("masked",fg)
    cv2.imwrite("m.png",fg)


    pic1 = cv2.imread('p.png')
    pic2 = cv2.imread('m.png')
    mask_ab = cv2.bitwise_xor(pic2, pic1)

    #cv2.imshow('abc',mask_ab)
    cv2.imwrite('final.png',mask_ab)


    cv2.waitKey(0)

    img = cv2.imread('final.png')

    
    #img2 = cv2.logPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
    img3 = cv2.linearPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
    
    #cv2.imshow('before', img)
    #cv2.imshow('logpolar', img2)
    #cv2.imshow('linearpolar', img3)

    cv2.imwrite('polar.png',img3)
    
    cv2.waitKey(0)


    def build_filters():
     filters = []
     ksize = 31
     for theta in np.arange(0, np.pi, np.pi / 16):
         kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
         kern /= 1.5*kern.sum()
         filters.append(kern)
     return filters
 
    def process(img, filters):
     accum = np.zeros_like(img)
     for kern in filters:
         fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
         np.maximum(accum, fimg, accum)
     return accum
 
    if __name__ == '__main__':
     img=cv2.imread('polar.png')
 
     filters = build_filters()
 
     res1 = process(img, filters)
     cv2.imshow('result', res1)
     cv2.imwrite("gh.png",res1)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

     import image_slicer
     xy=image_slicer.slice('polar.png', 16)
     yz=image_slicer.slice('gh.png', 16)

     cv2.waitKey(0)

    import sys


    img = cv2.imread('polar_01_01.png')
    px1 = img[64, 32]


    img = cv2.imread('gh_01_01.png')
    px2 = img[64, 32]

    if(px1[1]>=px2[1]):
        sys.stdout=open("test.txt","w")
        print ("1")
    
    else:
        sys.stdout=open("test.txt","w")
        print("0")
    
    

    img = cv2.imread('polar_01_02.png')
    px3 = img[64, 32]


    img = cv2.imread('gh_01_02.png')
    px4 = img[64, 32]

    if(px3[1]>=px4[1]):
        sys.stdout=open("test.txt","a")
        print("1")
    else:
        sys.stdout=open("test.txt","a")
        print("0")
    

    img = cv2.imread('polar_01_03.png')
    px5 = img[64, 32]


    img = cv2.imread('gh_01_03.png')
    px6 = img[64, 32]

    if(px5[1]>=px6[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('polar_01_04.png')
    px7 = img[64, 32]


    img = cv2.imread('gh_01_04.png')
    px8 = img[64, 32]

    if(px7[1]>=px8[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_02_01.png')
    px9 = img[64, 32]


    img = cv2.imread('polar_02_01.png')
    px10 = img[64, 32]

    if(px9[1]>=px10[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_02_02.png')
    px11 = img[64, 32]


    img = cv2.imread('polar_02_02.png')
    px12 = img[64, 32]

    if(px11[1]>=px12[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_02_03.png')
    px13 = img[64, 32]


    img = cv2.imread('polar_02_03.png')
    px14 = img[64, 32]

    if(px13[1]>=px14[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")
    img = cv2.imread('polar_02_04.png')
    px15 = img[64, 32]


    img = cv2.imread('gh_02_04.png')
    px16 = img[64, 32]

    if(px15[1]>=px16[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_03_01.png')
    px17 = img[64, 32]


    img = cv2.imread('polar_03_01.png')
    px18 = img[64, 32]

    if(px17[1]>=px18[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('polar_03_02.png')
    px19 = img[64, 32]


    img = cv2.imread('gh_03_02.png')
    px20 = img[64, 32]

    if(px19[1]>=px20[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_03_03.png')
    px21 = img[64, 32]


    img = cv2.imread('polar_03_03.png')
    px22 = img[64, 32]

    if(px21[1]>=px22[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('polar_03_04.png')
    px23 = img[64, 32]


    img = cv2.imread('gh_03_04.png')
    px24 = img[64, 32]

    if(px23[1]>=px24[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_04_01.png')
    px25 = img[64, 32]


    img = cv2.imread('polar_04_01.png')
    px26 = img[64, 32]

    if(px25[1]>=px26[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_04_02.png')
    px27 = img[64, 32]


    img = cv2.imread('polar_04_02.png')
    px28 = img[64, 32]

    if(px27[1]>=px28[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('polar_04_03.png')
    px29 = img[64, 32]


    img = cv2.imread('gh_04_03.png')
    px30 = img[64, 32]

    if(px29[1]>=px30[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")

    img = cv2.imread('gh_04_04.png')
    px31 = img[64, 32]


    img = cv2.imread('polar_04_04.png')
    px32 = img[64, 32]

    if(px31[1]>=px32[1]):
        sys.stdout=open("test.txt","a")
        print ("1")
    else:
        sys.stdout=open("test.txt","a")
        print ("0")
    
    import filecmp

    filecmp.cmp("test.txt", "match1.txt")
    


def helloCallBack():
   tkMessageBox.showinfo( "Image", "Selec")
   filename = askopenfilename()


    











root = Tk()
root.title('IRIS Recognition')
root.geometry("598x120+250+100")
mf = Frame(root)
mf.pack()


f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()

file_path = StringVar(root)



Button(f1, text="Register", command=register).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
Button(f2, text="verify", width=32, command=verify).grid(sticky='ew', padx=10, pady=10)

root.mainloop()
