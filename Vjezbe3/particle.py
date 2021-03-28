import math as m
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,x0,y0,v0,kut,dt):
        self.x0 = x0
        self.dt =dt
        self.y0= y0
        self.v0 = v0
        self.kut = kut

    def reset(self):
        self.x0=0
        self.y0=0
        self.v0=0
        self.kut=0
        self.vx=[]
        self.vy=[]
        self.y=[]
        self.x=[]
        self.T=[]

    def __move(self):
        t=0
        g=-9.81
        a=0
        T=[t]
        self.vy0 = self.vy0 + g*self.dt
        self.y0 = self.y0 + self.vy0*self.dt
        self.vx0 = self.vx0 + a*self.dt
        self.x0 = self.x0 +self.vx0*self.dt
        
    def range(self):
        n=100000
        t=0
        T=[t]
        self.x=[self.x0]
        self.y=[self.y0]
        self.vy0=self.v0*m.sin(m.radians(self.kut))
        self.vx0=self.v0*m.cos(m.radians(self.kut))
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        for i in range(n):
            self.__move()
            if self.y0>=0:
                t=t+self.dt
                T.append(t)
                self.y.append(self.y0)
                self.x.append(self.x0)
                self.vx.append(self.vx0)
                self.vy.append(self.vy0)
        self.domet=max(self.x)
        return self.domet

    
    def plot_trajectory(self):
        self.__move()
        plt.figure(1)
        plt.plot(self.x,self.y,label="Putanja",color="b")
        plt.show()

    def ana_domet(self):
        g=-9.81
        self.t1 = (self.vy[0]+m.sqrt(self.vy[0]**2 + 2*(-g)*self.y[0]))/(-g)
        self.ana_domet=self.x[0]+self.vx[0]*self.t1
        return self.ana_domet
        
    def relativa_greska(self):
        self.rel_pog=abs(self.domet-self.ana_domet)/self.ana_domet
        return self.rel_pog
        
    def printInfo(self):
        print(f"cestica ima pocetnu brzinu {len(self.y)} {len(self.x)} {len(self.vy)} {len(self.vx)} {self.v0} pod kutem {self.kut} i u pocetnom trenutku nalaszi se na polozaju x={self.x[0]},y={self.y[0]}")
        
        """plt.figure(2)
        plt.plot([0,self.dt],[self.ana_domet,self.domet])
        plt.show()"""

    


