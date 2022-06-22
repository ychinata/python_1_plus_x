import numpy as np
import matplotlib.pyplot as mp

# 2022.6.21

# x坐标
x = np.linspace(0, 8*np.pi, 1000)
# y坐标
sin_y = np.sin(x)
cos_y = np.cos(x/2) / 2
# 画布
mp.figure("Fill")
# 标题
mp.title("Fill", fontsize=20)
# x和y轴标签
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
# 刻度参数
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制正弦和余弦曲线
mp.plot(x, sin_y, color='dodgerblue')
mp.plot(x, cos_y, color='orangered')
# 填充
mp.fill_between(x, sin_y, cos_y, sin_y > cos_y, color='red')
mp.fill_between(x, sin_y, cos_y, sin_y < cos_y, color='blue', alpha=0.4)
mp.show()
