import matplotlib.pyplot as mp

# 2022.6.21

mp.figure("Axes")
# 第一张子图左、底、宽、高
mp.axes([0.1, 0.1, 0.8, 0.8])
mp.text(0.5, 0.5, '1', va='center', ha='center', fontsize=36)
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 第2张子图
mp.axes([0.6, 0.2, 0.2, 0.2])
mp.text(0.5, 0.5, '2', va='center', ha='center', fontsize=36)
# 关闭刻度
mp.xticks(())
mp.yticks(())
mp.show()
