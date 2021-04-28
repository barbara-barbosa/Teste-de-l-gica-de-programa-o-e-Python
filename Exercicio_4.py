# -*- coding: utf-8 -*-
"""
Created on Apr 28 11:16:01 2021

@author: bbarbosa
"""
from datetime import date #importa a biblioteca datetime
import holidays #importa a biblioteca de feriados


print ("4. Faça um script em Python que receba duas datas como entrada em formato string e retorne quantos dias uteis (formato inteiro) possuem entre essas duas datas. Considerar os feriados brasileiros, os feriados brasileiros devem ser armazenados em memória. Considerar datas entre 2010 e 2021")

# lista de feriados brasileiros
feriados= holidays.Brazil() # atribui os feriados brasileiros para a variavel 'feriados'

i = 0 #atribui o valor 0 para a variavel i
for feriado in feriados['2019-01-01':'2020-12-31'] : #for para contar os feriados de 2019-2020
      #print(feriado)
      i+=1 #soma +1 para a variavel i enquanto o for conta os feriados
      #print(i)
      
inicial_data = date(2019, 1, 1) #data inicial 
final_data = date(2020, 12, 31) #data final

x = (final_data - inicial_data) # atribui a diferença entre as datas na variavel x
z = x.days-i #converte a variavel x para um numero inteiro de data e subtrai o valor total de feriados da variavel i
print("Quantidade de dias utéis entre 2019 a 2021:",z) #resultado na tela 



