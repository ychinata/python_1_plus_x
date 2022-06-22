import matplotlib.pyplot as mp
import numpy as np

# 2022.6.21

#  创建Figure One
mp.figure("Figure One", figsize=(8, 6), facecolor='lightgray', dpi=200)
# 标题
mp.title("Figure One", fontsize=20)
# x轴标签
mp.xlabel("x", fontsize=14)
# y轴标签
mp.ylabel("y", fontsize=14)
# 刻度参数
mp.tick_params(labelsize=10)
# 网格线
mp.grid(linestyle=':')
# 创建Figure Two
mp.figure("Figure Two", figsize=(8,  6), facecolor='lightgray', dpi=120)
# 标题
mp.title("Figure Two", fontsize=20)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 选中Figure one
mp.figure('Figure One')
x = np.linspace(-np.pi, np.pi, 1000)
sin_y = np.sin(x)
cos_y = np.cos(x) / 2
# 绘制正弦曲线
mp.plot(x, sin_y, color='blueviolet')
# 选中Figure Two
mp.figure('Figure Two')
# 绘制余弦曲线
mp.plot(x, cos_y, color='seagreen')
mp.show()
