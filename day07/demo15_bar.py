"""
绘制橘子和苹果的销量条形图
2022.6.23
"""

import numpy as np
import matplotlib.pyplot as mp
import random

# 从15到40之间随机生成12个整数
oranges = [random.randint(15, 40) for i in range(12)]
print(oranges)
apples = [random.randint(15, 40) for i in range(12)]
print(apples)
# 画布
mp.figure("Sales")
# 标题
mp.title("Sales", fontsize=20)
# x轴标签
mp.xlabel("Month", fontsize=14)
# y轴标签
mp.ylabel("Mount", fontsize=14)
# x坐标
x = list(range(12))
# 绘制橘子条形图
mp.bar(x, oranges, 0.4, color='red', edgecolor='black', label='Orange')
# 绘制苹果销量条形图
x1 = [i+0.3 for i in x]
mp.bar(x1, apples, 0.4, color='dodgerblue', edgecolor='black', label='Apple', alpha=0.7)
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
