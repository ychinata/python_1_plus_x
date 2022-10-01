import pandas as pd
# reviewed:2022.9.29

print("创建DataFrame对象".center(50, '*'))
# 列表创建
df = pd.DataFrame([['China', 'Beijing', 20000000], ['American', 'NewYork', 15000000],
                   ['England', 'London', 10000000]], columns=['Country', 'City', 'Population'])
print(df)
# 字典创建
df = pd.DataFrame({"Country": ['China', 'American', 'England'], "City": ['Beijing', 'NewYork', 'London'],
                   "Population": [20000000, 15000000, 10000000]})
print(df)
# DataFrame创建
df1 = pd.DataFrame(df, columns=['Country', 'City'])
print(df1)
