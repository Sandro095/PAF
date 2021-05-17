import matplotlib.pyplot as plt
import math as m
import numpy as np

class Particle:
    def __init__(self,tijelo,r,C,y0,x0,vo,kut,dt):
        self.dt = dt
        self.tijelo = tijelo
        self.C = C
        self.x0 = x0
        self.y0 = y0
        self.vo = vo
        self.r = r
        self.kut = kut

    def gibanje(self):
        self.g= -9.81
        self.ro=1.225
        self.masa= 3
        if self.tijelo == 1:
            self.A= self.r**2
        elif self.tijelo ==0:
            self.A=self.r**2*m.pi #nisam siguan da li u formulu ide poprecni presjek ili povrsina hemisfere
        self.t=0
        self.vxo = self.vo*m.cos(m.radians(self.kut))
        self.vyo = self.vo*m.sin(m.radians(self.kut))
        self.vx=[self.vxo]
        self.vy=[self.vyo]
        self.x=[self.x0]
        self.y=[self.y0]
        self.T=[self.t]
        self.ay=[self.C*self.vyo]
        self.ax=[self.C*self.vxo]
        while self.y0>=0:
            self.ay0 = -9.81 -np.sign(self.vyo)*self.C*self.ro*self.A/(2*self.masa)*(self.vyo)**2 
            self.ax0 = -np.sign(self.vxo)*self.C*self.ro*self.A/(2*self.masa)*(self.vxo)**2
            self.vxo = self.vxo + self.ax0*self.dt
            self.vyo = self.vyo + self.ay0*self.dt
            self.y0 = self.y0 + self.vyo*self.dt
            self.x0 = self.x0 + self.vxo*self.dt
            self.t = self.t + self.dt           
            self.vy.append(self.vyo)
            self.vx.append(self.vxo)
            self.ay.append(self.ay0)
            self.ax.append(self.ax0)
            self.y.append(self.y0)
            self.x.append(self.x0)
            self.T.append(self.t)

        plt.figure(1)
        plt.plot(self.T,self.x,label="x")
        plt.ylabel("x")
        plt.figure(2)
        plt.plot(self.T,self.y,label="y")
        plt.ylabel("y")
        plt.figure(3)
        plt.plot(self.x,self.y,label="x-y")
        plt.ylabel("x-y")
        plt.show()


    def gibanje_to_hit(self):
        self.xs=2
        self.ys=2
        self.r=0.1
        self.kutevi =[]
        self.g= -9.81
        self.ro=1.225
        self.masa= 3
        if self.tijelo == 1:
            self.A= self.r**2
        elif self.tijelo ==0:
            self.A=self.r**2*m.pi #nisam siguan da li u formulu ide poprecni presjek ili povrsina hemisfere
        self.t=0
        self.vxo = self.vo*m.cos(m.radians(self.kut))
        self.vyo = self.vo*m.sin(m.radians(self.kut))
        self.vx=[self.vxo]
        self.vy=[self.vyo]
        self.x=[self.x0]
        self.y=[self.y0]
        self.T=[self.t]
        self.ay=[self.C*self.vyo]
        self.ax=[self.C*self.vxo]
        while self.y0>=0:
            self.ay0 = -9.81 -np.sign(self.vyo)*self.C*self.ro*self.A/(2*self.masa)*(self.vyo)**2 
            self.ax0 = -np.sign(self.vxo)*self.C*self.ro*self.A/(2*self.masa)*(self.vxo)**2
            self.vxo = self.vxo + self.ax0*self.dt
            self.vyo = self.vyo + self.ay0*self.dt
            self.y0 = self.y0 + self.vyo*self.dt
            self.x0 = self.x0 + self.vxo*self.dt
            self.t = self.t + self.dt  
            if abs(self.x0 - self.xs)<=self.r and abs(self.y0 - self.ys)<=self.r: 
                print(self.kut)


    def reset(self):
        self.vxo = 0
        self.vxo = 0
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]
        self.T=[]
        self.ay=[]
        self.ax=[]
        self.x0 = 0
        self.y0 = 0
        self.ay0 = 0 
        self.ax0 = 0
        

p1 = Particle(0,0.9,0.5,0,0,40,45,0.01)
p1.gibanje()

#provjera jednadbe
#p3 = Particle(0,0.9,0,0,0,40,45,0.01)
#p3.gibanje()

 
kut_range = np.arange(0,90,1)

for i in range(len(kut_range)):
    p2 = Particle(0,0.9,2,0,0,40,kut_range[i] ,0.01)
    p2.gibanje_to_hit()
    p2.reset()
