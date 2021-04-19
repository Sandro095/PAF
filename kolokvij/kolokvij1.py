import matplotlib.pyplot as plt
class Vertikalnihitac:
    def __init__(self,h,v0):
        self.h = h
        self.v0 = v0
        print(f"uspješno stvoren objekt nalazi se na visini {self.h} i ima pocetnu brzinu v0={self.v0}")
    
    def promjeni_visinu(self,h_novi):
        if h_novi==self.h:
            return h_novi
        else:
            return h_novi
        
        
    def promjeni_brzinu(self,vo_novi):
        if vo_novi==self.v0:
            return vo_novi
        else:
            return vo_novi
        

    def neke_liste(self):
        self.y=[self.h]
        self.v=[self.v0]
        self.g=-9.81
        self.dt=0.01
        self.t=0
        self.T=[self.t]
        self.n=10000

    def pomak(self):
        self.t = self.t + self.dt
        self.v0 = self.v0 + self.g*self.dt
        self.h = self.h + self.v0*self.dt
        if self.h>=0:
            self.T.append(self.t)
            self.y.append(self.h)
            self.v.append(self.v0) 

    def Gibanje(self):
        k=0
        self.neke_liste()
        for i in range(self.n):
            self.pomak() 

        return self.T,self.y,self.v
        
    def maximalna_visina_i_vrjeme_leta(self):
        j,k,l=self.Gibanje()
        print(f"Vrijeme leta je {j[-1]}")
        for i in range(len(l)):
            if l[i]<=0.1 and l[i]>=-0.1:
                print("maximalana visina je:" + str(k[i]))


    def graph(self):
        
        plt.figure(1)
        plt.plot(self.T,self.y,label="pomak")
        plt.legend(loc="best")
        plt.figure(2)
        plt.plot(self.T,self.v,label="brzina")
        plt.legend(loc="best")
        plt.show()

    def otpor(self,v0,x0):
        k=2
        m=5
        g=-9.81
        dt=0.01
        t=0
        poz=[v0]
        brzina=[x0]
        Time=[t]
        n=1000000
        for i in range(n):
            a=g -k*v0/m
            v0= v0 + a*dt
            x0= x0 + v0*dt
            t= t + dt
            if x0>=0:
                poz.append(x0)
                brzina.append(v0)
                Time.append(t)

        print(f"Vrijeme leta je {Time[-1]}")
        for i in range(len(brzina)):
            if brzina[i]<=0.1 and brzina[i]>=-0.1:
                print("maximalana visina je:" + str(poz[i]))

        plt.figure(1)
        plt.plot(Time,poz,label="pomak")
        plt.legend(loc="best")
        plt.figure(2)
        plt.plot(Time,brzina,label="brzina")
        plt.legend(loc="best")
        plt.show()

        
    
        
            

