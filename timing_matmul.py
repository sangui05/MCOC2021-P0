# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 09:40:23 2021

@author: Sangui
"""

#matmul.py
from numpy import zeros
from time import perf_counter
#TAMAÑO
N =6000
A = zeros((N,N))+1
B = zeros((N,N))+2
t1 = perf_counter()
C=A@B
t2 = perf_counter()
dt = t2-t1
print (f"dt = {dt} s")

