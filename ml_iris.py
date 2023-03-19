import pandas as pd
import sklearn.model_selection as sms 
import sklearn.ensemble as se

dados = pd.read_csv("C:/Users/CORE i5 6500/Desktop/Python/Projetos/Machine_Learning_e_Análise_de_Dados/Dataset/iris.csv")

dados['variety'] = dados['variety'].replace('Setosa', 0)
dados['variety'] = dados['variety'].replace('Versicolor', 1)
dados['variety'] = dados['variety'].replace('Virginica', 2)

y = dados['variety']
x = dados.drop('variety', axis= 1)

x_treino, x_teste, y_treino, y_teste = sms.train_test_split(x, y, train_size= 0.3)

modelo = se.ExtraTreesClassifier()

modelo.fit(x_treino, y_treino)
acuracia = modelo.score(x_teste, y_teste)

print('Acurácia: ', acuracia)

print(modelo.predict(x_teste[10:13]))
print(y_teste[10:13])