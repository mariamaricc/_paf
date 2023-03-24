import numpy as np
import matplotlib.pyplot as plt

def function(N):
    a = 0
    b = 5
    for i in range (N):
        a = a + 1/3
        b = b - 1/3
    print(a,b)

function(2000)

#Objašnjenje: