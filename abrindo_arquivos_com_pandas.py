# Abrindo arquivos no Python usando Pandas
# Comando pd.read_(nome da plataforma) para ler

import pandas as pd

dados = pd.read_excel('C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Pasta1.xlsx')

print(dados.head(5))