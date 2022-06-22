import matplotlib.pyplot as mp
import numpy as np

# 2022.6.21

# 在-pi和pi之间生成1000个点，它们之间是等差的
x = np.linspace(-np.pi, np.pi, 1000)
# print(x)
sin_y = np.sin(x) * 2
cos_y = np.cos(x) / 2
# 绘制折线图
# linestyle：线型，实线-，虚线--,虚点线-.,点线:
mp.plot(x, sin_y, linestyle='--', linewidth=3, color='orangered')
# mp.plot(x, sin_y, linestyle='--', linewidth=3, color=(1, 0, 0))
# mp.plot(x, sin_y, linestyle='--', linewidth=3, color='#00ff00')
mp.plot(x, cos_y, linestyle='-.', linewidth=1, color='dodgerblue')
# 显示图形
mp.show()
