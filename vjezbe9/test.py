import numpy as np
import matplotlib.pyplot as plt
import planet as p

zemlja_sunce = p.Planet(np.array([1.496*10**(11), 0]), np.array([0.1, 0.1]), np.array([0, 29783]), np.array([0, 0]), np.array([0, 0]), np.array([0, 0]), 5.9742*10**(24), 1.989*10**(30))
x1, y1, x2, y2 = zemlja_sunce.range(100)

plt.figure(figsize=(5.5, 5.5))
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(["Zemlja", "Sunce"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()