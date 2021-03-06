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

def IntP03_2(x,t):
    
    k1 = 0.564
    k2 = 0.333
    k3 = 1
    F1 = 4
    F2 = 5
    A = 1
    
    
    
    
    if t<=5:
        Ca_in = 5
        Cb_in = 7
    else:  
        Ca_in = 7
        Cb_in = 5
    
    
    
    xdot=np.zeros(4)
    
    Ca = x[0]
    Cb = x[1]
    Cc = x[2]
    h = x[3]
    rc = h*A*(k1*Ca**2*Cb-k2*Cc**2.5)
    rb = -rc
    ra = -2*rc
    Fo = k3*np.sqrt(h)
    
    
    xdot[0] = (F1*Ca_in-Fo*Ca+ra)/(h*A)
    xdot[1] = (F2*Cb_in-Fo*Cb+rb)/(h*A)
    xdot[2] = (-Fo*Cc+rc)/(h*A)
    xdot[3] = (F1+F2-Fo)/(A)
    return xdot


h = 0.01
t=np.arange(0,15+h,h)
x0=np.array([0,0,0,1])

f = lambda t2,x: IntP03_2(x, t2)
X = RK4(f,x0,t)

plt.figure(1)
plt.plot(t,X[0,:])


plt.figure(2)
plt.plot(t,X[1,:])

plt.figure(3)
plt.plot(t,X[2,:])