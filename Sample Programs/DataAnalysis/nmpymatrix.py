import numpy as np

First_Matrix = np.arange(30).reshape(5, 6)

print(First_Matrix)
print(First_Matrix.shape)
print(format(First_Matrix.resize))
print(format(First_Matrix.max(axis = 1)))
print(format(First_Matrix.sum(axis = 1)))
print(format(First_Matrix.sum(axis = 0)))
first_list = [1 , 2, 3]
second_list = [11 , 22, 33]
print(First_Matrix)

print(np.array(second_list)/np.array(first_list))
#print(np.identity(3))

a = np.ones((4, 4), dtype=float)
#print(a)
