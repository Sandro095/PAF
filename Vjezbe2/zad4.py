import matplotlib.pyplot as plt
import math
g=9.81

def graf(h,vo,kut,n):
    vxo=vo*math.cos(math.radians(kut))
    vyo=vo*math.sin(math.radians(kut))

    T=0
    t=[]
    vy=[]
    vx=[]
    y=[]
    x=[]
    xo=0
    a=0

    for i in range(n):
        dt=0.01
        T=T+dt
        t.append(T)
        vyo=vyo-g*dt
        vxo=vxo + a*dt
        xo=xo+vxo*dt
        h=h+vyo*dt
        if h>=0:
            y.append(h)
            x.append(xo)

    plt.figure(1)
    plt.plot(x,y,label="visina")
    plt.xlabel("t[s]")
    plt.ylabel("h[m]")
    plt.show()

#print(graf(10,40,45,1000))

def max_visina(yo,vo,kut,n):

    y=[yo]
    vyo=vo*math.sin(math.radians(kut))
    vy=[vyo]
    

    for i in range(n):
        dt=0.01
        vyo=vyo-g*dt
        yo=yo+vyo*dt
        if yo>=0:
            y.append(yo)
    print(max(y))

#print(max_visina(10,50,45,1000000))

def domet(h,vo,kut,n):

    xo=0
    T=0
    a=0
    t=[T]
    x=[]
    vxo=vo*math.cos(math.radians(kut))
    vyo=vo*math.sin(math.radians(kut))

    for i in range(n):
        dt=0.01
        T=T+dt
        vyo=vyo-g*dt
        h=h+vyo*dt
        vxo=vxo + a*dt
        xo=xo + vxo*dt
        if h>=0:
            x.append(xo)

    dom=x[-1]
    print(dom)
        
#print(domet(10,50,70,100000))

def max_brz(vo,kut,n):

    a=0
    vyo=vo*math.sin(math.radians(kut))
    vxo=vo*math.cos(math.radians(kut))
    vy=[vyo]
    vx=[vxo]

    for i in range(n):
        dt=0.01
        vyo=vyo-g*dt
        vy.append(vyo)
        vxo=vxo + a*dt
        vx.append(vxo)
    vmax=math.sqrt(max(vy)**2+max(vx)**2)
    print(vmax)
    
#print(max_brz(50,20,1000))

def bullseye(xt,yt,r,h,vo,kut):
    T=0
    x=0
    n=1000
    y=[h]
    d=[x]
    t=[T]
    a=0

    vxo=vo*math.cos(math.radians(kut))
    vyo=vo*(math.sin(math.radians(kut)))

    ts=round(xt/vxo,4)
    Ty=h+(vyo*ts)-(0.5*g*ts**2)
    dist=[]

    for i in range(n):
            dt=0.01
            T=T+dt
            t.append(T)
            vyo=vyo-g*dt
            vxo=vxo + a*dt
            h=h+vyo*dt
            if h>=0:
                x=x+vxo*dt
                dista_donja=math.sqrt((xt-x)**2+((yt-r)-h)**2)
                dista_gornja=math.sqrt((xt-x)**2+((yt+r)-h)**2) 
                dist.append(dista_donja)
                dist.append(dista_gornja)
                y.append(h)
                d.append(x)
                if abs(x-xt)<=0.2: 
                    if abs(y[i]-yt)<=r:
                        print("udrio je u metu!")
                    elif abs(y[i]-yt)>=r:
                        print(min(dist))

    plt.figure(1)
    plt.plot(d,y,label="domet")
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.plot([xt,xt],[yt-r,yt+r],label="meta",color="g")
    plt.show()

#print(bullseye(60,50,5,0,50,45))
#print(bullseye(60,50,2,0,50,45))


    

