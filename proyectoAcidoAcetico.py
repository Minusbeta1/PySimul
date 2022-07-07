# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:50:03 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def RK4(f,x0,t):
    #Runge-Kutta method
    dt=t[1]-t[0] #ste size
    nt=t.size    #array size
    nx=x0.size   #array size
    x=np.zeros((nx,nt)) #zeros array
    x[:,0]=x0           #initial condition
    
    
    #Starting method
    for k in range(nt-1):
        
        #Define the method constants
        
        k1=dt*f(t[k], x[:,k])
        k2=dt*f(t[k]+dt/2, x[:,k]+k1/2)
        k3=dt*f(t[k]+dt/2,x[:,k]+k2/2)
        k4=dt*f(t[k]+dt,x[:,k]+k3)
        
        #Adding terms
        
        dx=(k1 + 2*k2 + 2*k3 +k4)/6
        
        #Compute next value
        x[:,k+1]=x[:,k]+dx
        
    #Return the array
    return x
 




def system (x,t):
    
    u0=0.175
    a1=0.0192
    b0=1
    b3=1.67e-4
    c=3.5e-5
    n=2
    pi0=20
    m=2
    pm=90
    gamma=0.03
    
    xdot=np.zeros(4)
    
    Xv=x[0]
    Xnv=x[1]
    Xd=x[2]
    P=x[3]
    
    u=(u0*(1+a1*P))/(b0+b3*P**3)
    k=c*P**n
    pi=pi0*(1-(P/pm)**m)
    
    

    
    xdot[0]=(u*P-k*P)*Xv
    xdot[1]=k*P*Xv-gamma*Xnv
    xdot[2]=gamma*Xnv
    xdot[3]=(pi*P)*(Xv+Xnv)
    
    return xdot

h=0.1
t=np.arange(0,100+h,h)
x10=0.5
x0=np.array([x10])
f=lambda t,x: system(x, t)
X=RK4(f,x0,t)
plt.figure(1)
plt.plot(t,X[0,:])
plt.figure(2)
plt.plot(t,X[1,:])
plt.figure(3)
plt.plot(t,X[2,:])
plt.figure(4)
plt.plot(t,X[3,:])
