from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 2022.6.25

# 读取数据
with open('data/cd_tq.csv') as f:
    dates, hightest_tem, lowest_tem = [], [], []
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 日期
        date = line_split[1]
        # 最高温
        hi_tem = int(line_split[2])
        # 最低温
        low_tem = int(line_split[3])
        dates.append(date)
        hightest_tem.append(hi_tem)
        lowest_tem.append(low_tem)
# 背景色
# 渐变色，0,0,0,1分别代表右、下、左、上，第5个参数是设置渐变色的
bg_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'darkviolet'},{offset:1,color:'cyan'}])"
high_area_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'red'},{offset:0.5,color:'orange'},{offset:1,color:'yellow'}])"
low_area_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'violet'},{offset:0.5,color:'green'},{offset:1,color:'blue'}])"

# 绘图
line = (
    Line(
        init_opts=opts.InitOpts(width='100%', height='800px', page_title="成都十年最高温和最低温", bg_color=JsCode(bg_color))
    )
    .add_xaxis(dates)
    .add_yaxis(
        '最高温',
        hightest_tem,
        # 显示标记
        is_symbol_show=True,
        # 标记实心圆
        symbol='circle',
        # 标记大小
        symbol_size=8,
        # 光滑曲线
        is_smooth=True,
        # 线颜色和宽度设置
        linestyle_opts=opts.LineStyleOpts(color='#fff', width=1.5),
        # 标签设置
        label_opts=opts.LabelOpts(color='#fff'),
        # 图元样式设置
        itemstyle_opts=opts.ItemStyleOpts(
            color='lightpink',
            border_color='coral',
            border_width=3
        ),
        # 区域填充设置,opacity是图形透明度，0表示全透明
        areastyle_opts=opts.AreaStyleOpts(color=JsCode(high_area_color), opacity=1)
    )
    .add_yaxis(
        '最低温',
        lowest_tem,
        is_symbol_show=True,
        symbol='circle',
        symbol_size=8,
        is_smooth=True,
        linestyle_opts=opts.LineStyleOpts(color='cyan', width=1.5),
        label_opts=opts.LabelOpts(color='cyan', position='bottom'),
        itemstyle_opts=opts.ItemStyleOpts(
            color='dodgerblue',
            border_width=3,
            border_color='darkviolet'
        ),
        areastyle_opts=opts.AreaStyleOpts(
            color=JsCode(low_area_color), opacity=0.5
        )
    )
    .set_global_opts(
        # 标题设置
        title_opts=opts.TitleOpts(
            title='成都2011-2022年最高温和最低温',
            pos_left='center',
            pos_top='10px',
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold', color='#fff')
        ),
        # 图例设置
        legend_opts=opts.LegendOpts(
            pos_top='7%',
            # 垂直对齐
            orient='vertical',
            # 图例为方块
            legend_icon='rect',
            textstyle_opts=opts.TextStyleOpts(color='#fff')
        ),
        # y轴设置
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(color='#fff'),
            axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='#fff'))
        ),
        # x轴设置
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(color='#fff'),
            axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='#fff'))
        ),
        # 区域缩放配置
        datazoom_opts=opts.DataZoomOpts(
            # 可选slider、inside
            type_='slider',
            # 数据窗口范围起始百分比
            range_start=0,
            range_end=5
        ),
        # 提示框组件配置，trigger触发类型，item数据项触发(默认),axis坐标轴触发,none什么都不触发
        tooltip_opts=opts.TooltipOpts(trigger='axis')
    )
).render('line.html')
