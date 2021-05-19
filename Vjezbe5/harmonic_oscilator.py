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
        self.T=[]
        self.lista_vremena=[]
        self.lista_brzina=[]
        self.lista_polozaja=[]
        self.lisa_akceleracija=[]

    def analy(self):
            self.neke_liste()
            for i in range(self.n):
                self.analy_polozaj = self.x0* m.cos(self.w*self.time)
                self.analy_brzine = -self.w * self.x0 *m.sin(self.w*self.time)
                self.analy_akceleracija = (-1)*self.w*self.w * self.x0 *m.cos(self.w*self.time)
                self.time = self.time + self.dt 
                self.lisa_akceleracija.append(self.analy_akceleracija)
                self.lista_brzina.append(self.analy_brzine)
                self.lista_polozaja.append(self.analy_polozaj)
                self.lista_vremena.append(self.time)
            return self.lista_polozaja,self.lista_brzina,self.lisa_akceleracija,self.lista_vremena


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

        return self.x,self.v,self.a,self.T       


    def graf_numerical(self):
        a,b,c,d=self.polozaj()
        plt.figure(1)
        plt.plot(d,a,label="analitičko rješenje",color="blue")
        plt.legend(loc="best")
        plt.figure(2)
        plt.plot(d,b,label="analitičko rješenje",color="blue")
        plt.legend(loc="best")
        plt.figure(3)
        plt.plot(d,c,label="analitičko rješenje",color="blue")
        plt.legend(loc="best")
        plt.show()


    def graf_analy(self):
        a,b,c,d=self.analy()
        plt.figure(1)
        plt.plot(d,a,label="analitičko rješenje",color="blue")
        plt.legend(loc="best")
        plt.figure(2)
        plt.plot(d,b,label="analitičko rješenje",color="blue")
        plt.legend(loc="best")
        plt.figure(3)
        plt.plot(d,c,label="analitičko rješenje",color="blue")
        plt.legend(loc="best")
        plt.show()


    def graf_usporedba(self):
        a,b,c,d=self.analy()
        e,f,g,h=self.polozaj()
        plt.figure(1)
        plt.plot(d,a,label="analitičko rješenje",color="blue")
        plt.plot(h,e,label="numeričko rješenje",color="red")
        plt.legend(loc="best")
        plt.show()

    def period(self):
        a,b,c,d= self.polozaj()
        epsilon=0.001
        
        for i in range(2,len(d),1):
            if abs(a[0]-a[i])<=epsilon:
                print("period je: " + str(d[i]) +" s")



p1 = harmonicoscilator(20,5,10,0.01,10)
#p1.graf_numerical()
#p1.graf_analy()
#p1.reset()
p1.period()
