
import numpy as np

a = np.arange(12)
print(a)
# 视图变维
b = a.reshape(3, 4)
print(b)
# 以下2行代码会报错，元素个数不匹配
# b = a.reshape(3, 5)
# print(b)
c = b.ravel()
print(c)
# 复制变维
d = b.flatten()
print(d)
# 验证数据有没有复制
a += 10
print("***************")
print(a, b, c, d, sep='\n')
# 就地变维
b.shape = (12,)
print(b)
