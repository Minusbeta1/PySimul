# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:31:20 2022

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
    
    #parametros
    R=3
    H=8
    C=0.5
    F_in=3
    h=x[0]
        
    
    xdot = np.zeros(1)
    
    #xdot[0]=(f1/v)*(Ca1)-(f0/v)*Ca-r
    #xdot[1]=(f2/v)*(Cb1)-(f0/v)*Cb-r
    
    xdot[0]=((F_in-C*np.sqrt(h))*H**2)/(math.pi*R**2*h**2)
          
          
          
    return xdot

    



#condiciones iniciales
h=0.001

t=np.arange(0,50+h,h)
x10=0.5
x0=np.array([x10])
#function


f=lambda t,x: Cono(x, t)

X=RK4(f, x0, t)  
plt.figure(1)
plt.plot(t,X[0,:])
