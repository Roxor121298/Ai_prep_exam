
# Exercices 1
import numpy as np
# 
#
# Vos solutions ici
#
# Solution 1

sol1 = np.array([1, 2, 3, 4, 5])


# Solution 2

sol2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# Solution 3

rng = np.random.default_rng()
sol4 = rng.uniform(low=0, high=1, size=(10))

# Solution 4

sol4 = np.identity((5), dtype=np.uint16)


# Solution 5

sol5_meilleur = np.full((2,3,4), -1, dtype=np.int32)


sol5 = np.array([
                [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],
                [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
                ],dtype=np.int32)

# Solution 6

rng = np.random.default_rng()
sol6 = rng.choice([True,False], size=(10))

# Solution 7


# Solution 8 


sol8 = np.linspace(0., 1., 8)



sol4 = rng.uniform(low=0, high=1, size=(10,10))

sol9 = rng.uniform(low=-100.0, high=100.0, size=(10,2))



data1 = np.linspace(0, 10, 10, dtype=np.int32)
data2 = np.linspace(11,19,9).reshape(3,3)
data3 = np.full((4,4), 1)


a = data1[1]
b = data2[1,1]
c = data2[0,0]
d = data3[3,3]

a = b + c * d


sol1 = np.arange(10)

# Solution 2

sol2 = sol1 = np.arange(10)

# Solution 2

sol2 = np.arange(2, 22, 2)

def sumindice (i,j):
    return i+j

rng = np.random.default_rng()
sol7 = rng.random(size=(3,4))

sol7 = sol7.reshape(2,6)


sol7 = sol7.flatten()



sol8 = np.full((4,4), 1)

sol8 = sol8.flatten()

sol8 = sol8.reshape(2,8)

rng = np.random.default_rng()
sol9 = rng.uniform(low=10,high=100,size=(5,5))

sol9.astype(np.float32)

# Solution 10

# Créez un tableau 2D de 12 x 2 nombres réels aléatoires entre [0, 2[. 
# Le transformer en matrice 3 x 8, puis convertir les éléments en nombres entiers. 
# Finalement, le transformer en matrice 1D en valeurs booléennes.



sol10 = np.random.default_rng().uniform(low=0,high=2, size=(12,2))
sol10 = sol10.reshape(3,8)
sol10 = sol10.astype(np.int32)
sol10 = sol10.astype(np.bool_).flatten()


data = np.arange(3*3*3*3).reshape(3,3,3,3) 


rng = np.random.default_rng()

def prodmatrice(data1, data2):
    return data1 * data2

data1 = rng.uniform(low=-10, high=10,size=(12,2))
data2 = rng.random(size=(12,2))

data3 = data1 * data2


print(data2[:,-2:])


























