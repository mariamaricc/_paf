import math
import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self,m_z, m_s,r_z,r_s,v_z,v_s, a_z,a_s):
        self.r_z = r_z
        self.r_s = r_s
        self.x_z = [1.486*(10**11)]
        self.y_z = [0]
        self.x_s = [0]
        self.y_s = [0]
        self.v_z = v_z
        self.v_s = v_s
        self.a_z = a_z
        self.a_s = a_s
        self.G = 6.67408*(10**(-11))
        self.t = [0]
        self.m_z = m_z
        self.m_s = m_s
        self.t_uk = 365.242*24*3600

    def __move(self,dt):
        d1 = (self.r_z - self.r_s)**2
        d2 = (self.r_s - self.r_z)**2
        n1 = math.sqrt(d1[0] + d1[1])
        n2 = math.sqrt(d2[0] + d2[1])

        self.t.append(self.t[-1] + dt)

        self.a_z = -self.G*(self.m_s / n1**3 )*(self.r_z - self.r_s)
        self.a_s = -self.G*(self.m_z / n2**3 )*(self.r_s - self.r_z)

        self.v_z = self.v_z + self.a_z*dt
        self.v_s = self.v_s + self.a_s*dt

        self.r_z = self.r_z + self.v_z*dt
        self.r_s = self.r_s + self.v_s*dt

        self.x_z.append(self.r_z[0])
        self.y_z.append(self.r_z[1])
        self.x_s.append(self.r_s[0])
        self.y_s.append(self.r_s[1])

    def range(self, dt):
        while self.t[-1] <= self.t_uk:
            self.__move(dt)
        return self.x_z, self.y_z, self.x_s, self.y_s

    def reset(self,dt):
        self.__init__(self.r_s,self.r_z,self.v_s,self.v_z, self.a_s,self.a_z,self.m_s, self.m_z)