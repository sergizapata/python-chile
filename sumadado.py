#! /usr/bin/python
# -*- coding: iso-8859-15 
from random import *
n= int(input("Ingrese la cantidad de intentos: "))
gana = 0
for i in range(n):
    x=randint(1,6)
    if x != 3:
        break
    
    else:
        print("el numero es: ", x) 
print("el numero es:: ", x) 