import pandas as pd

dados = pd.read_csv("C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Dataset/athlete_events.csv")

dados2 = dados.dropna()
# Essa função deleta todas as linhas com dados faltantes

enulo = dados.isnull()
# Irá retornar se cada variável do DataSet é nula ou não (True or False)

faltantes = dados.isnull().sum()
# Soma quantos dados faltantes há em cada coluna

faltantes_percentual = (dados.isnull().sum() / len(dados["ID"]))*100
# Fórmula para calcular o percentual da NaN em cada coluna

substituir = dados['Medal'].fillna('Nada')
# Substitui os dados faltantes  
substituir2 = dados['Age'].fillna(dados['Age'].mean())
# Para substituir os NaN's pela média da coluna Age

print(faltantes_percentual)
