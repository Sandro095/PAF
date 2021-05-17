import matplotlib.pyplot as plt
import math as m
import numpy as np

class Particle:
    def __init__(self,C,y0,x0,vo,kut,dt):
        self.dt = dt
        self.C = C
        self.x0 = x0
        self.y0 = y0
        self.vo = vo
        self.kut = kut
    
    def gibanje_euler(self):
        self.g= -9.81
        self.ro=1.225
        self.masa= 3
        self.povrsina = 2
        self.t=0
        self.vxo = self.vo*m.cos(m.radians(self.kut))
        self.vyo = self.vo*m.sin(m.radians(self.kut))
        self.vx=[self.vxo]
        self.vy=[self.vyo]
        self.x=[self.x0]
        self.y=[self.y0]
        self.T=[self.t]
        self.ay=[self.C*self.ro*self.povrsina/(2*self.masa)*self.vyo]
        self.ax=[self.C*self.ro*self.povrsina/(2*self.masa)*self.vxo]
        while self.y0>=0:
            self.ay0 = -9.81 -np.sign(self.vyo)*self.C*self.ro*self.povrsina/(2*self.masa)*(self.vyo)**2 
            self.ax0 = -np.sign(self.vxo)*self.C*self.ro*self.povrsina/(2*self.masa)*(self.vxo)**2
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

    """def gibanje_rangekuta(self):
        self.g= -9.81
        self.ro=1.225
        self.masa= 3
        self.povrsina = 2
        self.t=0
        self.vxo = self.vo*m.cos(m.radians(self.kut))
        self.vyo = self.vo*m.sin(m.radians(self.kut))
        self.vx=[self.vxo]
        self.vy=[self.vyo]
        self.x=[self.x0]
        self.y=[self.y0]
        self.T=[self.t]
        self.ay=[self.C*self.ro*self.povrsina/(2*self.masa)*self.vyo]
        self.ax=[self.C*self.ro*self.povrsina/(2*self.masa)*self.vxo]
        while self.y0>=0:
            self.k1vx = -9.81 -np.sign(self.vyo)*self.C*self.ro*self.povrsina/(2*self.masa)*(self.vyo)**2 
            self.k1vy = -np.sign(self.vxo)*self.C*self.ro*self.povrsina/(2*self.masa)*(self.vxo)**2
            self.k1xx = self.vxo*self.dt
            self.k1xy =self.vyo*self.dt

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
        plt.show()"""



p1 = Particle(2,0,0,40,45,0.01)
p1.gibanje_euler()
   