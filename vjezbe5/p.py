import calculus as calc
import math as m 
import numpy as np 
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
x_os, y_os = calc.raspon(calc.g, -10, 10, 0.01)
y_os2 = []
x_os3, y_os3 = calc.raspon(calc.g, -10, 10, 0.01)

for i in x_os:
    y_os2.append(calc.a_g(i))

axes[0].plot(x_os, y_os)
axes[0].scatter(x_os, y_os2, s=5)
axes[0].scatter(x_os3, y_os3, s=5, color="red")

x_os_, y_os_ = calc.raspon(calc.f, -2, 2, 0.01)
y_os2_ = []
x_os3_, y_os3_ = calc.raspon(calc.f, -2, 2, 0.01)

for i in x_os_:
    y_os2_.append(calc.a_f(i))

axes[1].plot(x_os_, y_os_, color="green")
axes[1].scatter(x_os_, y_os2_, s=5, color="magenta")
axes[1].scatter(x_os3_, y_os3_, s=5, color="red")

plt.show()