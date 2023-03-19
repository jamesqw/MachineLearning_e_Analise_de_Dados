import numpy as np

# O array cria uma lista com algumas restrições, uma vez que todos os elementos devem ser do mesmo tipo
a = np.array([(1,2,3), (4,5,6)])
# array([(), ()]) para arrays com mais de uma dimensão
# a.max() = puxa o maior ekemento da matriz e a.min() para o menor
# a.sum() soma, a.mean() calcula a média, a.std() calcula o desvio padrão

#------------------------------------------------------------------------------------------------------------

b = np.zeros((4, 3))
# Dentro dos parênteses é informada a dimensão
# np.ones; 

#------------------------------------------------------------------------------------------------------------

c = np.eye(4)
# Essa matriz precisa ter o mesmo número de colunas e linhas

print(a)

input()