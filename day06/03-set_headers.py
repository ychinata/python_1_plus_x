import requests


class BaiduSpider:
    def __init__(self):
        self.start_url = "https://www.baidu.com/"
        # 请求头信息
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }

    def crawl(self):
        return requests.get(self.start_url, headers=self.headers)


if __name__ == '__main__':
    baidu = BaiduSpider()
    r = baidu.crawl()
    print(r.request.headers)
    print(r.content.decode("utf8"))
