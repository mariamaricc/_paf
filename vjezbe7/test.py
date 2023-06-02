import matplotlib.pyplot as plt
import particle as p

p1 = p.Projectile(0, 0, 60, 10, 1.225, 0, 0.01, 10, 1)
p1.euler()
plt.plot(p1.x, p1.y, c="red")
plt.show()