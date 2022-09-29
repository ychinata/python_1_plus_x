
import pandas as pd

print("创建Series对象".center(50, '*'))
# 列表创建
s = pd.Series([3, -5, 7, 4], index=list('ABCD'))
print(s)
# 字典创建
s = pd.Series({"A": 3, "B": -5, "C": 7, "D": 4})
print(s)
print("查询Series数据".center(50, '*'))
print(s[1])
print(s['C'])
print(s[s > 2])
print(s[[0, 1]])
print(s[['A', 'B']])
print("修改Series数据".center(50, '*'))
s[0] = 10
print(s)
s[:2] = [15, 25]
print(s)
# inplace表示在原数据生效
s.replace(15, 30, inplace=True)
print(s)
print("删除Series数据".center(50, '*'))
s.pop('A')
print(s)
del(s['B'])
print(s)
