import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
# reviewed:2022.9.29


def dmy2ymd(dmy):
    # 将字节转换为字符串
    dmy = dmy.decode('utf-8')
    # 将日-月-年转换为年-月-日
    ymd = '-'.join(dmy.split('-')[::-1])
    return ymd


# 读取数据
dates, opening_prices, hightest_prices, lowest_prices, closing_prices = np.loadtxt(
    './data/aapl.csv', dtype='M8[D],f8,f8,f8,f8', delimiter=',', usecols=(1, 3, 4, 5, 6),
    unpack=True, converters={1: dmy2ymd})
print(dates)
print(opening_prices)
print(hightest_prices)
print(lowest_prices)
print(closing_prices)

# 创建画布
mp.figure("Candlestick")
# 标题
mp.title("Candlestick", fontsize=20)
# x轴标签
mp.xlabel("Date", fontsize=14)
# y轴标签
mp.ylabel("Price", fontsize=14)
# 获取当前坐标系
ax = mp.gca()
# 设置x轴主要刻度为每周一
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
# 设置x轴次要刻度为每天
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置x轴主刻度显示样式为'%d %b %Y'
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 网格线型为点线
mp.grid(linestyle=':')
# 将日期转换为matplotlib中的日期类型
dates = dates.astype(md.datetime.datetime)
# 阳线掩码
rise = closing_prices - opening_prices > 0
print(rise)
# 阴线掩码
fall = closing_prices - opening_prices < 0
# 初始化填充色,3f4代表一维，3个元素的数组，每个元素是f4类型
fc = np.zeros(dates.size, dtype='3f4')
# 阳线填充色白色
fc[rise] = [1, 1, 1]
# 阴线填充色绿色
fc[fall] = [0, 0.5, 0]
print(fc)
# 初始化边缘色
ec = np.zeros(dates.size, dtype='3f4')
# 阳线边缘色红色
ec[rise] = [1, 0, 0]
# 阴线边缘色为绿色
ec[fall] = [0, 0.5, 0]
# 绘制引线,条的高度为最高价-最低价，宽度0，从最低价开始画
mp.bar(dates, hightest_prices - lowest_prices, 0, lowest_prices, color=fc, edgecolor=ec)
# 绘制实体，条的高度为收盘价-开盘价，宽度0.6，从开盘价开始画
mp.bar(dates, closing_prices - opening_prices, 0.6, opening_prices, color=fc, edgecolor=ec)
# 自动调整x轴坐标样式
mp.gcf().autofmt_xdate()
# 显示图形
mp.show()
