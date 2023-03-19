# Histograma é um gráfico que mostra quantas vezes determinados valores ocorreram

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Dataset/athlete_events.csv")

dados.hist(column="Age", bins=100)
# Utilizando a função ".hist" do pandas para gerar um gráfico (neste caso) de 100 barras.

plt.show()