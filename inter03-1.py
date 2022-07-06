# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:41:07 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

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

def IntP03_1(x,t):
    
    
    a11=-13
    a12=1
    a21=0
    a22=-0.4
    x1=x[0]
    x2=x[1]
    
    xdot=np.zeros(2)
    
    xdot[0]=a11*x1+a12*x2
    xdot[1]=a21*x1+a22*x2

    return xdot

h=0.01
x10=50
x20=60
t=np.arange(0,10+h,h)
x0=np.array([x10,x20])


#function


f=lambda t,x: IntP03_1(x, t)

X=RK4(f, x0, t)  
plt.figure(1)
plt.plot(t,X[0,:])
plt.figure(2)
plt.plot(t,X[1,:])  