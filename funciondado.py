#! /usr/bin/python
# -*- coding: iso-8859-15 
#escribir una funcion recursiva para contar en cuantos intentos se puede adivinar el numero de un dado

from random import *
def adivina(n):
        n = randint(1,6)
        return n
a = int(input("Adivina el numero: ")) 
for i in range(a):
    print adivina(i)  
    if a== adivina (i):
        print ("acerto ", a, i)
          
    else:
        print ("fallo ", a,i)       