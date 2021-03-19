import matplotlib.pyplot as plt
import math

vi=10
xi=10
v=[vi]
x=[xi]
n=100
T=0
t=[T]
F=10
m=1
a=F/m

print(f"akcleleracija je {a}")

for i in range(n):
    dt=10/n
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
plt.plot([0,10],[a,a],label="akceleracija",color="g")
plt.xlim(0,10)
plt.xlabel("t[s]")
plt.ylabel("a[(m/s)/s]")
plt.show()


