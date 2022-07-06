# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:04:36 2022

@author: minus
"""

import numpy as np
from scipy.optimize import fsolve

def execute(z):
    
    #y=8*x**3+6*x**2+2
    
    Z=np.zeros(2)
    
    x=z[0]
    y=z[1]
    
    Z[0]=x**2*y+2*x
    Z[1]=y**2*x+2*y
    
    
    return Z



root=fsolve(execute,[-2.5,5])

print(root)








#def func(x):
#    return [x[0] * np.cos(x[1]) - 4,
#            x[1] * x[0] - x[1] - 5]
#root = fsolve(func, [50, 25])
#print(root)