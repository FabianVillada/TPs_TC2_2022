# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 08:26:25 2022

@author: Fabian
"""

import sympy as sp
from sympy.abc import s
from IPython.display import display, Math

Vi, Vo, Vx = sp.symbols("Vi, Vo, Vx")
G1, G2, Y1, Y2, R, C = sp.symbols("G1, G2, Y1, Y2, R, C")

aa = sp.solve([ 
                Vx*(Y1+Y2)-Vi*Y1,         # ecuacion nodo Vx entrada inversora opamp
                Vx*(G1+G2) -Vi*G1 -Vo*G2  # ecuacion nodo Vx entrada no inversora opamp
                ], 
                [Vi, Vo])                # Resuelve sist de ec lineal para Vi y Vo

transf_func = aa[Vo]/aa[Vi]


# Ejercicio 7.a: Pasatodo de 1er orden

tf7a = transf_func.subs(Y1, s*C)        #Remplaza  en transf_func Y1=s.C 
tf7a = tf7a.subs(Y2, 1/R)               #Remplaza  en transf_func Y2=1/R

num, den = sp.fraction(sp.simplify(sp.expand(tf7a)))

num = sp.Poly(num,s)
den = sp.Poly(den,s)


k = num.LC() / den.LC()     # num.LC() : devuelve el coeficiente principal de num

num = num.monic()
den = den.monic()

den_coeffs = den.all_coeffs()
wo = den_coeffs[-1]

tf7a_final = sp.Mul(k,num/den, evaluate=False)

print('')
print('################')
print('# SIMULACION SIMBOLICA sympy #')
print('################')
display(tf7a_final)
display(Math( r' \omega_o = ' + sp.latex(wo) ))