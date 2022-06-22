import numpy as np
import matplotlib.pyplot as mp

# 2022.6.21

# 定义变量
n = 1000
# x坐标,服从标准正态分布，平均值为0，标准差为1，n个数据
x = np.random.normal(0, 1, n)
# y也是服从标准正态分布
y = np.random.normal(0, 1, n)
# 计算每个点到原点的距离
d = np.sqrt(x ** 2 + y ** 2)
# 画布
mp.figure("Scatter")
mp.title("Scatter", fontsize=20)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 颜色映射,d按照从小到大排序，jet_r是从深红到深蓝，最小值就是深红，最大值就是深蓝，中间的就根据它的大小
# 映射到深红和深蓝之间
mp.scatter(x, y, s=30/d, c=d, cmap='jet_r')
mp.show()
