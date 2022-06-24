"""
绘制价格5日/10日移动均值/指数均值折线图
Author: 黄晓宇
东莞职业技术学院
Date: 2022.6.24
"""

import matplotlib.pyplot as mp
import matplotlib.dates as md
import numpy as np
import math

# 读取数据
with open('data/aapl.csv') as f:
    dates, closing_prices = [], []
    for line in f:
        line_split = line.strip().split(',')
        # print(line_split)
        # 日期
        date = line_split[1]
        # 收盘价
        closing_price = float(line_split[-2])
        dates.append(date)
        closing_prices.append(closing_price)
# print(dates)
# print(len(closing_prices))
# 处理日期
# 按-分割
dates = [d.split('-') for d in dates]
# 倒转顺序
dates = [[int(d[2]), int(d[1]), int(d[0])] for d in dates]
dates = [md.datetime.datetime(*d) for d in dates]
print(dates)


# 计算移动平均值
def calc_sma(n, closing_prices):
    # 初始化移动平均值空列表
    sma = []
    for i in range(len(closing_prices) - n + 1):
        # 从收盘价中切片得到数据
        cut_prices = closing_prices[i: i + n]
        mean_price = round(sum(cut_prices) / len(cut_prices), 2)
        # 追加到sma中
        sma.append(mean_price)
    return sma


# 计算指数平均值
def calc_ema(n, closing_prices):
    # 初始化移动平均值空列表
    ema = []
    for i in range(len(closing_prices) - n + 1):
        # 从收盘价中切片得到数据
        cut_prices = closing_prices[i: i + n]
        # TODO...计算指数移动平均值
        # 权重数组，使用math.exp([列表])，列表为-1到0之间生成N个等差的点，点间距为（N-1）
        # 例如5个数，则权重为[math.exp(-1),...,math.exp(0)]
        x = np.linspace(-1, 0, n)
        weight = []
        for j in range(len(x)):
            weight.append(math.exp(x[j]))
        # TODO
        # 计算加权平均值，公式为:(值*权重)之和/权重之和
        # 计算这几个数据的平均值
        cut_prices = np.array(cut_prices)
        weight = np.array(weight)
        # exp_mean_price = sum(cut_prices*weight)
        exp_mean_price = round(sum(cut_prices*weight) / sum(weight), 2)
        # 追加到ema中
        ema.append(exp_mean_price)
    return ema


# 5日移动均线
sma5 = calc_sma(5, closing_prices)
print(sma5)
# 10日移动均线
sma10 = calc_sma(10, closing_prices)
# 5日指数均线
ema5 = calc_ema(5, closing_prices)
# 10日指数均线
ema10 = calc_ema(10, closing_prices)

# 画布
mp.figure('Simple Moving Average')
# 标题
mp.title('Simple Moving Average', fontsize=20)
# x轴
mp.xlabel("Date", fontsize=14)
# y轴
mp.ylabel('Price', fontsize=14)
# 获取当前坐标系
ax = mp.gca()
# 设置x轴主刻度为每个星期一
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
# x轴次要刻度为每一天
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置x主刻度显示样式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))

mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 绘制收盘价
mp.plot(dates, closing_prices, color='lightgray', label='Closing Price')
# 绘制5日移动均线
mp.plot(dates[4:], sma5, color='orangered', label='SMA-5')
# 绘制10日移动均线
mp.plot(dates[9:], sma10, color='dodgerblue', label='SMA-10')
# 绘制5日指数均线
mp.plot(dates[4:], ema5, color='green', label='EMA-5')
# 绘制10日移动均线
mp.plot(dates[9:], ema10, color='magenta', label='EMA-10')
# 自动调整水平坐标轴的日期标签
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
