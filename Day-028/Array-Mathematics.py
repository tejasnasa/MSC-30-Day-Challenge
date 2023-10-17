import numpy as np

N, M = map(int, input().split())
arr1 = np.array([input().split() for i in range(N)], int)
arr2 = np.array([input().split() for i in range(N)], int)

print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.floor_divide(arr1, arr2))
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))
