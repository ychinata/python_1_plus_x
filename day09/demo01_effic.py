
"""
计算0-999999的平方与立方之和，比较Python和NumPy的代码简洁度和运行效率
"""
import time
import numpy as np
# reviewed:2022.9.29

n = 999999
# 开始时间
start = time.time()
A, B = [], []
for i in range(n):
    A.append(i ** 2)
    B.append(i ** 3)
C = []
# 联合遍历
for a, b in zip(A, B):
    C.append(a + b)
# print(C)
# 结束时间
end = time.time()
print("Python所花的时间为:%s" % (end - start))
start = time.time()
A, B = np.arange(n) ** 2, np.arange(n) ** 3
C = A + B
end = time.time()
print("NumPy所花的时间为:%s" % (end - start))
# print(C)

# Python所花的时间为:1.2234580516815186
# NumPy所花的时间为:0.05197596549987793
