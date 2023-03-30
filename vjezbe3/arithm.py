import numpy as np
import matplotlib.pyplot as plt
import math

def arithm (x):
    x_mean = 0
    n = 0
    for i in range (10):
        x_mean += x[i]
        n += 1
    print(x_mean/n)

    a = 0
    b = 0
    for i in range(10):
        a += (x[i] - x_mean/n)**2
        b += 1
    σ = math.sqrt(a/(b*(b-1)))
    print(round(σ,5))
arithm([1,2,3,4,5,6,7,8,9,10])