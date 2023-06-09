import math
import numpy as np
import matplotlib.pyplot as plt
k = 1

def f1(F,v,x,t):
    return 10

def f2(F,v,x,t):
    return -k*x

def gibanje(F,v,x,t,m=10):
    t = [0]
    v = [0]
    x = [0]
    a = [f2(F,v,x,t)/m]
    dt = 0.01
    
    for i in range(500):
        t.append(i*(dt))
        v.append(v[i] + a[i]*(dt))
        x.append(x[i] + v[i]*(dt))
        a.append(f2(F,v,x,t)/m)

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