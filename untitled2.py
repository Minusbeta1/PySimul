# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 17:10:53 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
#import pylab as pl
import  math
#math.pi

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





def Cono(x,t):
    
    k1=100000
    k2=0.1
    k3=2e-7
    k4=0.5
    
    if t<=6:
        k5=5
    else:
        k5=8
    
    k6=100
    
    xdot=np.zeros(3)
    
    H=x[0]
    V=x[1]
    I=x[2]
    
    xdot[0]=-k3*H*V-k5*V+k6*I
    xdot[1]=k3*H*V-k4*I
    xdot[2]=k1-k2*H-k3*H*V
    
    
    return xdot

    



#condiciones iniciales
h=0.002

x10=100
x20=0
x30=1000000

t=np.arange(0,15+h,h)
x0=np.array([x10,x20,x30])
#function


f=lambda t,x: Cono(x, t)

X=RK4(f, x0, t)  
plt.figure(1)
plt.plot(t,X[0,:])