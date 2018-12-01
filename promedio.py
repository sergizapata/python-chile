#! /usr/bin/python
# -*- coding: iso-8859-15 
n= int(input("ingrese la cantidad de datos: "))
suma=0
for i in range(n):
      x = float(input("ingrese el dato: "))
      suma=suma + x
prom = suma/n 
print("el promedio es: ", prom)     