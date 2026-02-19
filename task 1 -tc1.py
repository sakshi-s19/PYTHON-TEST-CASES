import numpy as np

# ----------------------
# Test Case 1
# ----------------------

print("Test Case 1")

# Create 3x3 array
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print("Original 3x3 Array:")
print(arr)

# Reshape to (1,9)
reshaped_arr = arr.reshape(1,9)

print("Reshaped Array (1x9):")
print(reshaped_arr)


# ----------------------
# Test Case 2
# ----------------------

print("\nTest Case 2")

# Create two 1D arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

# Element-wise multiplication
result = a * b

print("Array 1:", a)
print("Array 2:", b)
print("Element-wise Multiplication:", result)