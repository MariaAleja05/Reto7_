# -*- coding: utf-8 -*-
"""Punto_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

# **Tercer Punto**

**Enunciado:** Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
"""

n = int(input("Ingrese un número mayor o igual a 2: "))
m=n
lista = []
numeros_pares =  []

while m<=n:
  if m>1:
    m -= 1
    if m%2==0:
      lista.append(m)
  else:
    break
print("Los números pares desde n hasta 2 son: " + str(lista))