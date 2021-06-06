import zad1 as z
import numpy as np
import matplotlib.pyplot as plt
time_orbit = 60*60*24*365.242

sustav = z.Gravity()
sustav.medudjelovanje(time_orbit)

plt.figure(1, figsize=(5,5))
plt.scatter(0, 0)
plt.plot(sustav.x2_poz,sustav.y2_poz)
plt.show()