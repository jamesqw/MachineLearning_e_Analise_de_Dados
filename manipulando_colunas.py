# Comando 'rename(columns={'':''})' para substituir o nome da coluna

#import pandas as pd
#import numpy as np

#alunosDic = {'   Nome' : ['Ricardo', 'Maurício', 'Lucas', 'João'], \
#    '   Nota' : [10, 6.5, 8, 7], '   Aprovado': ['Sim', 'Sim', 'Sim', 'Sim']}

#alunosDF = pd.DataFrame(alunosDic)
#alunosDF.rename(columns={'Nome' : '   Name', 'Nota' : '   Score',  \
#    '   Aprovado' : 'Approved'})

#print(alunosDF)

#input()
 
import pandas as pd 

dados = pd.read_csv("C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Dataset/athlete_events.csv")
# Lembre-se de arrumar o diretório do arquivo! (contrabarras e o nome no final)
# .value_counts() para detalhar as informações da coluna
# print(dados["Medal"].value_counts())

#------------------------------------------------------------------------------------------------------------------------------------------

# .drop("ID", axis=1) para excluir colunas. axis=1 (para colunas) e axis=0 (para linhas)
print(dados.drop("ID", axis=1))

input()



