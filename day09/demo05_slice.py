import numpy as np
# reviewed:2022.9.29

a = np.arange(10)
print(a)
print(a[:7:1])
print(a[:7])
print(a[2::2])
print(a[:1:-1])
# 二维数组切片
b = np.arange(24).reshape(6, 4)
print(b)
print(b[1::2, ::-2])
print(b[[1, 2, 4], ::2])
