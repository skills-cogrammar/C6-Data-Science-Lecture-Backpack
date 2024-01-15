import numpy as np
# lista=[2,4,5,6,8]

# # array function
# numpy_array = np.array(lista)
# print("array function:")
# print(numpy_array)

# # zeroes
# print("zeros function:")
# print(np.zeros(10))
# print(np.zeros((3, 4)))

# # arange
# print("arange function")
# print(np.arange(5))
# print(np.arange(1, 10, 2))

# # rand
# print("rand function")
# print(np.random.rand(10) * 100) # scalar multiplication

# # N-dimensions
# print("N-dimensions")
# print(np.array([
#                 [1,2,3],
#                 [4,5,6]
#               ]).ndim)


# # full function
# print("Full function")
# print(np.full((2,2,2), 5).ndim)

# # rand 2d
# print("rand 2d")
# print(np.random.rand(3,5) * 100)

# # empty
print("empty")
print(np.empty((2,2)))

# Data types
print(np.array([1.4,2.4,3.4,4.4,5.4], dtype='int32'))
print(np.array([1+2j, 2+2j]).dtype)
int_arr= np.array([1,2,3,4,5])
print(int_arr.astype('float')) 
