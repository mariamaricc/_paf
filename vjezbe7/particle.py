import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x_0, y_0, v_0, theta, rho, C_d, dt, m, A):
        self.t = [0]
        self.g = -9.81
        self.m = m
        self.rho = rho
        self.C_d = C_d
        self.A = A
        self.x = [x_0]
        self.y = [y_0]
        self.v_y = [v_0 * np.sin(theta * np.pi / 180)]
        self.v_x = [v_0 * np.cos(theta * np.pi / 180)]
        self.a_y = [self.g - (self.v_y[0] * self.C_d * self.rho * (self.v_y[0])**2) / (2 * self.m)]
        self.a_x = [(-self.v_x[0] * self.C_d * self.rho * (self.v_x[0])**2) / (2 * self.m)]
        self.dt = dt
    
    def __move(self):
        self.v_x.append(self.v_x[-1] + self.a_x[-1] * self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1] * self.dt)
        self.x.append(self.x[-1] + self.v_x[-1] * self.dt)
        self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
        self.a_x.append((-np.sign(self.v_x[-1]) * self.C_d * self.rho * (self.v_x[-1])**2) / (2 * self.m))
        self.a_y.append(self.g - (np.sign(self.v_y[-1]) * self.C_d * self.rho * (self.v_y[-1])**2) / (2 * self.m))
        self.t.append(self.t[-1] + self.dt)

    def __a_x(self, v):
        return (-np.sign(v) * self.C_d * self.rho * (v)**2) / (2 * self.m)

    def __a_y(self, v):
        return self.g - (np.sign(v) * self.C_d * self.rho * (v) / (2 * self.m))

    def __move_runge_kutta(self):
        k_1_v_x = self.__a_x(self.v_x[-1]) * self.dt
        k_2_v_x = self.__a_x((self.v_x[-1] + k_1_v_x / 2)) * self.dt
        k_3_v_x = self.__a_x((self.v_x[-1] + k_2_v_x / 2)) * self.dt
        k_4_v_x = self.__a_x((self.v_x[-1] + k_3_v_x)) * self.dt

        k_1_v_y = self.__a_y(self.v_y[-1]) * self.dt
        k_2_v_y = self.__a_y((self.v_y[-1] + k_1_v_y / 2)) * self.dt
        k_3_v_y = self.__a_y((self.v_y[-1] + k_2_v_y / 2)) * self.dt
        k_4_v_y = self.__a_y((self.v_y[-1] + k_3_v_y)) * self.dt

        self.v_x.append(self.v_x[-1] + 1 / 6 * (k_1_v_x + 2 * k_2_v_x + 2 * k_3_v_x + k_4_v_x))
        self.v_y.append(self.v_y[-1] + 1 / 6 * (k_1_v_y + 2 * k_2_v_y + 2 * k_3_v_y + k_4_v_y))

        k_1_x = self.v_x[-1] * self.dt
        k_2_x = (self.v_x[-1] + k_1_x / 2) * self.dt
        k_3_x = (self.v_x[-1] + k_2_x / 2) * self.dt
        k_4_x = (self.v_x[-1] + k_3_x) * self.dt

        k_1_y = self.v_y[-1] * self.dt
        k_2_y = (self.v_y[-1] + k_1_y / 2) * self.dt
        k_3_y = (self.v_y[-1] + k_2_y / 2) * self.dt
        k_4_y = (self.v_y[-1] + k_3_y) * self.dt

        self.x.append(self.x[-1] + 1 / 6 * (k_1_x + 2 * k_2_x + 2 * k_3_x + k_4_x))
        self.y.append(self.y[-1] + 1 / 6 * (k_1_y + 2 * k_2_y + 2 * k_3_y + k_4_y))


        self.t.append(self.t[-1] + self.dt)

    
    def euler(self):
        while self.y[-1] >= 0:
            self.__move()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]

    def runge_kutta(self):
        while self.y[-1] >= 0:
            self.__move_runge_kutta()
        if self.y[-1] < 0:
            del self.y[-1]
            del self.x[-1]

    def range(self):
        return sorted(self.x)[-1]