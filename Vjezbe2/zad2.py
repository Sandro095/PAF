import matplotlib.pyplot as plt
import math

T=0
h=10
x=10
y=[h]
d=[x]
t=[T]

v0=50
kut=45
g=-9.81


vxo=v0*math.cos(math.radians(kut))
vyo=v0*math.sin(math.radians(kut))

n=1000
a=0

for i in range(n):
    dt=10/n
    T=T+dt
    t.append(T)
    vyo=vyo+g*dt
    vxo=vxo+a*dt
    h=h+vyo*dt
    y.append(h)
    x=x+vxo*dt
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
plt.figure(3)


plt.show()