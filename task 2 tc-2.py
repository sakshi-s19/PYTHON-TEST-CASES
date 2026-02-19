import numpy as np

print("Test Case 2 - Transpose and Dot Product")

# Define 3x2 matrix
C = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print("Original Matrix (3x2):")
print(C)

# Transpose
C_transpose = C.T

print("Transpose (2x3):")
print(C_transpose)

# Define another 3x2 matrix
D = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Dot product
result = np.dot(C_transpose, D)

print("Dot Product Result:")
print(result)