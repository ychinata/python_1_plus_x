import pandas as pd
# reviewed:2022.9.30

df = pd.DataFrame({"A": [1, 2, 3], "B": [10.1, 20.2, 30.3], "C": ['a', 'b', 'c']})
print(df)
# 查看类型
print(df.dtypes)
# 转换为字符串类型
df_dt = df.astype('str')
print(df_dt)
print(df_dt.dtypes)
# 将A列转换为浮点型，B列转换为整型
df_dt = df.astype({"A": float, "B": int})
print(df_dt)
print(df_dt.dtypes)
