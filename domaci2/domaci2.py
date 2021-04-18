import numpy as np
import matplotlib.pyplot as plt

def sila(masa,v0,x0):   
    return 5

def harmonisko(masa,v0,x0): 
    k=2
    return -k*x0

def funkcija(masa,v0,x0):
    time = np.arange(0,10,0.1)
    return v0+x0+time[1]

def gibanje(funk,masa,v0,x0):

    time = np.arange(0,10,0.1)
    dt = 0.1
    akceleracija=[]
    brzina=[]
    put=[]
    for i in range(len(time)):
        if funk=="funkcija":
            F=funk(masa,v0,x0)+time[i]
        else:
            F=funk(masa,v0,x0)
        a=F/masa
        v0 = v0 + a * dt
        x0 = x0 + v0 * dt
        akceleracija.append(a)
        brzina.append(v0)
        put.append(x0)

    plt.figure(1)
    plt.plot(time,akceleracija,label="a-t")
    plt.legend(loc="best")
    plt.figure(2)
    plt.plot(time,brzina,label="v-t")
    plt.legend(loc="best")
    plt.figure(3)
    plt.plot(time,put,label="s-t")
    plt.legend(loc="best")
    plt.show()

#gibanje(sila,3,1,2)   #const sila
#gibanje(harmonisko,3,1,2) #Harmonisko titarnaje
#gibanje(funkcija,3,1,2)  #prizvoljno gibanje







