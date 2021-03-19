import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(xi,vi,F,m,n):
    v=[vi]
    x=[xi]
    T=0
    t=[T]
    a=F/m

    for i in range(n):
        dt=0.01
        T=T+dt
        t.append(T)
        vi=vi+a*dt
        xi=xi+vi*dt
        v.append(vi)
        x.append(xi)

    plt.figure(1)
    plt.plot(t,x,label="put",color="r")
    plt.xlabel("t[s]")
    plt.ylabel("x[m]")
    plt.figure(2)
    plt.plot(t,v,label="brzina",color="b")
    plt.xlabel("t[s]")
    plt.ylabel("v[m/s]")
    plt.figure(3)
    plt.plot([0,n*dt],[a,a],label="akceleracija",color="g")
    plt.xlabel("t[s]")
    plt.ylabel("a[(m/s)/s]")
    plt.show()

def kosi_hitac(h,x,v0,kut,n):
    y=[h]
    d=[x]
    
    a=0
    g=-9.81
    T=0
    t=[T]

    vxo=v0*math.cos(math.radians(kut))
    vyo=v0*math.sin(math.radians(kut))

    for i in range(n):
        dt=0.01
        T=T+dt
        vyo=vyo+g*dt
        vxo=vxo +a*dt
        x=x+vxo*dt
        h=h+vyo*dt
        if h>=0:
            t.append(T)
            y.append(h)
            d.append(x)


    plt.figure(1)
    plt.plot(t,y,label="visina")
    plt.xlabel("t[s]")
    plt.ylabel("h[m]")
    plt.figure(2)
    plt.plot(t,d,label="domet")
    plt.xlabel("t[s]")
    plt.ylabel("x[m]")
    plt.figure(3)
    plt.plot(d,y,label="domet")
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.show()

