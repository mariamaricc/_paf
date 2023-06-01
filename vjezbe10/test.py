import numpy as np
import matplotlib.pyplot as plt
import planet as p

planet = p.Planet(1.989 * (10**30),5.9742 * (10**24),np.array((0,0)),np.array((0,0)),np.array((1.486*(10**11),0)),np.array((0,29783)))
planet.move(60*60*24*365.242)

plt.figure(figsize=(7,7))
ax = plt.axes()
ax.set_facecolor("black") ##na bijeloj pozadini se Sunce ne vidi
plt.plot(planet.x_z,planet.y_z, c = "blue", label = "Zemlja")
plt.plot(planet.x_s,planet.y_s, c = "yellow", label = "Sunce")
plt.legend()
plt.show()