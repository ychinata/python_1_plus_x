from pyecharts.charts import WordCloud
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import SymbolType

# 2022.6.25

# 读取数据
with open('data/weather_wind.csv', encoding='utf-8') as f:
    weather_dic, wind_dic = {}, {}
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        weather = line_split[0]
        wind = line_split[1]
        if weather not in weather_dic.keys():
            weather_dic[weather] = 0
        weather_dic[weather] += 1
        if wind not in wind_dic.keys():
            wind_dic[wind] = 0
        wind_dic[wind] += 1
sorted_weather = sorted(weather_dic.items(), key=lambda x: x[1], reverse=True)
sorted_wind = sorted(wind_dic.items(), key=lambda x: x[1], reverse=True)
print(sorted_weather)

# 绘图
bg_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'dodgerblue'},{offset:1,color:'cyan'}])"
w1 = (
    WordCloud(
        init_opts=opts.InitOpts(
            width='100%',
            height='800px',
            bg_color=JsCode(bg_color),
            page_title="天气词云图"
        )
    )
    .add(
        "天气",
        sorted_weather,
        # 自定义图片路径
        mask_image='data/cy.jpeg',
        width='100%',
        height='800px',
        # 词云图轮廓
        shape=SymbolType.DIAMOND
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title='天气词云图',
            title_textstyle_opts=opts.TextStyleOpts(
                color='#fff',
                font_size=20
            ),
            pos_left='center',
            pos_top='5%'
        )
    )
).render('html/demo_07_wc1.html')

w2 = (
    WordCloud(
        init_opts=opts.InitOpts(
            width='100%',
            height='800px',
            bg_color=JsCode(bg_color),
            page_title="风力词云图"
        )
    )
    .add(
        "风力",
        sorted_wind,
        # 自定义图片路径
        mask_image='data/cy.jpeg',
        width='100%',
        height='800px',
        # 词云图轮廓
        shape=SymbolType.DIAMOND
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title='风力词云图',
            title_textstyle_opts=opts.TextStyleOpts(
                color='#fff',
                font_size=20
            ),
            pos_left='center',
            pos_top='5%'
        )
    )
).render('html/demo_07_wc2.html')
