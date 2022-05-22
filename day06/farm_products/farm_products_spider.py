import json

from selenium import webdriver
from selenium.webdriver.common.by import By


class FarmProductSpider:
    # 实例化一个配置对象
    options = webdriver.ChromeOptions()
    # 启用无头模式
    options.add_argument("--headless")
    # 禁用GPU
    options.add_argument("--disable-gpu")

    def __init__(self):
        # 浏览器对象
        self.chrome = webdriver.Chrome(options=self.options)
        # 起始url
        self.start_url = "https://www.cnhnb.com/purchase/"
        # 记录爬取的是第几页
        self.current_page = 1
        # 用来保存每一页的数据
        self.page_data = []

    def parse_data(self):
        # 获取每一页的所有行
        lines = self.chrome.find_elements(
            by=By.XPATH,
            value="//div[@class='content']/ul/li[@class='eye-renderer__item']"
        )
        print(f"crawling the {self.current_page} page...")
        self.page_data = [self.parse_product(line) for line in lines]
        self.save_data()
        self.current_page += 1

    def save_data(self):
        # 保存数据
        # 序列化
        json_data = json.dumps(self.page_data, ensure_ascii=False, indent=2)
        print(f"saving the {self.current_page} page...")
        filename = f"{self.current_page}-page.json"
        with open(filename, "w", encoding="utf8") as f:
            f.write(json_data)

    @staticmethod
    def parse_product(line):
        """使用xpath提取一行数据"""
        # 采购的品种
        cate_name = line.find_element(
            by=By.XPATH,
            value=".//div[@class='cateName']"
        ).text
        # 采购数量
        qty = line.find_element(
            by=By.XPATH,
            value=".//div[@class='qty']"
        ).text
        # 期望货源地址
        scope_full_name = line.find_element(
            by=By.XPATH,
            value=".//div[@class='scopeFullName']"
        ).text
        # 发布人
        link_name = line.find_element(
            by=By.XPATH,
            value=".//div[@class='linkName']"
        ).text
        return {
            "cate_name": cate_name,
            "qty": qty,
            "scope_full_name": scope_full_name,
            "link_name": link_name
        }

    def crawl(self):
        # 发送请求
        self.chrome.get(self.start_url)
        while True:
            # 解析数据
            self.parse_data()
            try:
                # 翻页
                next_btn = self.chrome.find_element(
                    by=By.XPATH,
                    value="//button[@class='btn-next']"
                )
                # 使用selenium执行js代码
                self.chrome.execute_script("arguments[0].click();", next_btn)
            except Exception as e:
                print(e)
                # 退出浏览器
                self.chrome.quit()
                break


if __name__ == '__main__':
    farm = FarmProductSpider()
    try:
        farm.crawl()
    except KeyboardInterrupt:
        print("手动停止了爬虫^_^")
        exit()
