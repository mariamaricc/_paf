import numpy as np
<<<<<<< HEAD
import math
import matplotlib.pyplot as plt


def mean_stdev(x):
    n = 0
    x_mean = 0

    for i in range(10):
        x_mean = x_mean + x[i]
        n = n + 1
    print(x_mean/n)

    a = 0
    j = 0

    for i in range(10):
        a = a + (x[i]-x_mean/n)**2
        j = j + 1
    stdev = math.sqrt(a/(j*(j-1)))
    print(stdev)

mean_stdev(x = [1,2,3,4,5,6,7,8,9,10])
=======
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
>>>>>>> 5262214eb0bbbc23051517b6ac2ec94ebed5baea
