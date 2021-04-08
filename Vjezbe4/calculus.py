import math
import matplotlib.pyplot as plt

def f1(x):
    return x**3-5*x

def fd(x):
    return 3*x**2-5

a=[]
b=[]
r=[]
f=[]
#3x**2-2

def value(func,x):
    return(func(x))

def ana_funk(func,xd,xg,e):
    d=int((xg-xd)/e)
    for i in(range(d)):
        p=xd+i*e
        r.append(p)
        k=value(fd,p)
        f.append(k)
    return r,f

def deriviraj(funk,xo,e):
    der =  (value(f1,xo+e)-value(f1,xo-e))/(2*e)
    return der

def derivacja2(funk,xd,xg,e):
    d=int((xg-xd)/e)
    for i in range(d):
        p=xd+i*e
        a.append(p)
        k=deriviraj(funk,a[i],e)
        b.append(k)
    return a,b
        
print(deriviraj(f1,2,0.01))
c,d = derivacja2(f1,0,10,0.1)
g,h = ana_funk(fd,0,10,0.1)
plt.figure(1)
plt.scatter(c,d,label="num deri",color="r")
plt.plot(g,h,label="ana deri",color="b")
plt.show()

def integriraj(funk,xd,xg,e):
    d=int((xg-xd)/e)
    Id=0
    Ig=0
    Idd=[0]
    Igg=[0]
    pomakx=[xd]
    for i in range(d):
        Id=Id + (e)*value(funk,xd+i*e)
        Idd.append(Id)
        Ig=Ig +(e)*value(funk,(xd+e)+i*e)
        Igg.append(Ig)
        pomakx.append(xd+i*e)
        
    plt.figure(1)
    plt.scatter(test,Idd,label="donja meda")
    plt.scatter(test,Igg,label="donja meda")
    plt.show()
    
    #neznam kao graf napravit neznam sto da stavim na osi da divergira s obe strane

print(integriraj(f1,2,4,0.01))



def trap_integral(funk,xd,xg,e):
    n=int((xg-xd)/e)
    delx=(xg-xd)/n
    
    I=[0]
    for i in range(n):
        Id=Id+delx/2*(value(funk,xd+i*e)+value(funk,xd+(i+1)*e))
        I.append(Id)
    
    return Id


#print(trap_integral(f1,2,4,0.01))


        


        





