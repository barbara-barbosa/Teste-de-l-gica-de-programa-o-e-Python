# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:25:45 2021

@author: bjesus
"""

import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as py
import matplotlib.pyplot as plt

df = pd.read_csv('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_201902.csv', sep=';')
df.query('CNPJ_FUNDO in ["17.797.493/0001-35"]', inplace=True)
df.head()

df['DT_COMPTC'] =  pd.to_datetime(df['DT_COMPTC'], format='%Y/%m/%d')
df['DT_COMPTC'] = df['DT_COMPTC'].dt.day

plt.figure()

plt.title('Gráfico Rendimento Mensal de fevereiro/2019 - Fundo SUL AMÉRICA APOLLO FUNDO DE INVESTIMENTO MULTIMERCADO\n')# Atribuindo um título ao gráfico
plt.plot( df['DT_COMPTC'],df['VL_TOTAL'])

plt.xlabel('Dias')
plt.ylabel('Valor total')

plt.show()

