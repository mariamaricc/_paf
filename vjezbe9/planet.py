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

    def reset(self,dt):
        self.__init__(self.r_s,self.r_z,self.v_s,self.v_z, self.a_s,self.a_z,self.m_s, self.m_z)