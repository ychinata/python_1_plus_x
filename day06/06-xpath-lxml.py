import json

from lxml import etree


# 读取文件
with open("./search_engine.html", "r", encoding="utf8") as f:
    text = f.read()
# print(text)
# 把字符串编程标签对象
html = etree.HTML(text)
# 把标签对象变为字符串
# print(etree.tostring(html))
# 获取class='item-0'的li标签里面的a标签的href属性值
href = html.xpath("//li[@class='item-0']/a/@href")[0]
print(href)

# 获取class='item-1'的li标签中所有a标签的href属性和文本内容
a_list = html.xpath("//li[@class='item-1']/a")
content = []
# 遍历a_list
for a in a_list:
    item = {"href": a.xpath("./@href")[0], "text": a.xpath("./text()")[0]}
    content.append(item)
print(content)

# 获取类名 包含 ‘item’的li标签中所有a标签的href属性和文本内容
a_list = html.xpath("//li[contains(@class, 'item')]/a")
# print(len(a_list))
content = []
for a in a_list:
    item = {"href": a.xpath("./@href")[0], "text": a.xpath("./text()")[0]}
    content.append(item)

with open("engine.json", "w", encoding="utf8") as f:
    f.write(json.dumps(content, ensure_ascii=False, indent=2))


