import matplotlib.pyplot as plt

def pravac(x1,y1,x2,y2):
    a=input("Unesi 'plot' za ispis funkcije ili 'pdf' da se funkcija spremi kao pdf: ")
    k=(y2-y1)/(x2-x1)
    #y-y1=kx-x1
    l=-x1+y1
    if a=="plot":
        plt.plot([x1,x2],[y1,y2])
        plt.plot([x1,x2],[y1,y2],"ro")
        plt.show()
    elif a=="pdf":
        fig = plt.figure() 
        plt.plot([x1,x2],[y1,y2])
        plt.plot([x1,x2],[y1,y2],"ro")
        ime=input("unesi ime datoteke: ")
        plt.savefig(f"{ime}.pdf")
       
print(pravac(1,4,3,1))