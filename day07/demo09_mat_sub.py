"""
子图，矩阵式布局
2022.6.21
"""
import matplotlib.pyplot as mp

mp.figure("Subplot")
# 子图221
mp.subplot(2, 2, 1)
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个1,va表示垂直居中，ha表示水平居中
mp.text(0.5, 0.5, '1', va='center', ha='center', fontsize=36)

# 子图222
mp.subplot(2, 2, 2)
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个2,va表示垂直居中，ha表示水平居中
mp.text(0.5, 0.5, '2', va='center', ha='center', fontsize=36)

# 子图223
mp.subplot(2, 2, 3)
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个3,va表示垂直居中，ha表示水平居中
mp.text(0.5, 0.5, '3', va='center', ha='center', fontsize=36)

# 子图224
mp.subplot(2, 2, 4)
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个4,va表示垂直居中，ha表示水平居中
mp.text(0.5, 0.5, '4', va='center', ha='center', fontsize=36)
mp.show()
