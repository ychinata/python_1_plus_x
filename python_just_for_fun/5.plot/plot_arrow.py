import numpy as np
import matplotlib.pyplot as plt
#pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

# 2022.11.29

fig = plt.figure()
ax = plt.axes()

ax.set_xlabel('a')
ax.set_xlim(-1, 1)
ax.set_ylabel('b')
ax.set_ylim(-1, 1)

# A=j, (0,0)->(0,1)
ax.arrow(0, 0, 0, 1, length_includes_head=False, head_width=0.05, fc='b', ec='k')
# A=1
ax.arrow(0, 0, 1, 0, length_includes_head=False, head_width=0.05, fc='b', ec='k')
# A=-1
ax.arrow(0, 0, -1, 0, length_includes_head=False, head_width=0.05, fc='b', ec='k')
# A=-j
ax.arrow(0, 0, 0, -1, length_includes_head=False, head_width=0.05, fc='b', ec='k')
# A=1+j
ax.arrow(0, 0, 1, 1, length_includes_head=False, head_width=0.05, fc='b', ec='k')

# 横纵坐标等比例
plt.axis('equal')
# ax.grid()
plt.show()
