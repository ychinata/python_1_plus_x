# 自定义导入
# 1
# from rands import Dog
# 2
# import rands
# 3
from rands import *
# import random
#
# print(random.randint(1,10))
from random import randint
print(randint(1,20))

# try:如果有错，执行except下对代码
try:
    num = int(input("请输入薪资金额："))
    if num > 20:
        print("高薪")
# as起别名：e
except Exception as e:
    print("系统报错了:",e)

Dog().play()