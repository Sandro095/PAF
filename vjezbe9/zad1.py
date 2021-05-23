import matplotlib.pyplot as plt
import math as m
import numpy as np

class Particle:
    def __init__(self,m,h,k,C,l,dt):
        self.dt = dt
        self.l = l
        self.m = m
        self.h = h
        self.k = k
        self.C = C

    def konstante(self):
        g= -9.81
        self.t=0
        self.vy=0
        self.v=[]
        self.y=[]
        self.T=[]
        self.a=[]
        self.ekineticka=[]
        self.egpotencijalna=[]
        self.epotencijalna=[]
        self.ukupnaE=[]
        self.ro=1.225
        self.A=0.5
     
    def gibanje(self):
        self.konstante()
        while self.t<=25:
            if (self.h - self.l)>0:
                self.a= -9.81 + -1*np.sign(self.vy)*self.C*(self.vy**2)*self.ro*self.A/(2*self.m)
                self.epk=0
            if (self.h - self.l)<0: 
                self.a= -9.81 + self.k*abs(self.h-self.l)/(self.m) - 1*np.sign(self.vy)*self.C*(self.vy**2)*self.ro*self.A/(2*self.m)
                self.epk = 0.5*self.k*(self.h-self.l)**2
            self.vy = self.vy + self.a*self.dt
            self.h = self.h + self.vy*self.dt
            self.t = self.t + self.dt

            
            self.Ek = 0.5*self.m*self.vy**2
            self.Ep = self.m*(9.81)*self.h
            self.eukp = self.epk + self.Ep + self.Ek 

            self.ekineticka.append(self.Ek)
            self.egpotencijalna.append(self.Ep)  
            self.epotencijalna.append(self.epk) 
            self.ukupnaE.append(self.eukp)         
            self.v.append(self.vy)
            self.y.append(self.h)
            self.T.append(self.t)

        plt.figure(1)
        plt.plot(self.T,self.epotencijalna,label="Elasticna potencijalna energija")
        plt.plot(self.T,self.ekineticka,label="Kineticka potencijalna energija")
        plt.plot(self.T,self.egpotencijalna,label="Gravitacijska potencijalna energija")
        plt.plot(self.T,self.ukupnaE,label="ukupna energija")
        plt.legend(loc="best")
        plt.figure(3)
        plt.plot(self.T,self.y)
        plt.show()
        
p1= Particle(70,100,150,2,50,0.001) #s otporom zraka
p2= Particle(70,100,150,0,50,0.001) #bez otpora zraka
p1.gibanje()
p2.gibanje()
   