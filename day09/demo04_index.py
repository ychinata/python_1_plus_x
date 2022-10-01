import numpy as np
# reviewed:2022.9.29

# 一维数组的索引
a = np.arange(10)
print(a)
print(a[1])
print(a[-2])
# 二维数组的索引
b = np.arange(24).reshape(6, 4)
print(b)
print(b[2, -1])
# 布尔索引
bool_index = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
print(bool_index)
print(b[bool_index])
# 花式索引
print("花式索引".center(50, '*'))
print(b)
# 索引是一维的
print(b[[1, 3]])
# 索引数组是多维数组
mut_index = np.array([[1, 2], [3, 4]])
print(b[mut_index])
# 索引是多个数组
print(b[[0, 1], [1, 2]])
