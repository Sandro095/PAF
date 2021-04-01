import math as m
i=0
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,x0,y0,v0,kut,dt):
        self.x0 = x0
        self.dt = dt
        self.y0 = y0
        self.v0 = v0
        self.kut = kut

    def pocetni_uvjeti(self):
        self.n=100000
        self.t=0
        self.T=[self.t]
        self.x=[self.x0]
        self.y=[self.y0]
        self.vy0=self.v0*m.sin(m.radians(self.kut))
        self.vx0=self.v0*m.cos(m.radians(self.kut))
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        self.ve=[]

    def reset(self):
        self.x0=0
        self.y0=0
        self.v0=0
        self.kut=0
        self.vx=[]
        self.vy=[]
        self.ve=[]
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
        self.pocetni_uvjeti()
        for i in range(self.n):
            self.__move()
            if self.y0>=0:
                self.t=self.t+self.dt
                self.T.append(self.t)
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
        print(f"cestica ima pocetnu brzinu  {self.v0} pod kutem {self.kut} i u pocetnom trenutku nalaszi se na polozaju x={self.x0},y={self.y0}")

    def total_time(self):
        self.pocetni_uvjeti()
        for i in range(self.n):
            self.__move()
            if self.y0>=0:
                self.t=self.t+self.dt
                self.T.append(self.t)
        return self.T[-1]

    def max_speed(self):
        self.pocetni_uvjeti()
        for i in range(self.n):
            self.__move()
            if self.y0>=0:
                self.t=self.t+self.dt
                self.T.append(self.t)
                self.y.append(self.y0)
                self.x.append(self.x0)
                self.vx.append(self.vx0)
                self.vy.append(self.vy0)
        for i in range(len(self.vx)):
            self.vt=m.sqrt((self.vx[i])**2+(self.vy[i])**2)
            self.ve.append(self.vt)
            max_spe=max(self.ve)
        return max_spe

    def velocity_to_hit_target(self,xs,ys,r):
        self.n=100000
        self.t=0
        self.T=[self.t]
        self.x=[self.x0]
        self.y=[self.y0]
        self.vy0=self.v0*m.sin(m.radians(self.kut))
        self.vx0=self.v0*m.cos(m.radians(self.kut))
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        self.ve=[]
        self.brzine=[]
        for i in range(self.n):
            self.__move()
            if self.y0>=0:
                self.y.append(self.y0)
                self.x.append(self.x0)
                self.vx.append(self.vx0)
                self.vy.append(self.vy0)
        for i in range(len(self.vx)):
            self.vt=m.sqrt((self.vx[i])**2+(self.vy[i])**2)
            self.ve.append(self.vt)
        for i in range(len(self.x)):
            if abs(self.x[i]-xs)<=0.35 and abs(self.y[i]-ys)<=r:
                self.brzine.append(self.v0)
        return self.brzine
                  
        """plt.figure(1)
        plt.plot(self.x,self.y)
        plt.vlines(xs,ys-r,ys+r,color="g")
        plt.show()"""
            
    def angle_to_hit_target(self,xs,ys,r):
        self.n=100000
        self.t=0
        self.T=[self.t]
        self.x=[self.x0]
        self.y=[self.y0]
        self.vy0=self.v0*m.sin(m.radians(self.kut))
        self.vx0=self.v0*m.cos(m.radians(self.kut))
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        self.ve=[]
        self.kuti=[]
        for i in range(self.n):
            self.__move()
            if self.y0>=0:
                self.y.append(self.y0)
                self.x.append(self.x0)
                self.vx.append(self.vx0)
                self.vy.append(self.vy0)
        for i in range(len(self.vx)):
            self.vt=m.sqrt((self.vx[i])**2+(self.vy[i])**2)
            self.ve.append(self.vt)
        for i in range(len(self.x)):
            if abs(self.x[i]-xs)<=0.35 and abs(self.y[i]-ys)<=r:
                self.kuti.append(self.kut)
                plt.figure(1)
                plt.plot(self.x,self.y)
                plt.vlines(xs,ys-r,ys+r,color="g")
                plt.show()


        return self.kuti               
            
            
        








    


