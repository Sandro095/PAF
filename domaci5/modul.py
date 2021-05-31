import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import modul1 as m1

class Particle():

    def __init__(self,v0,q):
        self.v0=v0
        self.q=q

    def akcle(self,v0,t):
        self.masa=1
        self.B=np.array((0,0,10/t))
        self.E=np.array((0.01,0.01,0.01))
        self.ak=((self.E/(t+100)) + np.cross(self.v0,self.B))*(self.q/self.masa)
        return self.ak

    def gibanje_kutta(self):
        self.masa=1
        self.dt=0.01
        self.rx=[]
        self.ry=[]
        self.rz=[]
        self.t=0
        self.r=np.array((0,0,0))
        while self.t<=10:
            self.t=self.t+self.dt
            self.k1v = (self.akcle(self.v0,self.t))*self.dt       
            self.k1x = self.v0*self.dt      
            self.k2v=(self.akcle(self.v0 + self.k1v/2,self.t+self.dt/2))*self.dt       
            self.k2x=(self.v0 + self.k1v/2)*self.dt     
            self.k3v=(self.akcle(self.v0 + self.k2v/2,self.t+self.dt/2))*self.dt      
            self.k3x=(self.v0 + self.k2v/2)*self.dt           
            self.k4v=(self.akcle(self.v0 + self.k3v/2,self.t+self.dt))*self.dt   
            self.k4x=(self.v0 + self.k3v)*self.dt           
            self.v0 = self.v0 + 1/6*(self.k1v + 2*self.k2v + 2*self.k3v + self.k4v)       
            self.r = self.r + 1/6*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x)
            self.rx.append(self.r[0])
            self.ry.append(self.r[1])
            self.rz.append(self.r[2])

        return self.rx,self.ry,self.rz

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
            self.a=(self.Elektricno_polje + np.cross(self.v0,self.Magentsko_polje))*(self.q/self.masa)
            self.v0=self.v0 + self.a*self.dt
            self.r= self.r + self.v0*self.dt
            self.rx.append(self.r[0])
            self.ry.append(self.r[1])
            self.rz.append(self.r[2])

        return self.rx,self.ry,self.rz

v0=np.array((10,0,10))
elektorn= Particle(v0,-1)
pozitron= Particle(v0,1)
elektron2 = Particle(v0,-1)

#poutanja elektora u konstanom polju i ne konst polju
h,j,k= elektron2.Gibanje_euler()
a,b,c= elektorn.gibanje_kutta()

######NAPOMENA###### neznam koje brojeve uzezi, rx i ry mi explodiraju na 10^6 pa se zbog tog čini da konstanto magnetsko polje ima ravnu putanju
#zapravo nema jer kad se makne gibnje u ne const mag i elektrincom polu onda ima putanju helixa

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(h,j,k,label="const B")
plt.plot(a,b,c,label="ne const B")
plt.legend(loc="best")
plt.show()

#promjenjivo elektricno i magnetko polje usopredba elektrona i pozitrona

elektorn= Particle(v0,-1)
pozitron= Particle(v0,1)
e,f,g= pozitron.gibanje_kutta()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(a,b,c,label="elektron")
plt.plot(e,f,g,label="pozitron")
plt.show()
    
    
    
