import numpy as np
import matplotlib.pyplot as plt

class Particle():
    def __init__(self, v_0, theta, x_0, y_0):
        self.x = []
        self.y = []
        self.t = []
        self.v_x = []
        self.v_y = []
        self.a_x = []
        self.a_y = []
        self.v_0 = v_0
        self.theta = theta
        self.x_0 = x_0
        self.y_0 = y_0
        self.g = 9.81
        
        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.v_x = [self.v_0*np.cos((self.theta / 180)*np.pi)]
        self.v_y = [self.v_0*np.sin((self.theta / 180)*np.pi)]
        self.a_x.append(0)
        self.a_y.append(9.81)

        print(self.v_0, self.theta, self.x_0, self.y_0)

    def __move(self):
        dt = 0.01
        self.t.append(self.t[-1]+dt)
        self.v_y.append(self.v_y[-1] - self.g*dt)
        self.v_x.append(self.v_x[-1]+self.a_x[-1]*dt)
        self.x.append(self.x[-1] + self.v_x[-1]*dt)
        self.y.append(self.y[-1] + self.v_y[-1]*dt)
        
    def plot_trajcetory(self):
        fig = plt.figure()
        ax = plt.axes()
        ax.set(xlabel = 'x/[m]', ylabel = 'y/[m]')
        ax.grid()
        plt.plot(self.x,self.y)
        plt.show()

    def range(self):
        while(self.y[-1] >= 0):
            self.__move()
        return self.x[-1]

    def reset(self):
        self.__init__(self.v_0, self.theta, self.x_0, self.y_0)
        print(self.v_0, self.theta, self.x_0, self.y_0)