# O pandas serve para manipular objetos estruturais
# Função 'shape' conta as linhas e colunas de um DataFrame
# Função 'head()' encorpa o DF dando ênfase ao cabeçalho
# Função 'describe()' pega as colunas numéricas e traz informações sobre elas


import pandas as pd
import numpy as np

alunosDic = {'Nome' : ['Ricardo', 'Maurício', 'Lucas', 'João'], \
    'Nota' : [10, 6.5, 8, 7], 'Aprovado': ['Sim', 'Sim', 'Sim', 'Sim']}

alunosDF = pd.DataFrame(alunosDic)

print(alunosDF.head())

input()
 