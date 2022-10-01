import numpy as np
import pandas as pd
# reviewed:2022.9.30

# 创建DataFrame
df1 = pd.DataFrame(np.zeros((3, 4)), columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)), columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df1)
print(df2)
# 堆叠合并，默认参数
c1 = pd.concat([df1, df2])
print(c1)
# 横向堆叠合并
c2 = pd.concat([df1, df2], axis=1)
print(c2)
# 纵向堆叠合并，求交集
c3 = pd.concat([df1, df2], axis=0, join='inner')
print(c3)
# 纵向堆叠合并，求交集，重置索引
c4 = pd.concat([df1, df2], join='inner', ignore_index=True)
print(c4)
# 纵向堆叠合并，keys和names参数
c5 = pd.concat([df1, df2], keys=['dfA', 'dfB'], names=['idx1', 'idx2'])
print(c5)

