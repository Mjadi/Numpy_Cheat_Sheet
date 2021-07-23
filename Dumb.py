# import numpy as np

# *Basic data type changing

# x = [2.1, 3.4, 9.8]

# E_1 = np.array(x, dtype='i')
# print(E_1)
# print(E_1.dtype)

# *Changing datatype of an existing array

# z = np.array([4.2, 8.7])

# z_2 = z.astype('S')

# print(z)
# print(z_2)
# print(z_2.dtype)

# *Changing existing array to bool term

# s = np.array([1, 0, 2])

# s_2 = s.astype(bool)

# print(s)
# print(s_2)
# print(s_2.dtype)

# *Making a copy of an array

# arr = np.array([2, 5, 8])

# New_arr = arr.copy()
# New_arr[1] = 69

# print(arr)
# print(New_arr)

# *Making changes to the original array

# arr = np.array([2, 5, 8])

# New_arr = arr.view()
# New_arr[1] = 69

# print(arr)
# print(New_arr)

# *Making a check if the data in an array is original or not

# arr = np.array([2, 5, 8])

# New_arr = arr.view()
# New_arr_2 = arr.copy()

# print(New_arr.base)
# print(New_arr_2.base)

# *Checking shapes and dimensions of an array

# j = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], ndmin=5)

# print(j)
# print(j.shape)

# *reshaping an array to 2D

# r = np.array([1, 2, 3, 4, 5, 6])
# r_2 = r.reshape(3, 2)

# print(r)
# print(r_2)

# *reshaping an array to 3D

# q = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# q_2 = q.reshape(2, 3, 2)

# print(q)
# print(q_2)

# *Iterating arrays

# g = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for item in g:
#     for item2 in item:
#         print(item2)

# *Use of nditer method

# g = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])

# for x in np.nditer(g):
#     print(x)

# *Changing data_type of an iterating array

# v = np.array([0, 1, 0])

# for item in np.nditer(v, flags=["buffered"], op_dtypes=["S"]):
#     print(item)

# *iterating through conditions

# l = np.array([[2, 4, 6, 8], [10, 12, 14, 16]])

# for item in np.nditer(l[0:2, ::2]):
#     print(item)

# *enumaring and iterating a multidimenstional array

# t = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9,10]])

# for index_no, item in np.ndenumerate(t):
#     print(index_no, item)

# *Use of concatenate method in numpy

# r = np.array([1, 2, 3])
# r_1 = np.array([4, 5, 6])

# r_2 = np.concatenate((r, r_1))
# print(r_2)

# *Use of the stack method

# c = np.array([1, 2, 3])
# c_1 = np.array([4, 5, 6])

# arr = np.stack((c, c_1), axis=1)
# print(arr)

# *Normal Split function

# text = "Hi Pc"
# text = text.split() 
# print(text)

# *Split method in numpy

# o = np.array(["Nope", "Ya"])
# print(np.array_split(o, 2))

# *Splitting with axis

# f = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],])

# print(np.hsplit(f, 3))

# Searching data in an array

# p = np.array([2, 5, 3, 4, 9, 7])

# p_1 = np.where(p == 3)

# print(p_1)

# *Taking input as a list with the help of for loop

# a = int(input())

# m = []

# for i in range(0, a):
# 	b = input()
# 	m.append(b)

# print(m[-1] + " big")
# print(m[0] + " small")

# *testing the where method

# z = np.array([3, 5, 2, 6, 9])

# z_1 = np.where(z%2==0)
# print(z_1)

# *Making a binary search for data

# u = np.array([1, 4, 6, 8])

# u_1 = np.searchsorted(u, 4, side='right')
# print(u_1)

# *Search where data val should be inserted

# d = np.array([1, 4, 6, 8])

# d_1 = np.searchsorted(d, [2, 5, 7])
# print(d_1)

# *Sorting Data in arrays

# y = np.array([[2, 1, 9], [3, 8, 6]])

# y_1 = np.sort(y)
# print(y_1)

# *It also sets data alphabetically

# *Here is the bool val

# j = np.array([True, False, False, True])

# j_1 = np.sort(j)
# print(j_1)

# *Using Filter 

# d = np.array([23, 56, 78, 96])
# d_1 = [False, True, True, False]

# d_2 = d[d_1]
# print(d_2)

# *Doing filtering per codition

# arr = np.array([1, 2, 3, 4, 7])

# fil_arr = []

# for data in arr:
    
#     if data <= 3:
#         fil_arr.append(True)

#     elif data > 3:
#         fil_arr.append(False)

# new_arr = arr[fil_arr]
# print(arr)
# print(new_arr)

# *Example 2

# arr = np.array([67, 24, 96, 81, 45])

# arr_2 = []

# for data in arr:
#     if data%2==0:
#         arr_2.append(True)

#     else:
#         arr_2.append(False)

# new_arr = arr[arr_2]

# print(arr, new_arr)

# *Shortcutting the process

# d = np.array([67, 24, 96, 81, 45])

# fil_d = d%2==0

# new_d = d[fil_d]
# print(d, new_d)

# *Task Over





