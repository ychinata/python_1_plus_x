import numpy as np
import matplotlib.pyplot as mp

# 2022.6.23

n = 1000
# 得到xy坐标
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
# 得到z坐标
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# 画布
mp.figure("Contour")
mp.title("Contour", fontsize=20)
# x和y轴标签
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 等高线填充区，20阶
mp.contourf(x, y, z, 20, cmap='jet')
# 等高线，20阶，颜色黑色，线宽0.5
contr = mp.contour(x, y, z, 20, colors='black', linewidth=0.5)
# 为等高线添加标签，inline_spacing表示断头线宽度,fmt为格式
mp.clabel(contr, inline_spacing=0.6, fmt='%.1f', fontsize=8)
mp.show()
