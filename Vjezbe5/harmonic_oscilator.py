import matplotlib.pyplot as plt
import math as m
class harmonicoscilator:

    def __init__(self,x0,k,m,dt,t_oscil):

        self.x0 = x0
        self.dt = dt
        self.k = k
        self.m = m
        self.t_oscil = t_oscil

    def neke_liste(self):

        #numericke
        self.t=0
        self.v=[]
        self.x = []
        self.a= []
        self.T = []
        self.n=int(self.t_oscil/self.dt)
        self.w=m.sqrt(self.k/self.m)
        self.fi=0
        self.v0=0

        #analaticke
        self.lista_polozaja=[]
        self.lista_brzina=[]
        self.lisa_akceleracija =[]
        self.lista_vremena=[]
        self.time=0
        
    def reset(self):
        self.x=[]
        self.v=[]
        self.a=[]

    def analy(self):
            self.neke_liste()
            for i in range(self.n):
                self.time = self.time + self.dt
                self.analy_polozaj = self.x0* m.sin(self.w*self.time)
                self.analy_brzine = self.w * self.x0 *m.cos(self.w*self.time)
                self.analy_akceleracija = (-1)*self.w*self.w * self.x0 *m.sin(self.w*self.time) 
                self.lisa_akceleracija.append(self.analy_akceleracija)
                self.lista_brzina.append(self.analy_brzine)
                self.lista_polozaja.append(self.analy_polozaj)
                self.lista_vremena.append(self.time)

            plt.figure(1)
            plt.scatter(self.lista_vremena,self.lista_polozaja,label="pomak")
            plt.legend(loc="best")
            plt.figure(2)
            plt.scatter(self.lista_vremena,self.lista_brzina,label="brzina")
            plt.legend(loc="best")
            plt.figure(3)
            plt.scatter(self.lista_vremena,self.lisa_akceleracija,label="akceleracija")
            plt.legend(loc="best")
            plt.show()

    def polozaj(self):
        self.neke_liste()
        for i in range(self.n):
            self.ac= -(self.k/self.m)*self.x0
            self.v0= self.v0 + self.ac*self.dt
            self.x0= self.x0 + self.v0*self.dt
            self.t= self.t + self.dt
            self.x.append(self.x0)
            self.v.append(self.v0)
            self.a.append(self.ac)
            self.T.append(self.t)
        
        plt.figure(1)
        plt.scatter(self.T,self.x,label="poz")
        plt.legend(loc="best")
        plt.figure(2)
        plt.scatter(self.T,self.v,label="brzina")
        plt.legend(loc="best")
        plt.figure(3)
        plt.scatter(self.T,self.a,label="akc")
        plt.legend(loc="best")
        plt.show()

        