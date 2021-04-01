import particle as par
import numpy as np
import math as m
p1 = par.Particle(0,0,50,45,0.01)
#print(p1.total_time())
#print(p1.max_speed())

kut=[]
brz=[]
v_range = np.arange(0,100,1)
kut_range = np.arange(0,90,1)

#za brzinu

"""for i in range(len(v_range)):
    p2 = par.Particle(0,0,v_range[i],45,0.01,)
    brz.append(p2.velocity_to_hit_target(25,25,0.5))
    p2.reset()
brzi = list(filter(None, brz))
print(brzi[1],brzi[-1])"""

#nekad zna izbaciti listu s 2 ista broja kao min ili max, to se događa zbog vrijednosti epsilona u particle 

#za kut

"""for i in range(len(kut_range)):
    p3 = par.Particle(0,0,40,kut_range[i],0.01)
    kut.append(p3.angle_to_hit_target(25,25,3))
    p3.reset()
kuti = list(filter(None, kut))
print(kuti[1],kuti[-1])"""

#ako se smanji radius kuta moze se dogodit greska zbog epsilona u particle.isti kut se appenda vise puta pa izbaci gresku za element liste