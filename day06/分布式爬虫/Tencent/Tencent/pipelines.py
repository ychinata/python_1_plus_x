# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TencentPipeline(object):
    def __init__(self):
        # 数据库连接对象
        self.connect = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            db='tencent',
            user="root",
            password="root"
        )
        # 游标对象
        self.cur = self.connect.cursor()
        # 准备SQL语句
        create_table_sql = """
            create table if not exists `job` (
            job_id int unsigned auto_increment,
            job_name varchar(100),
            country_name varchar(50),
            location_name varchar(100),
            BG_name varchar(50),
            product_name varchar(50),
            category_name varchar(50),
            description text,
            update_time varchar(20),
            post_url text,
            primary key(job_id)
            );
        """
        # 执行SQL语句创建表
        self.cur.execute(create_table_sql)
        self.connect.commit()
        print("数据表创建成功^_^")

    def process_item(self, item, spider):
        insert_sql = """
            insert into job(
                job_name,
                country_name,
                location_name,
                BG_name,
                product_name,
                category_name,
                description,
                update_time,
                post_url
            ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cur.execute(
            insert_sql,
            [
                item["recruit_post_name"],
                item["country_name"],
                item["location_name"],
                item["BG_name"],
                item["product_name"],
                item["category_name"],
                item["responsibility"],
                item["last_update_time"],
                item["post_url"]
            ]
        )
        # 提交事务
        self.connect.commit()
        print("数据保存成功^_^")
        return item

    def __del__(self):
        self.connect.close()
        self.cur.close()
