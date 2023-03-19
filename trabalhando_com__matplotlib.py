import matplotlib.pyplot as plt
import numpy as np

#x = [1,2,3,4,5,6,7,8,9,10]
#y = [1,2,3,4,5,6,7,8,9,10]

#plt.scatter(x,y)

x1 = np.arange(0,1000,1)
# Usando o arrange, posso evitar escrever todos os dados manualmente.

plt.plot(x1, x1**2)
plt.show()

