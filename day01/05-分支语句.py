# 30岁男人，1选择家庭，2选择事业
# res = input("输入选择：")
"""
if 条件（真/假）：
    真：执行这行代码
elif 条件2：
    真：执行这行代码
else:
    假:执行这行代码
"""
# if res == "1":
#     print("家庭幸福")
# elif res == "2":
#     print("事业有成")
# else:
#     print("你输入的有误....")
# 三元运算符
a = 20
b = 30
if a>b:
    print("a是最大的")
else:
    print("b最大{}".format(b))
#
c = a if a>b else b
print(c)
