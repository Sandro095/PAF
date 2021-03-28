import numpy as np
import particle as par
import matplotlib.pyplot as plt
p1 = par.Particle(10,20,50,45,0.001)
p1.range()
p1.plot_trajectory()
p1.ana_domet()
p1.relativa_greska()
rel_greska = []
p1.printInfo()


dt_ran = np.arange(0.01,0.5,0.001)


for i in range(len(dt_ran)):
    p2 = par.Particle(0,0,50,45,dt_ran[i])
    p2.range()
    p2.ana_domet()
    ef=p2.relativa_greska()
    rel_greska.append(ef)

plt.figure(1)
plt.plot(dt_ran,rel_greska,label="relativna pogreska")
plt.show()


    
    







