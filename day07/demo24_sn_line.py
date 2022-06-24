"""
绘制每个区的均价折线图
2022.6.23
"""
import seaborn as sn
import matplotlib.pyplot as mp
import random

mp.rcParams['font.sans-serif'] = ['SimHei']
# 读取数据
with open('data/house1.csv', encoding='utf-8') as f:
    # 每个区房屋总价的字典
    price_dic = {}
    # 每个区房屋数量的字典
    num_dic = {}
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 区域
        district = line_split[7]
        # 价格
        price = float(line_split[0])
        if district not in price_dic.keys():
            # 初始化
            price_dic[district] = 0
            num_dic[district] = 0
        # 价格累加
        price_dic[district] += price
        # 次数加1
        num_dic[district] += 1
# 计算均价
avg_dic = {}
for d, t_p in price_dic.items():
    avg_dic[d] = round(t_p / num_dic[d], 2)
print(avg_dic)
# x
x = [avg[0] for avg in avg_dic.items()]
# y
y = [avg[1] for avg in avg_dic.items()]
# 随机生成用于分组的序列
hue = [random.choice(['有电梯', '无电梯']) for i in range(len(x))]

# 子图
_, ax1 = mp.subplots(1, 1, figsize=(15, 10))
# 绘制折线图
# sn.lineplot(x=x, y=y, ax=ax1)
sn.lineplot(x=x, y=y, ax=ax1, hue=hue, style=hue, markers=True, palette='Set1')
ax1.set_title("各区域房屋均价", fontsize=18)
ax1.set_xlabel("区域", fontsize=12)
ax1.set_ylabel("价格", fontsize=12)
mp.show()
