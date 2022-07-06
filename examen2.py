# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 17:05:12 2022

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





def Esfera(x,t):
    
    #parametros
    
    k=4.5
    alpha=1.1
    beta=0.8
    V=6
    radio=t**-1
    
    xdot = np.zeros(3)
    Ca=x[0]
    Cb=x[1]
    Cc=x[2]
    r=k*V*(Ca**alpha)*(Cb**beta)
    
    F_in=1
    F_in2=1
    f0=F_in+F_in2
    
    
    
    
    xdot[0] = (F_in*Ca+F_in2*Cb-f0*Cc+r)/(math.pi*radio**2)
          
          
          
    return xdot

    



#condiciones iniciales
h=0.001

t=np.arange(0,50+h,h)
x10=1
x20=1
x30=1
x0=np.array([x10,x20,x30])
#function


f=lambda t,x: Esfera(x, t)

X=RK4(f, x0, t)  
plt.figure(1)
plt.plot(t,X[0,:])