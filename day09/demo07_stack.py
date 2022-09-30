import numpy as np
# reviewed:2022.9.29

a = np.ones((3, 4))
print(a)
b = a + 10
print(b)
# 垂直组合
c = np.vstack((a, b))
print(c)
d = np.concatenate((a, b), axis=0)
print(d)
# 垂直拆分
print("垂直拆分".center(50, '*'))
# 不能拆成4行
e1, e2, e3 = np.vsplit(d, 3)
print(e1, e2, e3, sep='\n')
f1, f2, f3 = np.split(d, 3, axis=0)
print(f1, f2, f3, sep='\n')
# 水平组合
print("水平组合".center(50, '*'))
g = np.hstack((a, b))
print(g)
h = np.concatenate((a, b), axis=1)
print(h)
# 水平拆分
i1, i2 = np.hsplit(h, 2)
print(i1, i2, sep='\n')
j1, j2 = np.split(h, 2, axis=1)
print(j1, j2, sep='\n')

