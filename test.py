
# Exercices 1
import numpy as np
# 


data1 = np.arange(10)
data2 = data1[0:9:1].reshape(3,3)

data3 = np.arange(10,18).reshape(2,2,2)


data2[:] += 5

print(data2)

























