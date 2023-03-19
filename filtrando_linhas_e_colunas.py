# Comando 'loc[[]]' para filtrar linhas no DataFrame
# alunosDF.loc[alunosDF['Nome']=='Maurício'] Exemplo para localizar a linha de determinado elemento

import pandas as pd
import numpy as np

alunosDic = {'   Nome' : ['Ricardo', 'Maurício', 'Lucas', 'João'], \
    '   Nota' : [10, 6.5, 8, 7], '   Aprovado': ['Sim', 'Sim', 'Sim', 'Sim']}

alunosDF = pd.DataFrame(alunosDic)

print(alunosDF.loc[alunosDF["   Aprovado"]=="Sim"])

input()
 