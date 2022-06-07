# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:20:42 2022

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

def Lotk(x,t):
    alpha=1.1
    beta=0.4
    gamma=0.4
    delta=0.1
    
    xdot=np.zeros(2)
    
    xdot[0]=alpha*x[0]-beta*x[0]*x[1]
    xdot[1]=delta*x[0]*x[1]-gamma*x[1]

    return xdot

h=0.01
x10=20
x20=5
t=np.arange(0,300+h,h)
x0=np.array([x10,x20])


#function


f=lambda t,x: Lotk(x, t)

X=RK4(f, x0, t)  
plt.figure(1)
plt.plot(t,X[0,:])
plt.figure(2)
plt.plot(t,X[1,:])  
plt.figure(3)
plt.plot(X[0,:],X[1,:])
