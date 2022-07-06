# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:49:32 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def ODE_solver(x,t,a21,a22):
    
    a11,a12 = -1,2
    x1=x[0]
    x2=x[1]
    
    xdot=np.zeros(2)
    
    xdot[0]=a11*x1+a12*x2
    xdot[1]=a21*x1+a22*x2
    
    return xdot



#tiempo
t=np.linspace(0,5,1000)

#condiciones iniciales
x0=np.array([3,2])

#argumentos
#a21=-5
#a22=-7

a21=np.array([-4,-3,-2,-1])
a22=np.array([-2,-4,-6,-8])

L = np.size(a21)
#L2=len(21)


for i in range (L):
    
    
    X = odeint(ODE_solver,x0,t,args=(a21[i],a22[i]))



    plt.plot(t,X[:,0])
    plt.plot(t,X[:,1])    
    
    

