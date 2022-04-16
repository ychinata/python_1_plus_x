# input，print,len,format,range,int,float,str,bool,list,tuple,dict系统函数
# 自定义函数：一段功能的代码块
# 任意输入两个数，计算和
"""
def 函数名(a,b):
    函数体
"""
# 形参和实参一一对应
# 有参函数
# def adds(num,num2): # num1,num2形参 num = a,num2 = b
#     print(num+num2)
#
# a = int(input("请输入一个数："))
# b = int(input("请输入另一个数："))
# adds(a,b)  # 实参

# 无参函数
# import random
# # 打印1-10的随机整数
# def randdint():
#     a = random.randint(1,11)
#     # 返回值，元组
#     return a,a
#
# print(randdint()[0]+1)
# 匿名函数

nums = lambda a:a**2 # 参数 ：函数体
print(nums(10))