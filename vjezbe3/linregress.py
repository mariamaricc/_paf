import math
import numpy as np
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] 
φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
D = []
d = 0

for i in range(6):
    d = round(M[i] / φ[i],4)
    D.append(d)
print(D)

d1 = 0
m = 0
for i in range(6):
        d1 += D[i]
        m += 1
print(round(d1/m,2))

fig = plt.figure()
ax = plt.axes()
ax.set(xlabel = 'φ[rad]', ylabel = 'M[Nm]')
ax.grid()
plt.scatter(φ, M)
plt.show()
