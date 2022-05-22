import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 实例化一个Chrome对象
chrome = webdriver.Chrome()
# 发送请求
chrome.get("https://www.baidu.com")
# 找到搜索框，输入关键词
# 老版本的一个写法
# chrome.find_element_by_id('kw').send_keys("人工智能")
# 新版本的写法
chrome.find_element(by=By.ID, value="kw").send_keys("数据挖掘")
# 获取提交按钮进行点击
# chrome.find_element_by_id('su').click()
chrome.find_element(by=By.ID, value='su').click()
time.sleep(5)
# 关闭浏览器
chrome.quit()
