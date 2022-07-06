# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:35:01 2022

@author: minus
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import  math





F = 1
V = 1
k0 = 9703*3600
Ea = 11843
dens_cp = 500
T_in = 25+273.15
Ca_in = 10
U_A = 150
Tj = 25+273.15
R = 1.987
delta_H = 5960
   
T_ = np.linspace(300,380,100)
k = k0*np.exp(-Ea/R/T_)
Ca = ((F*Ca_in)/V)/(F/V + k)
r = (k*Ca)
Tj = dens_cp*V/U_A*(F/V*(T_-T_in)-delta_H/dens_cp*r)+T_
    



#tiempo
#T_=np.linspace(300,380,100)

#Tj=(dens_cp*V/U_A)*(F/V)*(T_-T_in)-(delta_H/dens_cp)*(r_)
#Tj = dens_cp*V/U_A*(F/V*(T_-T_in)-delta_H/dens_cp*r_)+T_
#condiciones iniciales


#argumentos
#a21=-5
#a22=-7


#X = odeint(cstr2,x0,t)
plt.figure(1)
plt.plot(Tj,T_,'b')




