# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:38:07 2022

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





def Fermentador(x,t):
    
    #parametros
    umax=1.5
    K=3
    D=0.1
    F=1 #wa
    V=1 #wa
    Y=0.9
    if t <= 20 :
        S_in = 18
        
    else:
        S_in = 7
        
    X=x[0]
    S=x[1]
    
    mu = (umax*S)/(K+S)
    
    xdot = np.zeros(2)
    
    #xdot[0]=(f1/v)*(Ca1)-(f0/v)*Ca-r
    #xdot[1]=(f2/v)*(Cb1)-(f0/v)*Cb-r
    
    xdot[0]=(-F/V)*X+Y*mu*X
    
    xdot[1]=(S_in-S)-mu*X
    
    
    return xdot


#condiciones iniciales
x0=2
y0=0.9
s0=10
h=0.1
t=np.arange(0,300+h,h)
x0=np.array([x0,s0])
#function


f=lambda t,x: Fermentador(x, t)

X=RK4(f, x0, t)  
plt.figure(1)
plt.plot(t,X[0,:])
plt.figure(2)
plt.plot(t,X[1,:])  
plt.figure(3)
plt.plot(X[0,:],X[1,:])







