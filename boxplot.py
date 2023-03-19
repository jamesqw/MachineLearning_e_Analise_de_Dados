# Lembre dos conceitos de quatil e percentil
# Fórmula para calcular os limites superior e inferior de um boxplot: ()
# () LS = Q3 + 1,5*(Q3-Q1), LI = Q1 - 1,5(Q3-Q1). Com isso, podemos encontrar os outliers do conjunto de dados

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Dataset/athlete_events.csv")

print(dados.boxplot(column=['Age', 'Height', 'Weight']))

plt.show()
