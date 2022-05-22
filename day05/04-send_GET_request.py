import requests


class BaiduSpider:
    def __init__(self):
        self.start_url = "https://www.baidu.com/s?"
        # 请求头信息
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }
        # 搜索的参数
        self.parameters = {
            "wd": self.get_keyword()
        }

    @staticmethod
    def get_keyword():
        keyword = input("请输入要搜索的关键词：")
        return keyword

    def crawl(self):
        return requests.get(
            url=self.start_url,
            headers=self.headers,
            params=self.parameters
        ).content.decode()


if __name__ == '__main__':
    baidu = BaiduSpider()
    r = baidu.crawl()
    print(r)
