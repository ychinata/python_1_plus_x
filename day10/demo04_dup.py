import pandas as pd
# reviewed:2022.9.30

df = pd.DataFrame({"A": [1, 1, 2, 2], "B": [1, 2, 1, 2]})
print(df)
# 判断A列是否重复
df_d = df.duplicated(subset='A')
print(df_d)
# 判断A列是否重复，keep参数
df_d = df.duplicated(subset='A', keep='last')
print(df_d)
# 判断A列和B列是否重复
df_d = df.duplicated(subset=['A', 'B'])
print(df_d)

# A列去重
drop_d = df.drop_duplicates(subset='A')
print(drop_d)
# A列去重，keep参数
drop_d = df.drop_duplicates(subset='A', keep='last')
print(drop_d)
# A列去重，ignore_index和inplace参数
df.drop_duplicates(subset='A', inplace=True, ignore_index=True)
print(df)

