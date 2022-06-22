import pandas as pd

df = pd.read_csv('house.csv', encoding='gbk')
print(df)
df.to_csv('house1.csv', encoding='utf-8', index=False)