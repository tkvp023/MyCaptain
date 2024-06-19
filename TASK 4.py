# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:04:32 2024

@author: Vakilsearch
"""

E = [0,2,4,6,8]
N = [1,2,3,4,5]

k = []
a = E.copy()
b = N.copy()
for i in E:
    for j in N:
        if i == j:
            k.append(i)
            
            
for h in k:
   a.remove(h)
   b.remove(h)
print("Union of E and N:",E+N+k)
print("Intersection of E and N:",k)
print("Difference of Eand N",E)
print("Symmetric difference of E and N:",a+b)

