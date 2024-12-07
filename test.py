
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

print(data2)

























