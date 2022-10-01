import pandas as pd
# reviewed:2022.9.30

# 生成时间序列，指定start和end
d1 = pd.date_range(start='2010-01-01', end='2010-01-05')
print(d1)
# 生成时间序列,指定start和periods
d2 = pd.date_range(start='2010-01-01', periods=5)
print(d2)
# 生成时间序列,指定start，periods和freq
d3 = pd.date_range(start='2010-01-01', periods=5, freq='M')
print(d3)
# 生成时间序列，指定freq为2个日历日
d4 = pd.date_range(start='2010-01-01', periods=5, freq=pd.DateOffset() * 2)
print(d4)
# 生成时间序列，指定freq为一个工作日
d5 = pd.date_range(start='2010-01-01', periods=10, freq=pd.offsets.BDay())
print(d5)

