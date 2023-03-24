import numpy as np
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
y_ = []
for i in range(6):
    y = 0.32 * φ[i]
    y_.append(y)
print(y_)
plt.scatter(φ, M)
plt.plot(φ,y_,'red')
plt.show()