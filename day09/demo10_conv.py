import numpy as np
# reviewed:2022.9.29

# 被卷积序列
a = np.array([1, 2, 3, 4, 5])
# 卷积核
b = np.array([6, 7, 8])
# 有效卷积
c1 = np.convolve(a, b, 'valid')
print(c1)
# 同维卷积
c2 = np.convolve(a, b, 'same')
print(c2)
# 完全卷积
c3 = np.convolve(a, b, 'full')
print(c3)

