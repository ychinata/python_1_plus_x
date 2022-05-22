import re
import requests


class YouDao:
    def __init__(self):
        # 翻译地址
        self.url = "https://m.youdao.com/translate"
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36"
        }
        # 请求数据
        self.data = {
            # 需要翻译的内容
            "inputtext": "",
            # 翻译模式
            "type": "AUTO"
        }

    @staticmethod
    def get_text():
        # 提示用户输入需要翻译的内容
        text = input("请输入你要翻译的一个内容(输入q|Q退出)：")
        # 判断输入的内容是否为q或者Q
        q_or_Q = (text == "q") or (text == "Q")
        # 不是q或者Q返回输入内容，是q或者Q退出程序
        return text if not q_or_Q else exit()

    def parse_url(self):
        # 获取翻译的内容
        text = self.get_text()
        # 给请求参数赋值
        self.data["inputtext"] = text
        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=self.data)
        # 对响应解码并返回
        return response.content.decode()

    @staticmethod
    def parse_data(html_str):
        # 使用正则表达式来提取翻译结果
        result = re.search(r'<ul id="translateResult">\s*<li>(.*)</li>\s*</ul>', html_str)
        # 有结果就返回，没有返回None
        return result.group(1) if result else None

    def run(self):
        # 发送请求获取数据
        ret = self.parse_url()
        # 解析翻译结果
        return self.parse_data(ret)


if __name__ == '__main__':
    youdao = YouDao()
    while True:
        translate = youdao.run()
        print(f"翻译结果：{translate}")
