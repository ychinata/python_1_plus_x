import pandas as pd
import numpy as np
# reviewed:2022.9.30


df = pd.DataFrame(np.arange(24).reshape(6, 4), index=list('abcdef'), columns=list('ABCD'))
df.loc['a', 'B'] = np.nan
df.loc['d', 'C'] = np.nan
print(df)
# 统计缺失值
print(df.isnull())
# 统计每列缺失值
print(df.isnull().sum(axis=0))
# 统计每行缺失值
print(df.isnull().sum(axis=1))
# notnull方法
print(df.notnull())
print('*' * 30)
# info方法
print(df.info())

# 删除缺失值，默认参数
df_drop = df.dropna()
print(df_drop)
# 删除缺失值，axis参数
df_drop = df.dropna(axis=1)
print(df_drop)
# 删除缺失值,subset参数
df_drop = df.dropna(subset=['a', 'b'], axis=1)
print(df_drop)

# 填充一个数
df_fill = df.fillna(value=10)
print(df_fill)
# method取pad
df_fill = df.fillna(method='pad')
print(df_fill)
# method取bfill，axis取1
df_fill = df.fillna(method='bfill', axis=1)
print(df_fill)
