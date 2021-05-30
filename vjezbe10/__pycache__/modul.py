import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Particle:

    def __init__(self,v,q):
        self.v = v
        self.q = q

    def akcle(self,v):
        self.masa=1
        self.Elektricno_polje=np.array((0,0,0))
        self.Magentsko_polje=np.array((0,0,1))
        self.ak=self.q*(self.Elektricno_polje + np.cross(v,self.Magentsko_polje))/self.masa
        return self.ak

    def Gibanje_euler(self):
        self.rx=[]
        self.ry=[]
        self.rz=[]
        self.r=np.array((0,0,0))
        self.t=0
        self.dt=0.01
        self.Elektricno_polje = np.array((0,0,0))
        self.Magentsko_polje = np.array((0,0,1))
        self.masa=1
        while self.t<=10:
            self.t=self.t+self.dt
            self.a=(self.Elektricno_polje + np.cross(self.v,self.Magentsko_polje))*(self.q/self.masa)
            self.v=self.v + self.a*self.dt
            self.r= self.r + self.v*self.dt
            self.rx.append(self.r[0])
            self.ry.append(self.r[1])
            self.rz.append(self.r[2])

        return self.rx,self.ry,self.rz

    def Gibanje_kutta(self):
        self.rx=[]
        self.ry=[]
        self.rz=[]
        self.r=np.array((0,0,0))
        self.t=0
        self.dt=0.01
        self.Elektricno_polje = np.array((0,0,0))
        self.Magentsko_polje = np.array((0,0,1))
        self.masa=1

        while self.t<=10:
            self.t=self.t+self.dt
            self.k1v = self.akcle(self.v)*self.dt 
            self.k1x = self.v*self.dt      
            self.k2v=(self.akcle(self.v + self.k1v/2))*self.dt     
            self.k2x=(self.v + self.k1v/2)*self.dt
            self.k3v=self.akcle(self.v + self.k2v/2)*self.dt    
            self.k3x=(self.v + self.k2v/2)*self.dt      
            self.k4v=self.akcle(self.v + self.k3v/2)*self.dt
            self.k4x=(self.v + self.k3v)*self.dt       
            self.v = self.v + 1/6*(self.k1v + 2*self.k2v + 2*self.k3v + self.k4v)    
            self.r = self.r + 1/6*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x)

            self.rx.append(self.r[0])
            self.ry.append(self.r[1])
            self.rz.append(self.r[2])

        return self.rx,self.ry,self.rz


v0 = np.array((10,10,10))
elektron=Particle(v0, -1)
poziron=Particle(v0, 1)
elektron2=Particle(v0, -1) # znam da treba raditi s reset funkcijom ali ovo je bilo lakse za napraviti puno manje linija koda 

#gibanje elektrona i pozitrona
a,b,c = elektron.Gibanje_euler()
e,f,g = poziron.Gibanje_euler()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(a,b,c,label="Putanja elektrona")
plt.plot(e,f,g,label="Putanja pozitrona")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#usporedba range kute i eulera

r,t,z = elektron2.Gibanje_kutta()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(a,b,c,label="euler")
plt.plot(r,t,z,label="range-kutta")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
