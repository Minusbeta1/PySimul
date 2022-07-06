# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:01:37 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def cstr(x,t,Ca,H):
    
    F=1
    V=1
    k0=9703*3600
    delta_H=-5900
    dens_cp=500
    T_in=298.15
    Ca0=10
    U_A=150
    T_chaqueta=298.15
    #R=1.987
    R=8.314
    Tj=1

    xdot=np.zeros(3)
    
    Ca=x[0]
    H=x[1]
    T=x[2]
    
    H_in=F*dens_cp*T_in-F*dens_cp*T
    Q=U_A*(Tj-T)
    
    xdot[0]=F*H_in+F*H+Q+(delta_H)*R*V
    xdot[1]=F*Ca0+F*Ca-R*V
    
    return xdot



#tiempo
t=np.linspace(0,15,1000)

#condiciones iniciales
x0=np.array([10,250])

#argumentos
#a21=-5
#a22=-7

a21=np.array([-4,-3,-2,-1])
a22=np.array([-2,-4,-6,-8])

L = np.size(a21)
#L2=len(21)


for i in range (L):
    
    
    X = odeint(cstr,x0,t,args=(a21[i],a22[i]))



    plt.plot(t,X[:,0])
    plt.plot(t,X[:,1])
    plt.plot(t,X[:,2])