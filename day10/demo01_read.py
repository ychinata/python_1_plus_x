import pandas as pd
# reviewed:2022.9.30

# 读取数据，默认参数
iris = pd.read_csv('./data/iris.csv')
print(iris)
# 读取数据，header参数
iris1 = pd.read_csv('./data/iris.csv', header=3)
print(iris1)
# 读取数据,names参数
iris2 = pd.read_csv('./data/iris.csv', header=None, names=['h', 'w', 'c'])
print(iris2)
# names和index_col参数
iris3 = pd.read_csv('./data/iris.csv', header=None, names=['h', 'w', 'c'], index_col='w')
print(iris3)
# 读取数据，useecols参数
iris4 = pd.read_csv('./data/iris.csv', header=None, names=['h', 'w', 'c'], usecols=['h', 'w'])
print(iris4)

# 写入数据,默认参数
iris2.to_csv('./data/iris1.csv')
# 写入数据，index_label参数
iris2.to_csv('./data/iris2.csv', index_label='idx')
# 写入数据，columns参数
iris2.to_csv('./data/iris3.csv', columns=['h', 'w'])
# 写入数据，header和index参数
iris2.to_csv('./data/iris4.csv', header=False, index=False)
