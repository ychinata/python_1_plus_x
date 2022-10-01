import pandas as pd
import numpy as np
# reviewed:2022.9.30


# 创建DataFrame
df = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
print(df)
# by参数
df_sort = df.sort_values(by='A')
print(df_sort)
# by、axis和ascending参数
df_sort = df.sort_values(by='a', axis=1, ascending=False)
print(df_sort)
# by、ascending、ignore_index参数
df_sort = df.sort_values(by='A', ascending=False, ignore_index=True)
print(df_sort)

