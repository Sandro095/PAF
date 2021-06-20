import zad1 as universe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random 

au = 1.496e11
day = 60*60*24
year = 365.242*day

min_mer_dist=[]
min_ven_dist=[]
min_ear_dist=[]
min_mar_dist=[]
min_sun_dist=[]


sun = universe.Planet("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
earth = universe.Planet("Earth", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29780.)))
mercury= universe.Planet("Mercury", 1.635e20, np.array((-0.3*au,0.)), np.array((0.,48000.)))
venus= universe.Planet("Venus", 1.635e18, np.array((-0.7*au,0.)), np.array((0.,35000.)))
mars= universe.Planet("Mars", 6.39e24, np.array((-1.524*au,0.)), np.array((0.,24100.)))

 
ss = universe.Universe() 

min_ear_dist=[]
min_mar_dist=[]
min_mer_dist=[]
min_sun_dist=[]
min_ven_dist=[]


#ovdne počinje 2 zadatak njega sam stavio u komenter jer njemu treba jako mnogo vremena da se napravi

"""
def randminus():
    while True:
        broj=random.randint(-1,1)
        if broj !=0:
            return broj

for i in range(1000):

    rx, ry = randminus()*random.randint(4*au,5*au), randminus()*random.randint(4*au,5*au)
    vx, vy = -np.sign(rx)*random.randint(1*10**4,4*10**4), -np.sign(ry)*random.randint(1*10**4,4*10**4)
    r=np.array((rx,ry))
    v=np.array((vx,vy))
    m=random.randint(1*10**13,9.9*10**13)


    comet = universe.Planet("comet", m, r, v)    
    ss.add_planet(sun)
    ss.add_planet(earth)
    ss.add_planet(mercury)
    ss.add_planet(venus)
    ss.add_planet(mars)
    ss.add_planet(comet)
    

    ss.evolve(5.0*year)

    ss.remove_planet(comet)

    min_mer_dist.append(min(mercury.dist)/au)
    min_ven_dist.append(min(venus.dist)/au)
    min_ear_dist.append(min(earth.dist)/au)
    min_mar_dist.append(min(mars.dist)/au)
    min_sun_dist.append(min(sun.dist)/au)
    ss.__init__()


fig, axs = plt.subplots(1, 5, sharey=True, tight_layout=True)
plt.xlim(0,1)
axs[0].hist(min_mer_dist, len(min_mer_dist), facecolor='blue', alpha=0.5,label="mercury")
axs[1].hist(min_ven_dist, len(min_ven_dist), facecolor='blue', alpha=0.5,label="venus")
axs[2].hist(min_ear_dist, len(min_ear_dist), facecolor='blue', alpha=0.5,label="earth")
axs[3].hist(min_mar_dist, len(min_mar_dist), facecolor='blue', alpha=0.5,label="mars")
axs[4].hist(min_sun_dist, len(min_sun_dist), facecolor='blue', alpha=0.5,label="sun")
plt.show()
#plt.savefig("comet histogram")
#sliku s 1000 cometa sam saveao ali kad je otvorim vidim samo bijelu boju 
# ovo je animacija sudara s marsom 
"""
comet = universe.Planet("comet", 1.989e15, np.array((3*au, 3*au)), np.array((-15000, -10000))) 

ss.add_planet(sun)
ss.add_planet(earth)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(mars)
ss.add_planet(comet)
    

ss.evolve(5.0*year)

fig, ax= plt.figure(figsize=(10,10)), plt.axes(xlim=(-5*au, 5*au), ylim=(-5*au, 5*au))

mercury_, = ax.plot([], [], 'o',color="gray")
venus_, = ax.plot([], [], 'o',color="purple")
earth_, = ax.plot([], [], 'o',color="blue")
mars_, = ax.plot([], [], 'o',color="red")
sun_, = ax.plot([], [], 'o',color="yellow")
comet_, =ax.plot([], [], 'o', color="green")

plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=2.0)
plt.plot(earth.x,earth.y,label=earth.name,color="blue")
plt.plot(mercury.x,mercury.y,label=mercury.name,color="grey")
plt.plot(venus.x,venus.y,label=venus.name,color="purple")
plt.plot(mars.x,mars.y,label=mars.name,color="red")
plt.plot(comet.x,comet.y,label=comet.name,color="green")
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")

x_mercury, x_venus, x_earth, x_mars, x_sun, x_comet = [], [], [], [], [], []
y_mercury, y_venus, y_earth, y_mars, y_sun, y_comet = [], [], [], [], [], []


def planets():

    mercury_.set_data([], [])
    venus_.set_data([], [])
    earth_.set_data([], [])
    mars_.set_data([], [])
    sun_.set_data([], [])
    comet_.set_data([], [])

    return mercury_, venus_, earth_, mars_, sun_,

def animation(i):

    x_sun.append(sun.x[i])
    y_sun.append(sun.y[i])

    x_mercury.append(mercury.x[i])
    y_mercury.append(mercury.y[i])
    
    x_venus.append((venus.x[i]))
    y_venus.append((venus.y[i]))

    x_earth.append((earth.x[i]))
    y_earth.append((earth.y[i]))

    x_mars.append((mars.x[i]))
    y_mars.append((mars.y[i]))
    
    x_comet.append(comet.x[i])
    y_comet.append(comet.y[i])

    mercury_.set_data(x_mercury[i], y_mercury[i])
    venus_.set_data(x_venus[i], y_venus[i])
    earth_.set_data(x_earth[i], y_earth[i])
    mars_.set_data(x_mars[i], y_mars[i])
    sun_.set_data(x_sun[i], y_sun[i])
    comet_.set_data(x_comet[i],y_comet[i])

    return mercury_,

animation = FuncAnimation(fig, animation, init_func=planets, interval=2)
plt.show()



