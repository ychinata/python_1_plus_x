import matplotlib.pyplot as mp

# 2022.6.23

# 值
values = [15, 23, 18, 12, 20]
# 间隙
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
# 标签
labels = ['C++', 'Python', 'Java', 'PHP', 'C']
# 颜色
colors = ['lightgreen', 'cyan', 'dodgerblue', 'deeppink', 'violet']
# 绘制饼图
# mp.pie(x=values, explode=spaces, labels=labels, colors=colors, autopct='%d%%', shadow=False)
# 绘制饼图，保留原值
total_values = sum(values)
mp.pie(x=values, explode=spaces, labels=labels, colors=colors, autopct=lambda x: round(x/100*total_values),
       shadow=True)
mp.show()
