
import numpy as np

# 创建数组[2, 3, 4]
a = np.arange(24).reshape(2, 3, 4)
print(a)
# 创建数组[4]
b = np.array([1, 2, 3, 1])
print(b)
print(a + b)
# 创建数组[3, 4]
c = np.arange(12).reshape(3, 4)
print(c)
print(a + c)
# 创建数组[2, 1, 4]
d = np.arange(8).reshape(2, 1, 4)
print(d)
print(a + d)
# 创建数组[2]
e = np.array([1, 2])
print(e)
print(a + e)
