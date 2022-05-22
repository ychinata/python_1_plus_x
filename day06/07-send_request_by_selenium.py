import time
from selenium import webdriver


# 实例化一个浏览器对象
chrome = webdriver.Chrome()
# 访问百度首页
chrome.get("https://www.baidu.com")
# 保存页面截图
chrome.save_screenshot("baidu.png")
# 获取网页的标题
title = chrome.title
print(title)
time.sleep(3)
# 关闭浏览器
chrome.quit()
