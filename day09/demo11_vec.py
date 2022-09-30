import numpy as np
# reviewed:2022.9.29

# 定义一个标量函数，计算和、差、积
def foo(x, y):
    return x + y, x - y, x * y


# 调用标量函数
res1, res2, res3 = foo(10, 2)
print(res1, res2, res3, sep='\n')
# 创建2个数组
a = np.array([1, 2, 5])
b = np.array([6, 7, 8])
# 将标量函数包装成矢量函数
bar = np.vectorize(foo)
print(bar)
# 调用矢量函数
res1, res2, res3 = bar(a, b)
print(res1, res2, res3, sep='\n')
