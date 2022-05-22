from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://www.baidu.com")

# 获取网页源码
page = chrome.page_source
# print(page)
# 获取当前的url
current_url = chrome.current_url
print(current_url)

# 获取百度首页页脚的信息
# find_element默认取第一个，find_elements是去所有元素
# about_contents = chrome.find_elements(by=By.CLASS_NAME, value="text-color")
# for content in about_contents:
#     print(content.text)

# 根据name属性获取元素
# chrome.find_element(by=By.NAME, value="wd").send_keys("Ruby")

# 使用xpath获取元素
# chrome.find_element(by=By.XPATH, value="//input[@id='kw']").send_keys("数据挖掘")

# 通过元素中文本内容获取元素
# chrome.find_element(by=By.PARTIAL_LINK_TEXT, value="hao").click()
# chrome.find_element(by=By.LINK_TEXT, value="hao123").click()

# 通过CSS选择器获取元素
# chrome.find_element(by=By.CSS_SELECTOR, value=".s_ipt").send_keys("Flask")

# 获取百度热搜
hots_search = chrome.find_elements(
    by=By.XPATH,
    value="//li[contains(@class, 'hotsearch-item')]/a"
)
# 遍历标签列表
hots = []
for hot in hots_search:
    title = hot.find_element(by=By.XPATH, value="./span[2]")
    item = {"title": title.text, "href": hot.get_attribute("href")}
    hots.append(item)
for h in hots:
    print(h)

# chrome.quit()
