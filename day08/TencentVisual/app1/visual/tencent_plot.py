
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TencentVisual.settings')
django.setup()
# 导入项目根目录
from TencentVisual.settings import BASE_DIR
# 导入模型类
from app1.models import *
import jieba
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig, SymbolType, JsCode
from pyecharts.charts import WordCloud, Page
from pyecharts import options as opts

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader(os.path.join(BASE_DIR, 'app1/templates')))


def plot_all_fig(job_name):
    wc1 = plot_wc('require', job_name)
    wc2 = plot_wc('duty', job_name)
    # 顺序多图
    page = Page(layout=Page.SimplePageLayout, page_title="词云图")
    page.add(wc1, wc2)
    return page


def plot_wc(field, job_name):
    # 读取指定岗位某个字段的数据
    res = Tencent.objects.filter(input_job_name=job_name).values(field)
    # 进行拼接
    all_str = ''.join([item[field] for item in res])
    # 结巴分词
    jieba_cut = list(jieba.cut(all_str))
    # 只保留中文和英文
    jieba_cut = [word for word in jieba_cut if ('\u4e00' <= word <= '\u9fa5') or ('A' <= word <= 'Z') or ('a' <= word <= 'z')]
    # 排除的、和、者、有
    jieba_cut = [word for word in jieba_cut if word not in ['的', '和', '者', '有']]
    # 频数统计
    s = pd.Series(jieba_cut)
    v_c = s.value_counts()
    print(v_c)
    # 获取词语
    words = [str(w) for w in v_c.index]
    # 获取数量
    nums = [int(n) for n in v_c.values]
    # 背景色
    bg_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'dodgerblue'},{offset:1,color:'cyan'}])"
    # 绘制词云图
    wc = (
        WordCloud(
            init_opts=opts.InitOpts(width='50%', height='100vh', bg_color=JsCode(bg_color))
        )
        .add(
            field,
            [list(z) for z in zip(words, nums)],
            # 自定义图片路径
            mask_image=os.path.join(BASE_DIR, 'static/images/cy.jpeg'),
            # 词云轮廓
            shape=SymbolType.DIAMOND
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='%s%s词云图' % (job_name, field),
                title_textstyle_opts=opts.TextStyleOpts(
                    color='#fff',
                    font_size=20
                ),
                pos_left='center',
                pos_top='5%'
            )
        )
    )
    return wc


if __name__ == '__main__':
    # w = plot_wc('require', '高级运维')
    # w.render()
    w = plot_all_fig('高级运维')
    w.render()
