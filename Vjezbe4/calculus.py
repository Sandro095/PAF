import math
import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return x**3-5*x

def fd(x):
    return 3*x**2-5

def value(func,x):
    return(func(x))

def ana_funk(func,xd,xg,e):
    r=[]
    f=[]
    d=int((xg-xd)/e)
    for i in(range(d)):
        p=xd+i*e
        r.append(p)
        k=value(fd,p)
        f.append(k)
    return r,f

def deriviraj(funk,xo,e,inti):
    if inti==1:
        der =  (value(f1,xo+e)-value(f1,xo-e))/(2*e)
        return der
    elif inti==0:
        deri2 =((value(f1,xo))-value(f1,xo-e))/e
        return deri2

def derivacja2(funk,xd,xg,e):
    a=[]
    b=[]
    d=int((xg-xd)/e)
    for i in range(d):
        p=xd+i*e
        a.append(p)
        k=deriviraj(funk,a[i],e,1)
        b.append(k)
    return a,b
        
def Graf(f1,xd,xg,e):

    c,d = derivacja2(f1,xd,xg,e)
    g,h = ana_funk(f1,xd,xg,e)
    plt.figure(1)
    plt.scatter(c,d,label="num deri",color="r")
    plt.plot(g,h,label="ana deri",color="b")
    plt.show()

def integriraj(funk,xd,xg,e):
    broj_koraka=int((xg-xd)/e)
    donja_suma=0
    gornja_suma=0
    donja_suma_list=[0]
    gornja_suma_list=[0]
    x_vrjednosti=[0]
    for i in range(broj_koraka):
        gornja_suma = gornja_suma + (e)*value(funk,(xd+e)+i*e)
        gornja_suma_list.append(gornja_suma)
        donja_suma=donja_suma +(e)*value(funk,xd+i*e)
        donja_suma_list.append(donja_suma)
        x_vrjednosti.append(xd+i*e)
    return donja_suma,gornja_suma

def integriraj2(funk,xd,xg,e):
    broj_koraka=np.arange(xd,xg,e)
    donja_suma=0
    gornja_suma=0
    donja_suma_list=[0]
    gornja_suma_list=[0]
    x_vrjednosti=[0]
    X_vrjednosti=0
    for i in range(len(broj_koraka)):
        gornja_suma = gornja_suma + (e)*value(funk,(xd+e)+i*e)
        gornja_suma_list.append(gornja_suma)
        donja_suma=donja_suma +(e)*value(funk,xd+i*e)
        donja_suma_list.append(donja_suma)
        X_vrjednosti=xd+i*e
        x_vrjednosti.append(X_vrjednosti)
    return donja_suma,gornja_suma,x_vrjednosti

def trap_integral(funk,xd,xg,e):
    broj_koraka=np.arange(xd,xg,e)
    delx=(xg-xd)/len(broj_koraka)
    Id=0
    I=[0]
    for i in range(len(broj_koraka)):
        Id=Id+delx/2*(value(funk,xd+i*e)+value(funk,xd+(i+1)*e))
        I.append(Id)
    return Id      

def inte_graf(funk,xd,xg):
    lista_epsilona=[0.1,0.5,1,2,3]
    Gornja_G=[]
    Donja_D=[]
    X_Vr=[]
    Trapez=[]
    for i in range(len(lista_epsilona)):
        j,k,g=integriraj2(funk,xd,xg,lista_epsilona[i])
        ej=trap_integral(funk,xd,xg,lista_epsilona[i])
        Trapez.append(ej)
        Donja_D.append(j)
        Gornja_G.append(k)
        X_Vr.append(lista_epsilona[i])
    plt.figure(1)
    plt.scatter(lista_epsilona,Donja_D)
    plt.scatter(lista_epsilona,Gornja_G)
    plt.scatter(lista_epsilona,Trapez)
    plt.show()

#print(deriviraj(f1,2,0.001,0))
#print(inte_graf(f1,2,4))
#print(Graf(f1,0,10,0.01))
#print(deriviraj(f1,2,0.01,1))
#print(integriraj(f1,2,4,0.01))
#print(trap_integral(f1,2,4,0.01))