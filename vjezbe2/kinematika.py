import matplotlib.pyplot as plt
import numpy as np

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

