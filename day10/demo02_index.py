import pandas as pd
import numpy as np
# reviewed:2022.9.30


df = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
print(df)
# 赋值方式修改行索引
df.index = ['aa', 'bb', 'cc']
print(df)
# 赋值方式修改列索引
df.columns = ['AA', 'BB', 'CC']
print(df)
# set_index方法，默认参数
df_s = df.set_index('AA')
print(df_s)
# set_index方法，drop参数
df_s = df.set_index('AA', drop=False)
print(df_s)
# set_index方法，drop和append参数
df_s = df.set_index('AA', drop=False, append=True)
print(df_s)
# set_index方法,drop、append、inplace参数
df.set_index('AA', drop=False, append=True, inplace=True)
print(df)

