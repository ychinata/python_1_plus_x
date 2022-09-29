
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = dmy.decode('utf-8')
    ymd = '-'.join(dmy.split('-')[::-1])
    return ymd


dates, opening_prices, hightest_prices, lowest_prices, closing_prices = np.loadtxt(
    './data/bhp.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), dtype='M8[D],f8,f8,f8,f8', unpack=True, converters={1: dmy2ymd}
)
# 日期取除了第一天的
dates = dates[1:]
# 开盘价、最高价、最低价取除了最后一天的
opening_prices = opening_prices[:-1]
hightest_prices = hightest_prices[:-1]
lowest_prices = lowest_prices[:-1]
# 收盘价取除了第一天的
closing_prices = closing_prices[1:]


# 定义标量函数计算一天的收益，当价格达到开盘价的0.99倍的时候买入，第二天收盘卖出
def profit(open_price, high_price, low_price, close_price):
    # 买入价格
    buying_price = open_price * 0.99
    # 判断买入价格在当天存在
    if low_price <= buying_price <= high_price:
        # 计算收益率并返回
        return (close_price - buying_price) * 100 / buying_price
    # 否则返回nan
    return np.nan


# 将标量函数封装成矢量函数，求整体的收益率
profits = np.vectorize(profit)(opening_prices, hightest_prices, lowest_prices, closing_prices)
print(profits)
# 得到收益率是nan的布尔型数组
nan = np.isnan(profits)
print(nan)
# 通过对nan取反得到有效收益率以及日期
profits = profits[~nan]
dates = dates[~nan]
print(profits)
# 得到盈利的日期及收益率
gain_dates = dates[profits > 0]
gain_profits = profits[profits > 0]
# 得到亏损的日期及收益率
loss_dates = dates[profits < 0]
loss_profits = profits[profits < 0]
# 画布
mp.figure('Trading Simulation')
# 标题
mp.title("Trading Simulation", fontsize=20)
# x轴标签
mp.xlabel('Date', fontsize=14)
# y轴标签
mp.ylabel('Profit', fontsize=14)
# 获取当前坐标系
ax = mp.gca()
# 设置主刻度和次刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置x轴主刻度样式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 网格线型
mp.grid(linestyle=':')
# 如果交易日期天数大于0，绘制整体收益情况
if len(dates) > 0:
    # 将日期转换为matplotlib中的日期
    dates = dates.astype(md.datetime.datetime)
    # 绘制收益折线图
    mp.plot(dates, profits, c='lightgray', label='Profit')
    # 绘制平均收益率水平线
    mp.axhline(y=profits.mean(), linestyle='--', color='gray')
# 如果盈利收益天数大于0，绘制盈利收益情况
if len(gain_dates) > 0:
    # 转换日期类型
    gain_dates = gain_dates.astype(md.datetime.datetime)
    # 绘制盈利情况
    mp.plot(gain_dates, gain_profits, 'o', c='orangered', label='Gain Profit')
    # 绘制平均盈利收益率水平线
    mp.axhline(y=gain_profits.mean(), linestyle='--', color='orangered')
# 如果亏损收益天数大于0
if len(loss_dates) > 0:
    # 转换日期类型
    loss_dates = loss_dates.astype(md.datetime.datetime)
    # 绘制亏损收益情况,只绘制点，不绘制线
    mp.plot(loss_dates, loss_profits, 'o', c='limegreen', label='Loss Profit')
    # 绘制平均亏损收益水平线
    mp.axhline(y=loss_profits.mean(), linestyle='--', color='limegreen')
# 显示图例
mp.legend()
# 自动调整x轴
mp.gcf().autofmt_xdate()
# 显示图形
mp.show()
