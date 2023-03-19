import pandas as pd
import sklearn.model_selection as sms
import sklearn.ensemble as se

dados = pd.read_csv("C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Dataset/wine_dataset.csv")

# Trataremos como variável target a “style”, que define se o vinho em questão é tinto ou branco
# Após definida a target, precisamos mudar os termos 'red' e 'white' para valores numéricos a fim de o programa conseguir trabalhar

dados['style'] = dados['style'].replace('red', 0)
dados['style'] = dados['style'].replace('white', 1)

# Agora precisamos separar as variáveis entre preditoras e alvo
# "alvo" é a variável alvo que queremos prever e "preditoras" é todo o resto

y = dados['style']
x = dados.drop('style', axis = 1)

# Vamos separar os dados em treino e teste para a melhor compreensão do algoritmo

x_treino, x_teste, y_treino, y_teste = sms.train_test_split(x, y, test_size = 0.3)
# Na função "train_test_split", nós indicamos primeiro a variável preditora e depois a alvo. O "test_size" irá definir a quantidade em % que o programa separará para teste.
# Nesta função em destaque, as variáveis alvo e preditoras serão divididas em quatro grupos de dois pares onde cada um será posteriormente utilizado pelo ML para aprender e testar

# Machine Learning:

modelo = se.ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)
# Conjunto de dados para se treinar
resultado = modelo.score(x_teste, y_teste)
# Através do que já foi aprendido, o algoritmo irá prever as classes das amostras
# Então, trará em forma de porcentagem quantas classes de amostras foram previstas corretamente

print("Acurácia:", resultado)
previsoes = modelo.predict(x_teste[400:403])
print(y_teste[400:403])
print(previsoes)
# Aqui usamos a função "predict" para ver na prática se o modelo acertou em suas previsões, utilizando a variável y_teste que é o gabarito.
