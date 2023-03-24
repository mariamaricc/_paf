import matplotlib.pyplot as plt
import numpy as np
import math as math

def jednoliko_gibanje(F,m):
    x_liszt = []
    v_x =  []
    a_x = []
    t = []

    for i in range(10):
        t.append(i)
        a = (F/m)
        a_x.append(a)
        v = a*t[i]
        v_x.append(v)
        x = v*t[i]
        x_liszt.append(x)

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'x/[m]')
    ax.grid()
    plt.plot(t, x_liszt)
    plt.show()

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'v/[m/s]')
    ax.grid()
    plt.plot(t, v_x)
    plt.show()

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'a/[m/s**2]')
    ax.grid()
    plt.plot(t, a_x)
    plt.show()

def kosi_hitac(v_0, theta):
    dt = 0.1
    t = [0]
    x_liszt = [0]
    v_x = [v_0 * math.cos(math.radians(theta))]
    v_y = [0]
    a_x = [0]
    a_y = [0]

    for i in range(10):
        t.append(i+1)
        vx = v_x[i]
        v_x.append(vx)
        x = x_liszt[i] + v_x[i]*dt
        x_liszt.append(x)

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'x/[m]')
    ax.grid()
    plt.plot(t, x_liszt)
    plt.show()

    print(v_x,x_liszt)
