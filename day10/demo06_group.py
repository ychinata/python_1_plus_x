import numpy as np
import pandas as pd
# reviewed:2022.9.30

df = pd.DataFrame({"key1": ['a', 'a', 'b', 'b', 'a'],
                   "key2": ['one', 'two', 'one', 'two', 'one'],
                   "data1": np.random.randn(5),
                   'data2': np.random.randn(5)})
print(df)
# 按key1进行分组
g = df.groupby(by='key1')
print(g)
# 分组之后求平均
print(g.mean())
# 按两个字符安分组
g1 = df.groupby(by=['key1', 'key2'])
print(g1)
# 分组之后求和
print(g1.sum())
# agg方法
res = df.groupby(by='key1').agg({"key2": 'count', "data1": ['mean', 'sum']})
print(res)
