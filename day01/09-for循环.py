
lists = [1,2,3,4,"张三",True]
# len() 获取列表中多少个元素，元祖，字典
# print(len(lists))
# 遍历
# i = 0
# while i < len(lists):
#     print(lists[i])
#     i += 1

# for循环
# for data in lists:
#     print(data)

# range()函数，快速生成整数集
# a = range(10)
# b = list(range(10))
# print(a)
# print(b)
for i in range(len(lists)):
    print(lists[i])

# 快速生存列表
s = [x**2+1 for x in range(10)]
print(s)