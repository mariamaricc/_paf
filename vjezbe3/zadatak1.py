import numpy as np
import matplotlib.pyplot as plt

#a)
i = 5.0
j = 4.935
print(i-j)
#Očekujem da će ispisati 0.065
#Zapravo je ispisao 0.06500000000000039. Zašto?

#b)
m = 0.1
n = 0.2
l = 0.3
o = m+n+l
p = 0.6
if (o==p):
    print("Brojevi su isti.")
else:
    print("Brojevi nisu isti.")