# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p=1']

    def parse(self, response):
        # 获取包含书籍信息的所有li标签
        books_data = response.xpath("//ul[@class='chart-dashed-list']/li")
        for book in books_data:
            book_item = DoubanItem()
            # 获取图书的封面
            img_link = book.xpath(
                "./div[@class='media__img']/a/img/@src"
            ).extract_first()
            book_item["img_link"] = img_link.strip() if img_link else ""

            # 获取书名
            title = book.xpath(
                "./div[@class='media__body']/h2/a/text()"
            ).extract_first()
            book_item["title"] = title.strip() if title else "未名"

            # 获取详细信息
            details = book.xpath(
                "./div[@class='media__body']/p[1]/text()"
            ).extract_first()
            details = details.split("/")
            if len(details) == 5:
                # 获取作者
                book_item["author"] = details[0].strip() if details[0] else "佚名"
                # 获取出版日期
                book_item["publish_date"] = details[1].strip() if details[1] else "未知"
                # 获取出版社
                book_item["publisher"] = details[2].strip() if details[2] else "未知"
                # 获取价格
                book_item["price"] = details[3].strip() if details[3] else "未知"
                # 获取装订方式
                book_item["binding"] = details[4].strip() if details[4] else "未知"

                # 获取评分
                score = book.xpath(
                    "./div[@class='media__body']/p[2]/span[2]/text()"
                ).extract_first()
                book_item["score"] = score.strip() if score else "未评分"
                # 将item对象传到管道中
                yield book_item

        # 获取下一页的url
        next_page_url = response.xpath(
            "//a[contains(text(), '后页')]/@href"
        ).extract_first()
        if next_page_url:
            # 发送请求
            yield response.follow(
                url=next_page_url,
                callback=self.parse
            )
