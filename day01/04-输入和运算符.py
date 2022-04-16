# input输入函数:全部是字符串
# name = input("请输入成绩（整数）：")
# # type函数：获取数据类型
# print(name)
# print(type(name))
# print(type(1))  # int,float,str,bool
# print(type(True))
# int()转整数,float()转小数,str()转字符串,
# bool()转布尔，0，“”，转成False，其他都是True
# 注意需要数据可转
# a = "战"
# b = str(a)
#
# (type(b))

# 算数运算符
# + - *乘 /除 %取余数 //取整数 **乘方
a = 10
b = 11.2
# print(a**b)
# 比较运算符:>,<,>=,<=,!=不等于,==等于
print(a!=b)
# 赋值运算符: = += -= *= /= %= //= **=
c = 1
c += 1  # c = c + 1
print(c)
# 逻辑运算符 and:同真为真 or同假为假 not否定
print(a>c or a>b)
print(not a>c)
