import numpy as np
# reviewed:2022.9.29

# 布尔型
a = np.array([1, 0], dtype=np.bool_)
print(a)
a = np.array([1, 0], dtype='?')
print(a)
# int8
b = np.array([1.5, 2.0], dtype='b')
print(b)
print(b.dtype)
# uint型
c = np.array([1, 2, 3], dtype='u2')
print(c)
print(c.dtype)
# 字符串
d = np.array(['a', 'bbb', 'cccc'], dtype='U4')
print(d)
print(d.dtype)
# 日期类型
e = np.array(['2022-01-01', '2020-02-05'], dtype='M8[s]')
print(e)
