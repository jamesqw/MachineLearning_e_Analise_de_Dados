# Nesse programa, usaremos Machine Learning para prever os tipos no Dataset Iris, além de, fazer testes para analisar qual
# o melhor valor de K em KNN.

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.25)

# Aqui é necessário alterar o valor de K de 1 até 25

counter = 1
dicionario_de_acuracias = {}

from sklearn.neighbors import KNeighborsClassifier

while counter <= 25:
    knn = KNeighborsClassifier(n_neighbors=counter)
    knn.fit(x_train, y_train)
    acuracia = knn.score(x_test, y_test)

    dicionario_de_acuracias[counter] = round(acuracia, 4)
    counter += 1

# Plotando resultados:

print(dicionario_de_acuracias)

plt.plot(list(dicionario_de_acuracias.keys()), list(dicionario_de_acuracias.values()))
plt.xlabel('Valores de K')
plt.ylabel('Acurácia')
plt.show()

