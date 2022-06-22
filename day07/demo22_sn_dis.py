
import seaborn as sn
import matplotlib.pyplot as mp

mp.rcParams['font.sans-serif'] = ['SimHei']

with open('../data/house1.csv', encoding='utf-8') as f:
    sizes = []
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        size = float(line_split[1])
        sizes.append(size)
# 最大
max_size = max(sizes)
bins = [0, 50, 75, 100, 125, 150, 200, max_size]

# 子图
_, ax1 = mp.subplots(1, 1, figsize=(15, 10))
# 绘制直方图
# sn.distplot(sizes, ax=ax1)
# sn.distplot(sizes, ax=ax1, kde=False)
# 设置bins
# sn.distplot(sizes, ax=ax1, bins=bins)
sn.distplot(sizes, ax=ax1, bins=bins, kde_kws={"linewidth": 2, "color": 'red'},
            hist_kws={"color": "blue", "edgecolor": "black"})
mp.show()
