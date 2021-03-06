# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:41:06 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
#import pylab as pl

def RK4 (f,x0,t):
    
    
    
    # Runge- Kutta method 
    
  dt= t[1] - t[0]  # ste size 
  nt = t.size  # array size 
  nx  = x0.size  # array size 
  x = np.zeros ((nx,nt))  # zeros array 
  x[:,0] = x0   # Initial condition 
    
    # Starting method
    
  for k in range (nt - 1):

# Define the method 
        k1 = dt*f( t[k], x[:,k] )
        k2 = dt*f( t[k] + dt/2, x[:, k] + k1/2 )
        k3 = dt*f( t[k] + dt/2, x[:, k] + k2/2 ) 
        k4 = dt*f( t[k] + dt, x[:, k] + k3 )

# Adding temrs 
        dx = (k1+2*k2+2*k3+k4)/6
 
 # Compute next value 
        x[:,k+1] = x[:,k] + dx
 
 # Return the array 
  return x


def IntP03_3(x,t):
    beta = 0.4
    gamma = 0.04
    
    xdot=np.zeros(3)
    
    s = x[0]
    i = x[1]
    r = x[2]
    
    N = s+i+r
    
    
    xdot[0]= -beta*s*i/N
    xdot[1]= beta*s*i/N-gamma*i
    xdot[2]= gamma*i
    return xdot


h = 0.01
t = np.arange(0,100+h,h)
x0 = np.array([997,3,0])

f=lambda t,x: IntP03_3(x, t)
X= RK4(f,x0,t)

plt.figure(1)
plt.plot(t,X[0,:])

plt.figure(2)
plt.plot(t,X[1,:])

plt.figure(3)
plt.plot(t,X[2,:])