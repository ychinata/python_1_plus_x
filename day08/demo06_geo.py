from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType

# 2022.6.25

# 读取数据
with open('data/air_quality.csv', encoding='utf-8') as f:
    citys, AQIS = [], []
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 城市
        city = line_split[0]
        #  AQI
        aqi = int(line_split[1])
        citys.append(city)
        AQIS.append(aqi)
# 绘制地图
# 背景色
bg_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'dodgerblue'},{offset:1,color:'cyan'}])"
# 地图区域多边形颜色
area_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'#feeff2'},{offset:1,color:'#b3fdd9'}])"
# 高亮区域多边形颜色
high_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'#e9eafd'},{offset:1,color:'#b5aff0'}])"
g = (
    Geo(
        # 初始配置，宽、高、背景色、网页标题
        init_opts=opts.InitOpts(
            width='100%',
            height='800px',
            bg_color=JsCode(bg_color),
            page_title="空气质量地图"
        ),
        # 忽略不存在的城市
        is_ignore_nonexistent_coord=True
    )
    .add_schema(
        # 地图类型
        maptype='china',
        # 地图区域的多边形图形样式
        itemstyle_opts=opts.ItemStyleOpts(
            color=JsCode(area_color),
            border_color='black'
        ),
        # 高亮状态下的多边形样式
        emphasis_itemstyle_opts=opts.ItemStyleOpts(
            color=JsCode(high_color),
            border_color='gold',
            border_width=3
        )
    )
    .add(
        "",
        [list(z) for z in zip(citys, AQIS)],
        # Geo图类型
        type_=ChartType.EFFECT_SCATTER,
        # 不显示标签
        label_opts=opts.LabelOpts(is_show=False)
    )
    .set_global_opts(
        # 视觉映射配置设置
        visualmap_opts=opts.VisualMapOpts(
            # 分段显示
            is_piecewise=True,
            pos_left='5%',
            pos_bottom='10%',
            # 分段显示颜色
            pieces=[
                {"min": 0, "max": 25, "label": "极优", "color": '#02e201'},
                {"min": 26, "max": 50, "label": "优", "color": '#019965'},
                {"min": 51, "max": 100, "label": "良", "color": '#ffff02'},
                {"min": 101, "max": 150, "label": "轻度污染", "color": '#ff7e01'},
                {"min": 151, "max": 200, "label": "中度污染", "color": '#fe0000'},
                {"min": 201, "label": "重度污染", "color": '#7a0121'},
            ]
        ),
        title_opts=opts.TitleOpts(
            title="空气质量地图",
            pos_left='center',
            pos_top='5%',
            title_textstyle_opts=opts.TextStyleOpts(
                color='#fff',
                font_size=20,
                font_weight='bold'
            )
        )
    )
).render('html/demo_06_geo.html')

