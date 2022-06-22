import numpy as np
import matplotlib.pyplot as mp

# 2022.6.21

# x坐标
x = np.linspace(-5,  5, 1000)
# y坐标
y = 8 * np.sinc(x)
# 画布
mp.figure("Grid")
# 标题
mp.title("Grid", fontsize=20)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
# 获取当前坐标系
ax = mp.gca()
# 设置x轴主刻度定位器为多点定位器,间隔为1
ax.xaxis.set_major_locator(mp.MultipleLocator())
# 设置x轴次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
# 设置y轴
ax.yaxis.set_major_locator(mp.MultipleLocator())
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.tick_params(labelsize=10)
# 设置主刻度网格
ax.grid(which='major', axis='both', linewidth=0.75, linestyle='-', color='orange')
# 设置次要刻度网格
ax.grid(which='minor', axis='both', linewidth=0.25, linestyle='-', color='orange')

mp.plot(x, y, color='blue', label='y=8sinc(x)')
mp.legend()
mp.show()
