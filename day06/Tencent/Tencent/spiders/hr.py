# -*- coding: utf-8 -*-
import json
import re

import scrapy
from Tencent.items import TencentItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?" \
               "parentCategoryId=40001&pageIndex={}&pageSize=300"
    start_urls = [base_url.format(1)]

    def parse(self, response):
        page = re.findall(r"pageIndex=(\d*)", response.url)[0]
        # 反序列化
        jobs = json.loads(response.text)["Data"]["Posts"]
        if jobs:
            for job in jobs:
                item = TencentItem()
                item["recruit_post_name"] = job["RecruitPostName"]
                item["country_name"] = job["CountryName"]
                item["location_name"] = job["LocationName"]
                item["BG_name"] = job["BGName"]
                item["product_name"] = job["ProductName"]
                item["category_name"] = job["CategoryName"]
                item["responsibility"] = job["Responsibility"]
                item["last_update_time"] = job["LastUpdateTime"]
                item["post_url"] = job["PostURL"]
                yield item
            yield scrapy.Request(
                url=self.base_url.format(int(page) + 1),
                callback=self.parse
            )
