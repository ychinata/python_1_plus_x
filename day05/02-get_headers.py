import requests


class BaiduSpider:
    def __init__(self):
        # 目标url
        self.url = "https://www.baidu.com/"

    def crawl(self):
        """发送请求"""
        response = requests.get(self.url)
        return response


if __name__ == '__main__':
    baidu = BaiduSpider()
    r = baidu.crawl()
    print(r.request.headers)

# 通过查看没有我们想要的数据，因为百度发现我们是一个爬虫程序
# 我们查看了请求头后发现，我们的请求头就是一个Python程序
# 所以百度就知道我们是一个爬虫就不会给我们返回完整数据
# 怎么解决？
