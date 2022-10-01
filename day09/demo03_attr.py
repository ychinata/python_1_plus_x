import numpy as np
# reviewed:2022.9.29

# 创建数组
a = np.arange(12)
print(a)
# 维度
print(a.shape)
# 维数
print(a.ndim)
# 改变维度
b = a.reshape(3, 4)
print(b)
print(b.shape)
print(b.ndim)
# dtype
print(b.dtype)
# size
print(b.size)
# 转置T
print(b.T)
# tolist()
print(b.tolist())
