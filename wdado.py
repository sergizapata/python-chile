#! /usr/bin/python
# -*- coding: iso-8859-15 
from random import *
x=0
n= int(input("Ingrese la cantidad de intentos: "))
for i in range(n):
    x= randint (1,6)
    print(x)
    if x == 3:
        break
