import matplotlib.pyplot as plt
import particle as p

p1 = p.Projectile(0, 0, 60, 10, 1.225, 0, 0.01, 10, 1)
p2 = p.Projectile(0, 0, 60, 10, 1.225, 0, 0.01, 10, 1)
p3 = p.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.01, 10, 1)
p4 = p.Projectile(0, 0, 60, 10, 1.225, 0.47, 0.01, 10, 1)

p1.runge_kutta()
p2.euler()
p3.runge_kutta()
p4.euler()

plt.plot(p1.x, p1.y, c="red")
plt.scatter(p2.x, p2.y, c="blue", s=2.5)
plt.plot(p3.x, p3.y, c="green")
plt.scatter(p4.x, p4.y, c="purple", s=2.5)

plt.legend([
    "runge kutta, dt = 0.01, bez otpora zraka",
    "euler, dt = 0.01, bez otpora zraka",
    "runge kutta, dt = 0.01, s otporom zraka",
    "euler, dt = 0.01, s otporom zraka"
])
plt.show()