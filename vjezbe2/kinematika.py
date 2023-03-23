import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(F,m):
    a =[F/m]
    t = [0]
    v = [0]
    x = [0]
    dt = 0.001
    
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

def kosi_hitac(v_0, theta):
    t = [0]
    v_x = [v_0*np.cos((theta / 180)*np.pi)]
    v_y = [v_0*np.sin((theta / 180)*np.pi)]
    x = [0]
    y = [0]
    g = 9.81
    dt = 0.001

    for i in range(1000):
        t.append(i*(dt))
        v_x.append(v_0*np.cos((theta / 180)*np.pi))
        v_y.append(v_y[i]-g*(dt))
        x.append(x[i]+v_x[i]*(dt))
        y.append(y[i]+v_y[i]*(dt))
    
    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'x/[m]')
    ax.grid()
    plt.plot(t, x)
    plt.show()

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'y/[m]')
    ax.grid()
    plt.plot(t, y)
    plt.show()

    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 'y/[m]', ylabel = 'x/[m]')
    ax.grid()
    plt.plot(x,y)
    plt.show()
    