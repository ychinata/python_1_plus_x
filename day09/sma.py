
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 将字节转为字符串
    dmy = dmy.decode('utf-8')
    ymd = '-'.join(dmy.split('-')[::-1])
    return ymd


# 读取日期和收盘价
dates, closing_prices = np.loadtxt(
    './data/aapl.csv', delimiter=',', unpack=True, usecols=(1, 6), dtype='M8[D],f8', converters={1: dmy2ymd}
)
print(dates)
print(closing_prices)


# 定义函数计算N日移动平均值
def calc(n):
    # 初始化
    sma = np.zeros(dates.size - n + 1)
    for i in range(sma.size):
        # 通过切片从收盘价中进行截取
        cut_prices = closing_prices[i:i+n]
        # 计算平均值并赋值
        sma[i] = cut_prices.mean()
    return sma


# 调用函数计算5日移动平均值
sma5 = calc(5)
print(sma5)
# 通过卷积计算5日移动平均值
sma_conv5 = np.convolve(closing_prices, np.ones(5) / 5, 'valid')
print(sma_conv5)
# 调用函数计算10日移动平均值
sma10 = calc(10)
# 通过卷积计算10日移动平均值
sma_conv10 = np.convolve(closing_prices, np.ones(10) / 10, 'valid')
# 画布
mp.figure("SMA")
# 标题
mp.title("Simple Moving Average Line", fontsize=20)
# x轴
mp.xlabel('Date', fontsize=14)
# y轴
mp.ylabel('Price', fontsize=14)
# 获取当前坐标系
ax = mp.gca()
# 设置主刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
# 设置次要刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置主刻度显示样式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 将日期转换为matplotlib中的日期类型
dates = dates.astype(md.datetime.datetime)
# 绘制5日移动均线
mp.plot(dates[4:], sma5, color='red', label='sma5')
mp.plot(dates[4:], sma_conv5, color='limegreen', label='sma_conv5', linewidth=5, alpha=0.5)
# 绘制10日移动均线
mp.plot(dates[9:], sma10, color='dodgerblue', label='sma10')
mp.plot(dates[9:], sma_conv10, color='orangered', label='sma_conv10', linewidth=5, alpha=0.5)
# 绘制收盘价曲线
mp.plot(dates, closing_prices, color='lightgray', label='closing_prices')
# x坐标自动调整
mp.gcf().autofmt_xdate()
# 显示图例
mp.legend()
mp.show()
