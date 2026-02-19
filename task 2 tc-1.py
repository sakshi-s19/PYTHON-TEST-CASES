import numpy as np

print("Test Case 1 - Matrix Multiplication")

# Define two 2x2 matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
result = np.matmul(A, B)

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Multiplication Result:")
print(result)