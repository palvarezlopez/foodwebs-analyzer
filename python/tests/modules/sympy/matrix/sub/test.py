import sympy as sp

# declare two matrices
A = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = sp.Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# print sum
print("Original A, B:")
sp.pprint(A)
sp.pprint(B)
print("A-B:")
sp.pprint(A - B)

# declare symbolic matrix
X = sp.MatrixSymbol('X', 3, 3)
Y = sp.MatrixSymbol('Y', 3, 3)

# subs
C = X-Y

# print symbolic sub
print("Original X, Y:")
sp.pprint(X)
sp.pprint(Y)
print("X-Y:")
sp.pprint(C)

# subs values
C = C.subs({X: A, Y:B})

# print
print("X(A)-Y(B):")
sp.pprint(C)

