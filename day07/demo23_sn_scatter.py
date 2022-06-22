
"""绘制房屋大小与价格散点图"""
import seaborn as sn
import matplotlib.pyplot as mp

mp.rcParams['font.sans-serif'] = ['SimHei']

with open('../data/house1.csv', encoding='utf-8') as f:
    sizes, prices, floors = [], [], []
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 大小
        size = float(line_split[1])
        # 价格
        price = float(line_split[0])
        # 电梯
        floor = line_split[4]
        sizes.append(size)
        prices.append(price)
        floors.append(floor)
_, ax1 = mp.subplots(1, 1, figsize=(15, 10))
# 绘制散点图
# sn.scatterplot(x=sizes, y=prices, ax=ax1)
# 按电梯分组
# sn.scatterplot(x=sizes, y=prices, ax=ax1, hue=floors)
# 设置hue、style、size
sn.scatterplot(x=sizes, y=prices, hue=floors, ax=ax1, style=floors, size=floors, palette='Set1')
mp.show()

