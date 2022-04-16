import random  # 随机数

# 根据用户输入信息，判断数字大了，还是小了
# 如果用户猜对了，奖励500百万
# 在1百万内随机生成一个整数
# num = random.randint(1,1000)
# 用户需要输入多少次
# 循环嵌套，外面循环1次，里面循环n次
while True:
    print("0:退出系统")
    print("1:开始猜数")
    sta = input("请输入命令：")
    if sta == "0":
        break
    elif sta == "1":
        # 在1百万内随机生成一个整数
        num = random.randint(1, 1000)
        while True:
            res = input("请输入猜对数：")
            res = int(res)
            if res > num:
                print("你猜的数字大了，请重新猜...")
            elif res == num:
                print("恭喜你猜对了，奖励500万...")
                break
            else:
                print("你猜对数字小了，请重新猜...")
    else:
        print("你输对命令有误，请重新输入...")