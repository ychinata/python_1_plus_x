import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure("Grid")
gs = mg.GridSpec(3, 3)
# 画第一个子图
mp.subplot(gs[:-1, 0])
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个1
mp.text(0.5, 0.5, '1', va='center', ha='center', fontsize=36)

# 画第二个子图
mp.subplot(gs[-1, :-1])
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个2
mp.text(0.5, 0.5, '2', va='center', ha='center', fontsize=36)

# 画第三个子图
mp.subplot(gs[1:, -1])
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个3
mp.text(0.5, 0.5, '3', va='center', ha='center', fontsize=36)

# 画第四个子图
mp.subplot(gs[0, 1:])
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个4
mp.text(0.5, 0.5, '4', va='center', ha='center', fontsize=36)

# 画第五个子图
mp.subplot(gs[1, 1])
# 关闭刻度
mp.xticks(())
mp.yticks(())
# 写一个5
mp.text(0.5, 0.5, '5', va='center', ha='center', fontsize=36)

mp.show()
