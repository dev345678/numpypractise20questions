# practise questions of numpy (20 questions):

import numpy as np

# 1. Create a 1D NumPy array from a list of numbers [10, 20, 30, 40, 50]
arr1 = np.array([10, 20, 30, 40, 50])

# 2. Create a 3x3 matrix with all elements as zero
zeros_matrix = np.zeros((3, 3))

# 3. Create a 5x5 identity matrix
identity_matrix = np.eye(5)

# 4. Create an array with values from 0 to 50 with a step of 5
step_array = np.arange(0, 51, 5)

# 5. Create a 3x3 matrix filled with random integers between 10 and 100
random_int_matrix = np.random.randint(10, 101, size=(3, 3))

# 6. Find the shape, size, and datatype of a given NumPy array
a = np.array([[1, 2, 3], [4, 5, 6]])
shape = a.shape
size = a.size
dtype = a.dtype

# 7. Convert a Python list [[1,2,3],[4,5,6]] to a NumPy array
list_to_array = np.array([[1, 2, 3], [4, 5, 6]])

# 8. Reshape a 1D array of size 12 into a 3x4 matrix
arr2 = np.arange(12)
reshaped_array = arr2.reshape(3, 4)

# 9. Flatten a 2D matrix [[1, 2], [3, 4]] into a 1D array
matrix = np.array([[1, 2], [3, 4]])
flattened_array = matrix.flatten()

# 10. Reverse the order of elements in a 1D NumPy array
arr3 = np.array([1, 2, 3, 4, 5])
reversed_array = arr3[::-1]

# 11. Replace all odd numbers in an array with -1
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])
arr4[arr4 % 2 == 1] = -1

# 12. Find the mean, median, and standard deviation of an array
arr5 = np.array([10, 20, 30, 40, 50])
mean = np.mean(arr5)
median = np.median(arr5)
std_dev = np.std(arr5)

# 13. Sort a NumPy array in ascending and descending order
arr6 = np.array([3, 1, 5, 2, 4])
asc_sorted = np.sort(arr6)
desc_sorted = np.sort(arr6)[::-1]

# 14. Create two arrays and perform element-wise addition, subtraction, multiplication, and division
arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])
add = arr7 + arr8
sub = arr7 - arr8
mul = arr7 * arr8
div = arr7 / arr8

# 15. Extract all even numbers from a given NumPy array
arr9 = np.array([1, 2, 3, 4, 5, 6])
even_numbers = arr9[arr9 % 2 == 0]

# 16. Count the number of NaN values in an array
arr10 = np.array([1, np.nan, 2, np.nan, 3])
nan_count = np.isnan(arr10).sum()

# 17. Replace NaN values with the mean of the array
mean_val = np.nanmean(arr10)
arr10[np.isnan(arr10)] = mean_val

# 18. Split a 1D array of size 12 into 4 equal parts
arr11 = np.arange(12)
split_arr = np.split(arr11, 4)

# 19. Stack two arrays vertically and horizontally
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
vert_stack = np.vstack((a1, a2))
horiz_stack = np.hstack((a1, a2))

# 20. Generate a 5x5 matrix of random floats and round it to 2 decimal places
rand_float_matrix = np.random.rand(5, 5)
rounded_matrix = np.round(rand_float_matrix, 2)
