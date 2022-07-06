# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:12:50 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linalg as LA

def matrix(x,t):
    
    a11 = -1
    a12 = 2
    a21 = -2
    a22 = 0
           
    x1=x[0]
    x2=x[1]
    
    xdot=np.zeros(2)
    
    xdot[0]=a11*x1+a12*x2
    xdot[1]=a21*x1+a22*x2
    
    return xdot



#tiempo
t=np.linspace(0,10,1000)

#condiciones iniciales
#x0=np.array([3,2])

#argumentos
#a21=-5
#a22=-7

#a21=np.array([-4,-3,-2,-1])
#a22=np.array([-2,-4,-6,-8])

#A = np.array([-1,2],[-2,0])
x0=np.array([[2,3],[-2,3],[-2,-3],[2,-3]])

#x10 = np.array([2,3],[-2,3])
#x20 = np.array ([-2,-3],[2,-3])

#x0 = np.array([x10,x20])
#L = np.size(x0)
L=len(x0)
#w,v = LA.eig(np.diag(1,2,3))
#print(w)


for i in range (L):
    
    
    X = odeint(matrix,x0[i,:],t)
    #X = odeint(matrix,x0,t,args=())



    plt.plot(X[:,0],X[:,1])
    #plt.plot(t,X[:,1])    
    
    

