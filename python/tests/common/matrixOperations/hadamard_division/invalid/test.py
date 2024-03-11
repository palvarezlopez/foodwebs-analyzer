import sympy as sp
from common import matrixOperations as mo

# test
matrix1 = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
matrix2 = sp.Matrix(2, 2, [11, 12, 13, 14])

print("Original:")
sp.pprint(matrix1)
sp.pprint(matrix2)
print("Hadamard_division (error):")
sp.pprint(mo.hadamard_division(matrix1, matrix2))