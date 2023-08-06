#10. Write a program to Multiply Two matrices

import numpy as np

mat1 = np.array([[1,2,3],[4,5,6]])
mat2 = np.array([[7,8],[9,1],[2,3]])

print(f'Elements of A ::\n {mat1}')
print(f'Elements of B ::\n {mat2}')

res = np.dot(mat1,mat2)

print(f"Multiplication of two matrics is :\n {res}")