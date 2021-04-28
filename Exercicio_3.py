# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:00:15 2021

@author: bbarbosa

"""
print (" 3.Escreva um script em Python que gere a sequência de Fibonacci (em formato de lista) dado um valor n em formato inteiro.")
x = int( input(" Digite Quantos termos você deseja mostrar na sequência de Fibonacci:")) # Armazena o número digitado inteiro na variavel 
x1 = 1
x2 = 0
x3 = 0
x4 = []

while x1 <= x: #enquanto for verdadeiro executa (enquanto x1 for menor igual ao valor inserido)
    x4.append(x1) # Adiciona o valor ao fim da lista enquanto for verdadeiro a condição
    x3 = x1 + x2 
    x2 = x1
    x1 = x3

print(x4) # Escreva o resultado da lista criada na variavel x4