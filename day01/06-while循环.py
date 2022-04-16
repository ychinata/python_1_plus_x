# i = 0
"""
while 条件：
    条件成立执行循环
# 有限循环
# 无限循环：死循环
# break 退出当前循环，以下代码都不执行
# continue: 跳过当前循环，进入下一层循环，以下代码都不执行
"""
# while i < 3:
#     name = input("请输入用户名：")
#     if name == "退出":
#         break
#     print(name)
# 打印1-10的偶数
i = 0
while i < 11:
    i += 1
    if i % 2 == 1:
        continue
    print(i)

# while True:
# while if input format print 运算符

