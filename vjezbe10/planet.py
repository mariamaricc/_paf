import numpy as np
import matplotlib.pyplot as plt
import math

class Planet:
    def __init__(self,m_s,m_z,r_s,v_s,r_z,v_z,dt = 10**4):
        self.x_z = []
        self.y_z = []
        self.x_s = []
        self.y_s = []
        self.m_s = m_s
        self.m_z = m_z
        self.r_s = r_s
        self.v_s = v_s
        self.r_z = r_z
        self.v_z = v_z
        self.G =  6.67408 * (10**(-11))
        self.x_z.append(r_z[0])
        self.y_z.append(r_z[1])
        self.x_s.append(r_s[0])
        self.y_s.append(r_s[1])
        self.t = 0
        self.dt = dt

    def __move(self):

        d1 = math.sqrt((self.r_s[0] - self.r_z[0])**2 + (self.r_s[1] - self.r_z[1])**2)
        self.a1 = -self.G * self.m_z/(d1**3) * np.subtract(self.r_s,self.r_z)
        self.v_s = np.add(self.v_s,self.a1*self.dt)
        self.r_s = np.add(self.r_s,self.v_s*self.dt)
        d2 = math.sqrt((self.r_z[0] - self.r_s[0])**2 + (self.r_z[1] - self.r_s[1])**2)
        self.a2 = -self.G * self.m_s/(d2**3) * np.subtract(self.r_z,self.r_s)
        self.v_z = np.add(self.v_z,self.a2*self.dt)
        self.r_z = np.add(self.r_z,self.v_z*self.dt)

    def move(self,t):
        while self.t <= t:
            self.__move()
            self.x_z.append(self.r_z[0])
            self.y_z.append(self.r_z[1])
            self.x_s.append(self.r_s[0])
            self.y_s.append(self.r_s[1])
            self.t += self.dt
        return self.x_z, self.y_z, self.x_s , self.y_s