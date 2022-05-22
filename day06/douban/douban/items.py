# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    title = scrapy.Field()
    # 封面
    img_link = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 出版社
    publisher = scrapy.Field()
    # 出版日期
    publish_date = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 装订方式
    binding = scrapy.Field()
    # 评分
    score = scrapy.Field()
