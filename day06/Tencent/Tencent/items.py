# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名
    recruit_post_name = scrapy.Field()
    # 国家名
    country_name = scrapy.Field()
    # 工作城市
    location_name = scrapy.Field()
    BG_name = scrapy.Field()
    # 产品名
    product_name = scrapy.Field()
    # 分类
    category_name = scrapy.Field()
    # 职位描述
    responsibility = scrapy.Field()
    # 更新时间
    last_update_time = scrapy.Field()
    # 职位详情连接
    post_url = scrapy.Field()

