# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:12:10 2022

@author: Fabian
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 04:13:44 2022

EJERCICIO 7.1 SIMULACION

A= - wo^2/s^2+s(wo/Q)-wo^2

R2/Rt=1/3=0.33

@author: Fabian
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq

K=1
# Q=1

Q = [4, 2, 1, 0.707]

plt.close('all')

for i in range(len(Q)):
    
    num = np.array([K*1]) 
    den = np.array([1,1/Q[i],1])

    pretty_print_bicuad_omegayq(num,den)
    
    mi_sos = sig.TransferFunction(num,den)
    
    if i==0:
        analyze_sys(mi_sos, 'Q=4')
    
    elif i==1:
        analyze_sys(mi_sos, 'Q=2')
        
    elif i==2:
        analyze_sys(mi_sos, 'Q=1')

    elif i==3:
        analyze_sys(mi_sos, 'Q=0.707')
        
