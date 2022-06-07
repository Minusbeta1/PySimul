# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

def system(x,t):
    k1=0.5
    k2=0.4
    xdot=np.zeros(2)
    
    Ca=x[0]
    Cb=x[1]
    
    
    xdot[0]= -k1*Ca**2+k2*Cb
    xdot[1]= -k2*Cb+k1*Ca**2
    return xdot
    
   
h=0.1
t=np.arange(0,20+h,h)
Ca0=np.array([5,8])

f=lambda t,x: system(x, t)
y= RK4(f,Ca0,t)


plt.plot(t,y[0,:])
plt.plot(t,y[1,:])
plt.xlabel('time (s)')
plt.ylabel('Ca (mol/l)')
plt.legend(['$C_a$','$C_b$'])