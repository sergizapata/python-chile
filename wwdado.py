#! /usr/bin/python
# -*- coding: iso-8859-15 
# simular el lanzamiento de un dado y determine la cantidad de lanzamientos hasta que salga el numero 5
from random import *
x = 0
# n = int(input("Ingrese la cantidad de intentos: "))
while True:
    x= randint (1,6)
    print(x)
    i=x+1
    if x == 5:
        break
    print("el lanzamiento en el que salio el 5 fue: ", i)    