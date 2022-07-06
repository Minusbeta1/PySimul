# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:51:36 2022

@author: minus
"""
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def cstr(x,t):
    
    F = 1
    V = 1
    k0 = 9703*3600
    Ea = 11843
    dens_cp = 500
    T_in = 25+273.15
    Ca_in = 10
    U_A = 150
    Tj = 25+273.15
    R = 1.987
    delta_H = 5960
       
    

    
    xdot=np.zeros(2)
    Ca=x[0]
    T_=x[1]
    
    k = k0*np.exp(-Ea/R/T_)
    r = (k*Ca)
    
    xdot[0]=(F*Ca_in)/V-(F*Ca)/V-r
    xdot[1]=(F*T_in)/V-(F*T_)/V+(U_A*(Tj-T_))/(dens_cp*V)+((delta_H)*r)/dens_cp
    
    #Tj = dens_cp*V/U_A*(F/V*(T_-T_in)-delta_H/dens_cp*r)+T_
    
    return xdot



t=np.linspace(0,250,400)
T0=np.linspace(300,420,10)
Ca0=np.linspace(0.001,10,10)
LT=len(T0)
LCa=len(Ca0)


for i in range(LT):
    for j in range(LCa):
        X=odeint(cstr,[Ca0[j],T0[i]],t)

        plt.plot(X[:,0],X[:,1])
        
        
        


root=fsolve(cstr,[2.3,370],args=(2,))
plt.plot(root[0],root[1],'r*',linewidth=7)
print(root)

root=fsolve(cstr,[5.8,350],args=(2,))
plt.plot(root[0],root[1],'r*',linewidth=7)
print(root)

root=fsolve(cstr,[10,225],args=(2,))
plt.plot(root[0],root[1],'r*',linewidth=7)
print(root)

plt.figure(3)
plt.subplot(2,1,1)
plt.plot(t,X[:,0])

plt.figure(3)
plt.subplot(2,1,1)
plt.plot(t,X[:,1])






