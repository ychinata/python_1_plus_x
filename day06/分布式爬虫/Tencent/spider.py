from scrapy.cmdline import execute
import os
import sys
import redis


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_redis_connect(host="127.0.0.1", port=6379, db=1):
    # 获取数据库连接对象
    con = redis.Redis(host, port, db)
    return con


def push_urls(list_name, *args):
    con = create_redis_connect()
    return con.lpush(list_name, *args)


if __name__ == '__main__':
    start_url = "https://careers.tencent.com/tencentcareer/api/post/Query?" \
                "parentCategoryId=40001&pageIndex=1&pageSize=300"
    queue_name = 'tencent'
    push_urls(queue_name, start_url)
    execute(["scrapy", "crawl", "hr"])
