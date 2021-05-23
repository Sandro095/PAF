import matplotlib.pyplot as plt
import math as m
import numpy as np

class Particle:
    def __init__(self,masa,C,y0,x0,vo,kut,dt):
        self.dt = dt
        self.masa= masa
        self.C = C
        self.x0 = x0
        self.y0 = y0
        self.vo = vo
        self.kut = kut

    def reset(self):
        self.t=0
        self.vxo = 0
        self.vyo = 0
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]
        self.T=[]
        self.ay=[]
        self.ax=[]
        self.ay0 = 0
        self.ax0 = 0
        self.vxo = 0
        self.vyo = 0
        self.y0 = 0
        self.x0 = 0     
        
    def gibanje_euler(self):
        self.g= -9.81
        self.ro=1.225
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
        
        return (self.T,self.x,self.y)

    def akceleracijaX(self,e):
        return -np.sign(e)*self.C*self.ro*self.povrsina/(2*self.masa)*e**2

    def akceleracijaY(self,e):
       return -9.81 -np.sign(e)*self.C*self.ro*self.povrsina/(2*self.masa)*(e)**2 

    def gibanje_rangekuta(self):
        self.g= -9.81
        self.ro= 1.225
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
        self.ay=[self.C*self.ro*self.povrsina/(2*self.masa)*self.vyo**2]
        self.ax=[self.C*self.ro*self.povrsina/(2*self.masa)*self.vxo**2]
        while self.y0>=0:
            self.k1vx = self.akceleracijaX(self.vxo)*self.dt
            self.k1vy = self.akceleracijaY(self.vyo)*self.dt

            self.k1xx = self.vxo*self.dt
            self.k1xy =self.vyo*self.dt

            self.k2vx=self.akceleracijaX(self.vxo + self.k1vx/2)*self.dt
            self.k2vy=self.akceleracijaY(self.vyo + self.k1vy/2)*self.dt

            self.k2xx=(self.vxo + self.k1vx/2)*self.dt
            self.k2xy=(self.vyo + self.k1vy/2)*self.dt

            self.k3vx=self.akceleracijaX(self.vxo + self.k2vx/2)*self.dt
            self.k3vy=self.akceleracijaY(self.vyo + self.k2vy/2)*self.dt

            self.k3xx=(self.vxo + self.k3vx/2)*self.dt      
            self.k3xy=(self.vyo + self.k3vy/2)*self.dt

            self.k4vx=self.akceleracijaX(self.vxo + self.k3vx/2)*self.dt
            self.k4vy=self.akceleracijaY(self.vyo + self.k3vy/2)*self.dt

            self.k4xx=(self.vxo + self.k4vx/2)*self.dt      
            self.k4xy=(self.vyo + self.k4vy/2)*self.dt

            self.vxo = self.vxo + 1/6*(self.k1vx + 2*self.k2vx + 2*self.k3vx + self.k4vx)
            self.vyo = self.vyo + 1/6*(self.k1vy + 2*self.k2vy + 2*self.k3vy + self.k4vy)
            self.x0 = self.x0 + 1/6*(self.k1xx + 2*self.k2xx + 2*self.k3xx + self.k4xx)
            self.y0 = self.y0 + 1/6*(self.k1xy + 2*self.k2xy + 2*self.k3xy + self.k4xy)

            self.t = self.t + self.dt           
            self.vy.append(self.vyo)
            self.vx.append(self.vxo)
            self.ay.append(self.akceleracijaX(self.vyo))
            self.ax.append(self.akceleracijaX(self.vxo))
            self.y.append(self.y0)
            self.x.append(self.x0)
            self.T.append(self.t)

        return self.T,self.x,self.y

    def graf_euler(self):
        a,b,c,=self.gibanje_euler()
        print(a,b,c)
        plt.figure(1)
        plt.plot(a,b,label="x")
        plt.ylabel("x")
        plt.figure(2)
        plt.plot(a,c,label="y")
        plt.ylabel("y")
        plt.figure(3)
        plt.plot(b,c,label="x-y")
        plt.ylabel("x-y")
        plt.show()

    def graf_rangekuta(self):
        a,b,c,=self.gibanje_rangekuta()
        plt.figure(1)
        plt.plot(a,b,label="x")
        plt.ylabel("x")
        plt.figure(2)
        plt.plot(a,c,label="y")
        plt.ylabel("y")
        plt.figure(3)
        plt.plot(b,c,label="x-y")
        plt.ylabel("x-y")
        plt.show()

    def graf_uspoprebda(self):
        plt.figure(1)
        a,b,c,=self.gibanje_euler()
        self.reset()
        plt.plot(b,c,label="euler")
        c,d,e,=self.gibanje_rangekuta()
        plt.plot(d,e,label="rangekutta")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


p1 = Particle(3,2,0,0,40,45,0.01)
#p1.graf_euler()
#p1.reset()
#p1.graf_rangekuta()
p1.graf_uspoprebda() #ako je dt=0.001 onda su priblizno isti
   
C_ko=np.arange(0,2,0.05)
mase=np.arange(1,20,0.1)

dometi_C=[]
dometi_mase=[]

for i in range(len(C_ko)):
    p2=Particle(3,C_ko[i],0,0,40,45,0.01)
    a,b,c=p2.gibanje_rangekuta()
    dometi_C.append(b[-1])
plt.plot(C_ko,dometi_C,label="ovisnost o dometa o koeficijenut trenja")
plt.xlabel("Koeficijent otpora")
plt.ylabel("domet")
plt.show()

for i in range(len(mase)):
    p3=Particle(mase[i],0.5,0,0,40,45,0.01)
    a,b,c=p3.gibanje_euler()
    dometi_mase.append(b[-1])
plt.plot(mase,dometi_mase,label="ovisnost o dometa o masi")
plt.xlabel("masa")
plt.ylabel("domet")
plt.show()

