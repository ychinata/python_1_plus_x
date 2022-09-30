import numpy as np
# reviewed:2022.9.29

# arange创建
a = np.arange(10)
print(a)
print(type(a))
a = np.arange(10, 1, -0.5)
print(a)
# array创建
b = np.array([1, 2, 3, 4])
print(b)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
b = np.array([1, 0, 1], dtype=bool)
print(b)
# line space创建
c = np.linspace(1, 100, 100)
print(c)
c = np.linspace(1, 100, 100, dtype=int)
print(c)
# zeros创建
d = np.zeros((2, 3), dtype=int)
print(d)
# Ones创建
e = np.ones((3, 4), dtype=float)
print(e)
