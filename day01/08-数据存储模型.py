# 整数，小数，str字符串，布尔,None
# 列表！=数组
# b = [] # 空列表
# a = [1,12.1,"a",True,[1,2,3]] # 有元素列表
# print(a)
# 列表操作,12.1,"a",True,[
# 增：append() 方法,在列表后追加
# a.append("张三")
# print(a)
# 删除：pop(num)方法,num删除对下标,如果不存在，表示删除最后一个
# a.pop()
# print(a)
# 查询一个
# print(a[1])
# 查多个
# print(a[1:4])
# 修改
# 先获取再修改
# a[2] = "张三"
# print(a)

# 元组:不允许改变 tuple  列表list
# b = (1,2,3,"a")
# # 查询
# print(b[2])
# print(a,type(a))
# c = tuple(a)
# print(c,type(c))

# 字典{键:值} dict
a = {"0":"张三","age":18,"count":[1,2,3,4,5]}
# print(a)
# 获取
# print(a["0"])
# # 键名是不能重复的
# # 增加
# a["log"] = "中国"
# print(a)
# # 修改
# a["age"] = 19
# print(a)
# # 删除
# a.pop("0")
# print(a)

# 字符串是特殊对列表
strs = "1234.速度.asd"
print(strs[5])
# 字符串拼接+，*多次重复
print(strs+"aaaa")
print("-"*30)