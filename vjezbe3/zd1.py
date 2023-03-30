import numpy as np
import matplotlib.pyplot as plt

#a)
i = 5.0
j = 4.935
print(i-j)
#Očekujem 0.065.
#Rezultat koji dobijem koristeći Python je 0.06500000000000039. To je zato što Python zna pretvoriti u konačni binarni zapis samo brojeve oblika 1/2**(na n-tu). Sve ostalo su aproksimacije koje ovise o veličini memorije.


#b)
a = 0.1
b = 0.2
c = 0.3
d = a+b+c
if (d==0.6):
    print("jest")
else:
    print("nije",d)
#Python kaže da 0.1 + 0.2 + 0.3 nije jednako 0.6. Rezultat ovisi o tome na koliko decimala zaokružimo broj.