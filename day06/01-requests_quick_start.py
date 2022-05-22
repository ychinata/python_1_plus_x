import requests


# 往百度的首页发送请求， 请求方式可以经过抓包进行确定
r = requests.get("https://www.baidu.com")

# 获取响应的编码方式
encoding = r.encoding
print(encoding)

# 获取响应状态码
status = r.status_code
print(status)

# 获取响应字符串
r_text = r.text
# print(r_text)

# 获取响应字节流
content = r.content
print(content)

# 对响应字节流进行解码
print(r.content.decode("utf8"))
