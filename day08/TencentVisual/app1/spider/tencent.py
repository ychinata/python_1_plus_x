
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TencentVisual.settings')
django.setup()

# 导入相关库
import requests
import time
import random
import json
from urllib import parse
from app1.models import *
import math


class TencentSpider:
    def __init__(self, job_name):
        self.job_name = job_name
        # 一级页面url
        self.one_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1655623782920&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
        # 二级页面url
        self.two_url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1655623613345&postId={}&language=zh-cn"
        # 请求头
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}

    def get_html(self, url):
        resp = requests.get(url=url, headers=self.headers)
        return resp.content.decode()

    def get_job_page(self, encode_job):
        """获取岗位总页数逻辑"""
        # 拼接第一页的url
        base_url = self.one_url.format(encode_job, 1)
        # 发送请求，获取响应内容
        infos = self.get_html(base_url)
        # 通过json转为字典
        job_infos = json.loads(infos)
        # 提取岗位总数
        job_count = int(job_infos['Data']['Count'])
        # 计算岗位页数,每页10条
        total_page = math.ceil(job_count / 10)
        return total_page

    def is_id_in_db(self, post_id):
        res = Tencent.objects.filter(post_id=post_id)
        if res:
            return True
        return False

    def get_post_ids(self):
        # 对职位进行编码
        encode_job = parse.quote(self.job_name)
        # 获取岗位页数
        total_page = self.get_job_page(encode_job)
        # 拼接每一页的url
        for page in range(1, total_page+1):
            page_url = self.one_url.format(encode_job, page)
            # 发送请求
            page_info = self.get_html(page_url)
            # 随机休眠
            time.sleep(random.uniform(0.2, 0.8))
            # 提取岗位信息
            job_posts = json.loads(page_info)['Data']['Posts']
            objs = []
            for job in job_posts:
                # 提起post_id,作为职位的标识
                post_id = job['PostId']
                # 判断post_id在不在表中
                if self.is_id_in_db(post_id):
                    print("职位%s已经抓取过" % post_id)
                    continue
                # post_id的岗位信息
                obj = self.extract_job_infos(post_id)
                objs.append(obj)
            # 插入10个岗位
            Tencent.objects.bulk_create(objs)
            print("插入第%d页成功" % page)

    def extract_job_infos(self, post_id):
        """提取岗位信息"""
        # 拼接二级页面url
        two_url = self.two_url.format(post_id)
        # 发送请求
        job_infos = self.get_html(two_url)
        job_dic = json.loads(job_infos)['Data']
        # 岗位名称
        name = job_dic['RecruitPostName']
        # 地点
        location = job_dic['LocationName']
        # 岗位类型
        kind = job_dic['CategoryName']
        # 岗位职责
        duty = job_dic['Responsibility']
        # 岗位需求
        require = job_dic['Requirement']
        # 更新时间
        update_time = job_dic['LastUpdateTime']
        # 封装到模型类对象
        obj = Tencent(input_job_name=self.job_name, post_id=post_id, name=name, location=location, kind=kind,
                      duty=duty, require=require, update_time=update_time)
        return obj

    def run(self):
        self.get_post_ids()


if __name__ == '__main__':
    spider = TencentSpider('高级运维')
    spider.run()
