import math
import numpy as np
import matplotlib.pyplot as plt

def f(F,x,v,t,m):
    dt = 0.01
    a = [F/m]
    
    for i in range(1000):
        t.append(i*(dt))
        v.append(v[i]+a[i]*(dt))
        x.append(x[i]+v[i]*(dt))
        a.append(F/m)

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'x/[m]')
    ax.grid()
    plt.plot(t, x)
    plt.show()

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'v/[m/s]')
    ax.grid()
    plt.plot(t, v)
    plt.show()

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'a/[m/s**2]')
    ax.grid()
    plt.plot(t, a)
    plt.show()
    return F(x,v,t)