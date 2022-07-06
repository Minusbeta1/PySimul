# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 18:24:53 2022

@author: minus
"""

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def system (x,t):
    
    k=4
    v=0.7
    D=2.1e-2
    
    
    
    return system


def optm(y20):
    
    z=np.linspace(0,1,3000)
    x=odeint(system,[3,y20],z)
    lx=len(x)
    yl=x[lx-1,1]
    y2l=0
    error=(yl-y2l)**2
    
    return error


y20=fsolve(optm,-3)
z=np.linspace(0,1,3000)
x=odeint(system,[3,y20],z)


