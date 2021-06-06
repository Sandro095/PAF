  
import numpy as np
import math
import matplotlib.pyplot as plt

class Gravity:
    def __init__(self):
        self.x1_poz = []
        self.y1_poz = []
        self.x2_poz = []
        self.y2_poz = []

    def konst(self):
        self.masa1 =  1.989 * (10**30)
        self.masa2 =  5.9742 * (10**24)
        self.v1 = np.array((0,0))
        self.r1 = np.array((0,0))
        self.v2 = np.array((0,29783))
        self.r2 = np.array((1.486*(10**11),0))
        self.t=0
        self.G= 6.67 *10**(-11)
        self.dt=60*60*24
        
    def __interakcija(self):
        dist1 = np.linalg.norm(self.r1-self.r2)
        self.a1 = -self.G * (self.r1 - self.r2) * self.masa2/(dist1**3) 
        self.v1 = self.v1 + self.a1*self.dt
        self.r1 = self.r1 + self.v1*self.dt
        
        dist2 = np.linalg.norm(self.r2-self.r1)
        self.a2 = -self.G * (self.r2 - self.r1) * self.masa1/(dist2**3) 
        self.v2 = self.v2 + self.a2*self.dt
        self.r2 = self.r2 + self.v2*self.dt

    def medudjelovanje(self,t):
        self.konst()
        while self.t <= t:
            self.__interakcija()
            self.x1_poz.append(self.r1[0])
            self.y1_poz.append(self.r1[1])
            self.x2_poz.append(self.r2[0])
            self.y2_poz.append(self.r2[1])
            self.t = self.t + self.dt

        return self.x1_poz, self.y1_poz, self.x2_poz , self.y2_poz