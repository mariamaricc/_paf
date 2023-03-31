import matplotlib.pyplot as plt
import numpy as np
import math as math

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
<<<<<<< HEAD
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

=======
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
    
>>>>>>> 5262214eb0bbbc23051517b6ac2ec94ebed5baea
    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlabel = 't/[s]', ylabel = 'x/[m]')
    ax.grid()
<<<<<<< HEAD
    plt.plot(t, x_liszt)
    plt.show()

    print(v_x,x_liszt)
=======
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
    
>>>>>>> 5262214eb0bbbc23051517b6ac2ec94ebed5baea
