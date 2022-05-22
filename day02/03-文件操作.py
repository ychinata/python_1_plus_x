
# 文件写入
"""
# utf-8 万国码
with open(路径,"w:写入",encoding='utf-8') as f:
    f.write("写入内容“)
文件操作方式：
w:覆盖写，如果文件不存在，直接创建
a：追加写，文件不存在会报错
r:读,文件不存在会报错
"""
import json
# json.dumps 将字典转成字符串
# json.loads 将字符串转成字典
with open("data/text.txt","a",encoding="utf-8") as f:
    f.write(json.dumps({"name":"张三"},ensure_ascii=False)+"\n")
#
# print("文件已写入")

with open("data/text.txt","r",encoding="utf-8") as f:
    # content = f.read()
    content = f.readlines()
# read：读出所有内容
print(content)
for data in content:
    print(json.loads(data)["name"])

"{‘name’:'张三'}"