# -*-coding:utf-8-*-

import seaborn as sn
import matplotlib.pyplot as mp

mp.rcParams['font.sans-serif'] = ['SimHei']
# 读取数据
with open('../data/house.csv') as f:
    districts, prices, floors = [], [], []
    # 迭代读取ֵ
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 区域
        district = line_split[7]
        # 价格
        price = float(line_split[0])
        # 电梯
        floor = line_split[4]
        districts.append(district)
        prices.append(price)
        floors.append(floor)

_, [ax1, ax2] = mp.subplots(2, 1, figsize=(15, 10))
# 一、住房数量条形图
# sn.barplot(x=districts, y=prices, ax=ax1, estimator=len)
# sn.barplot(x=districts, y=prices, ax=ax1, estimator=len, palette='Set1')
sn.barplot(x=districts, y=prices, ax=ax1, estimator=len, palette='Set1', hue=floors)
ax1.set_title("住房数量条形图", fontsize=18)
ax1.set_xlabel("区域", fontsize=12)
ax1.set_ylabel("数量", fontsize=12)
# 二、住房均价条形图
# sn.barplot(x=districts, y=prices, ax=ax2)
# sn.barplot(x=districts, y=prices, ax=ax2, ci=None)
sn.barplot(x=districts, y=prices, ax=ax2, ci=None, hue=floors)

mp.show()
