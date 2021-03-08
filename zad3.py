while True:
    x1=float(input("Unesi x1: "))
    y1=float(input("Unesi y1: "))
    x2=float(input("Unesi x2: "))
    y2=float(input("Unesi y2: "))
    if x1==x2:
        print("nemoguce je djeljenje s nulom ponovite upis: ")
    elif x1!=x2:
        break
#y-y1=kx-x1
k=(y2-y1)/(x2-x1)
l=-x1+y1
print("y="+str(k)+"x + "+str(l))