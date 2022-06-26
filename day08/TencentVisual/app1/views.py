from django.shortcuts import render
from django.http import HttpResponse
from app1.spider import tencent
from app1.visual import tencent_plot


def index(request):
    # return HttpResponse("这是首页")
    return render(request, 'index.html')


def crawl_data(request, job_name):
    # 启动爬虫，会将数据存入数据库
    spider = tencent.TencentSpider(job_name)
    spider.run()
    # 词云图可视化
    wc = tencent_plot.plot_all_fig(job_name)
    return HttpResponse(wc.render_embed())
