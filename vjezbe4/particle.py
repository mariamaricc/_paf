import numpy as np
import matplotlib.pyplot as plt

class Particle():
    def __init__(self, v_0, theta, x_0, y_0):
        self.v_0 = v_0
        self.theta = theta
        self.x_0 = x_0
        self.y_0 = y_0
        print(self.v_0, self.theta, self.x_0, self.y_0)

    def move(self):
        t = [0]
        v_x = [self.v_0*np.cos((self.theta / 180)*np.pi)]
        v_y = [self.v_0*np.sin((self.theta / 180)*np.pi)]
        x = [0]
        y = [0]
        g = 9.81
        dt = 0.01
        for i in range(100):
            t.append(i*(dt))
            v_x.append(self.v_0*np.cos((self.theta / 180)*np.pi))
            v_y.append(v_y[i]-g*(dt))
            x.append(x[i]+v_x[i]*(dt))
            y.append(y[i]+v_y[i]*(dt))
        fig = plt.figure()
        ax = plt.axes()
        ax.set(xlabel = 'y/[m]', ylabel = 'x/[m]')
        ax.grid()
        plt.plot(x,y)
        plt.show()

    def range(self):
        R = (self.v_0**2)*np.cos((self.theta / 180)*np.pi)/9.81
        print(round(R,5))

    def reset(self):
        self.v_0 = 0
        self.theta = 0
        self.x_0 = 0
        self.y_0 = 0
        print(self.v_0, self.theta, self.x_0, self.y_0)