from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 2022.6.25

# 读取数据
# open函数在windows系统下打开文件默认是GBK的编码
with open('data/weather_wind.csv', encoding='utf-8') as f:
    weather_dic, wind_dic = {}, {}
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 天气
        weather = line_split[0]
        # 风力
        wind = line_split[1]
        if weather not in weather_dic.keys():
            weather_dic[weather] = 0
        weather_dic[weather] += 1
        if wind not in wind_dic.keys():
            wind_dic[wind] = 0
        wind_dic[wind] += 1
# print(weather_dic)
# print(wind_dic)
# 降序排序取前10位,reverse表示反转
sorted_weather = sorted(weather_dic.items(), key=lambda x: x[1], reverse=True)[:10]
print(sorted_weather)
sorted_wind = sorted(wind_dic.items(), key=lambda x: x[1], reverse=True)[:10]

# 绘制饼图
bg_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'dodgerblue'},{offset:1,color:'cyan'}])"
pie1 = (
    Pie(
        # 初始配置,宽、高、背景色、网页标题
        init_opts=opts.InitOpts(
            width='100%',
            height='800px',
            bg_color=JsCode(bg_color),
            page_title="天气情况"
        )
    )
    .add(
        "天气",
        # 数据
        sorted_weather,
        # 玫瑰样式图,radius和area
        rosetype='radius',
        # 圆心
        center=['50%', '50%'],
        # 半径
        radius=['20%', '40%'],
        label_opts=opts.LabelOpts(
            # 标签位置,outside在饼图外,inside在饼图上
            position='outside',
            # 格式:{a}：系列名,{b}：数据名 {c}：数据值 {d}:百分比
            # {a|{a}} 前面的a表示样式,后面的a表示系列名，abg是a样式的背景设置
            formatter="{a|{a}}{abg|}\n{hr|}\n{b|{b}:}{c} {per|{d}%}",
            # 背景色
            background_color='#b0eef9',
            # 边框颜色
            border_color='#aaa',
            # 边框宽度
            border_width=1,
            # 边框圆角
            border_radius=5,
            # 富文本样式
            rich={
                # a样式
                "a": {"color": "blue", "lineHeight": 20, "align": "center", "fontsize": 10},
                # a样式的背景
                "abg": {
                    "backgroundColor": "#7fcee4",
                    "width": '100%',
                    "align": 'right',
                    "height": 20,
                    "borderRadius": [4, 4, 0, 0]
                },
                # 中间分割线样式
                "hr": {
                    "borderColor": "black",
                    "width": '100%',
                    "borderWidth": 0.2,
                    "height": 0
                },
                # b样式
                "b": {"fontsize": 12, "lineHeight": 25},
                # per样式作用于百分数
                "per": {
                    "color": 'violet',
                    "backgroundColor": '#334455',
                    "padding": [2, 3],
                    "borderRadius": 2
                }
            }
        )
    )
    .set_global_opts(
        # 图例设置，不显示
        legend_opts=opts.LegendOpts(is_show=False),
        # 标题设置
        title_opts=opts.TitleOpts(
            title="天气情况",
            pos_left='center',
            pos_top='1%',
            title_textstyle_opts=opts.TextStyleOpts(color='#fff')
        )
    )
).render('html/demo_05_pie1.html')

pie2 = (
    Pie(
        # 初始配置,宽、高、背景色、网页标题
        init_opts=opts.InitOpts(
            width='100%',
            height='800px',
            bg_color=JsCode(bg_color),
            page_title="风力情况"
        )
    )
    .add(
        "风力",
        # 数据
        sorted_wind,
        # 玫瑰样式图,radius和area
        rosetype='area',
        # 圆心
        center=['50%', '50%'],
        # 半径
        radius=['20%', '40%'],
        label_opts=opts.LabelOpts(
            # 标签位置,outside在饼图外,inside在饼图上
            position='outside',
            # 格式:{a}：系列名,{b}：数据名 {c}：数据值 {d}:百分比
            # {a|{a}} 前面的a表示样式,后面的a表示系列名，abg是a样式的背景设置
            formatter="{a|{a}}{abg|}\n{hr|}\n{b|{b}:}{c} {per|{d}%}",
            # 背景色
            background_color='#b0eef9',
            # 边框颜色
            border_color='#aaa',
            # 边框宽度
            border_width=1,
            # 边框圆角
            border_radius=5,
            # 富文本样式
            rich={
                # a样式
                "a": {"color": "blue", "lineHeight": 20, "align": "center", "fontsize": 10},
                # a样式的背景
                "abg": {
                    "backgroundColor": "#7fcee4",
                    "width": '100%',
                    "align": 'right',
                    "height": 20,
                    "borderRadius": [4, 4, 0, 0]
                },
                # 中间分割线样式
                "hr": {
                    "borderColor": "black",
                    "width": '100%',
                    "borderWidth": 0.2,
                    "height": 0
                },
                # b样式
                "b": {"fontsize": 12, "lineHeight": 25},
                # per样式作用于百分数
                "per": {
                    "color": 'violet',
                    "backgroundColor": '#334455',
                    "padding": [2, 3],
                    "borderRadius": 2
                }
            }
        )
    )
    .set_global_opts(
        # 图例设置，不显示
        legend_opts=opts.LegendOpts(is_show=False),
        # 标题设置
        title_opts=opts.TitleOpts(
            title="风力情况",
            pos_left='center',
            pos_top='1%',
            title_textstyle_opts=opts.TextStyleOpts(color='#fff')
        )
    )
).render('html/demo_05_pie2.html')
