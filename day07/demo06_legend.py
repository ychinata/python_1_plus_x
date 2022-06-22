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
mp.plot(x, sin_y, linestyle='--', linewidth=3, color='orangered', label='y=2sin(x)')
# mp.plot(x, sin_y, linestyle='--', linewidth=3, color=(1, 0, 0))
# mp.plot(x, sin_y, linestyle='--', linewidth=3, color='#00ff00')
mp.plot(x, cos_y, linestyle='-.', linewidth=1, color='dodgerblue', label=r'$y=\frac{cos(x)}{2}$')
# 限制x坐标范围
mp.xlim(x.min() * 1.2, x.max() * 1.2)
# 通过如下方式单独设置左和右
# mp.xlim(right=20)
# mp.xlim(left=-20)
# 限制y坐标范围，可以通过top和bottom进行限制
mp.ylim(sin_y.min() * 1.2, sin_y.max() * 1.2)
# 设置x轴刻度，以pi为单位
mp.xticks([-np.pi, -np.pi/2, 0, np.pi/2, 3*np.pi / 4, np.pi],
          [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\frac{3}{4}\pi$', r'$\pi$'])
# 设置y轴刻度
mp.yticks([-2, -1, 1, 2])

# 获取当前坐标系
ax = mp.gca()
# 底部坐标轴
# set_position，设置坐标轴位置，axes(按比例0-1)，data(按数据)
ax.spines['bottom'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('axes', 0.8))
ax.spines['left'].set_position(('data', 0))
# set_color：设置坐标轴颜色，none表示不可见
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# 设置下面和左边坐标轴的颜色
ax.spines['bottom'].set_color('purple')
ax.spines['left'].set_color('darkgreen')
# 显示图例
mp.legend(loc='upper left')
# 显示图形
mp.show()
