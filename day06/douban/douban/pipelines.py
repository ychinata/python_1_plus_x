# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class DoubanPipeline(object):
    def __init__(self):
        # 创建MongoDB数据库连接对象
        self.client = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )["douban"]["book"]

    def process_item(self, item, spider):
        # 将item对象转换为字典
        book_item = {
            "title": item["title"],
            "img_link": item["img_link"],
            "author": item["author"],
            "publisher": item["publisher"],
            "publish_date": item["publish_date"],
            "price": item["price"],
            "binding": item["binding"],
            "score": item["score"]
        }
        # 保存到MongoDB数据库中
        self.client.insert(book_item)
        return item
