import matplotlib.pyplot as plt
import math


def provjera(x,y,xc,yc,r):
    a=input("Unesi 'plot' za ispis funkcije ili 'pdf' da se funkcija spremi kao pdf: ")
    d=math.sqrt((x-xc)**2+(y-yc)**2)
    e=float(input("Unesi neki epsilon: "))

    if abs(d-r)<e:
        print
        ("Tocka se priblizno nalazi na kruznici")
    elif d>r:
        print("Tocka se van kruznice")
    elif d<r:
        print("tocka se nalazi unutar kruznice")

    if a=="pdf":
        l=round(abs(d-r),2)
        fig, ax = plt.subplots()
        cir=plt.Circle((xc,yc),r,fill=False)
        dots=plt.plot([x],[y],"ro")
        ax.add_patch(cir)
        ax.set_aspect(1)
        plt.annotate("T("f"{x},{y}) d={l}",(x-1.4,y-0.5))
        ime=input("unesi ime datoteke: ")
        plt.savefig(f"{ime}.pdf")
    if a=="plot":
        l=round(abs(d-r),2)
        fig, ax = plt.subplots()
        cir=plt.Circle((xc,yc),r,fill=False)
        dots=plt.plot([x],[y],"ro")
        ax.add_patch(cir)
        ax.set_aspect(1)
        plt.annotate("T("f"{x},{y}) d={l}",(x-1.4,y-0.5))
        plt.show()
        

    
#provjera(4,4,0,0,1)