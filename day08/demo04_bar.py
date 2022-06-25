from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 2022.6.25

# 读取数据
with open('data/tem.csv') as f:
    # 高温字典
    hi_dic = {}
    # 低温字典
    low_dic = {}
    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        # 高温
        hi_tem = int(line_split[1])
        # 低温
        low_tem = int(line_split[2])
        # 判断该高温是否存在，不存在就初始化
        if hi_tem not in hi_dic.keys():
            hi_dic[hi_tem] = 0
        # 高温频数加1
        hi_dic[hi_tem] += 1
        if low_tem not in low_dic.keys():
            low_dic[low_tem] = 0
        low_dic[low_tem] += 1
# 高温排序
sorted_hi_tem = sorted(hi_dic.items(), key=lambda x: x[0])
print(sorted_hi_tem)
# 低温排序
sorted_low_tem = sorted(low_dic.items(), key=lambda x: x[0])
# 获取高温
hi_tem = [t[0] for t in sorted_hi_tem]
print(hi_tem)
# 获取高温频数
hi_num = [t[1] for t in sorted_hi_tem]
print(hi_num)

# 获取低温
low_tem = [t[0] for t in sorted_low_tem]
# 低温频数
low_num = [t[1] for t in sorted_low_tem]

# 绘制条形图
bg_color = "new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'dodgerblue'},{offset:1,color:'cyan'}])"
bar1 = (
    Bar(
        # 初始配置，宽度、高度、背景色、网页标题
        init_opts=opts.InitOpts(
            width='100%',
            height='600px',
            bg_color=JsCode(bg_color),
            page_title="最高温频数统计"
        )
    )
    .add_xaxis(hi_tem)
    .add_yaxis(
        '高温频数',
        hi_num,
        # 条宽度
        bar_width='60%',
        # 标题颜色设置
        label_opts=opts.LabelOpts(color='black')
    )
    .set_global_opts(
        # 标题设置
        title_opts=opts.TitleOpts(
            title='最高温频数统计',
            # 左右居中
            pos_left='center',
            pos_top='1%',
            # 标题文本设置
            title_textstyle_opts=opts.TextStyleOpts(color='#fff', font_weight='bold')
        ),
        # 图例设置，不显示
        legend_opts=opts.LegendOpts(is_show=False),
        # 区域缩放配置
        datazoom_opts=[opts.DataZoomOpts(range_start=0, range_end=20), opts.DataZoomOpts(type_='inside', range_start=0, range_end=20)]
    )
    .set_series_opts(
        # 图元样式设置
        itemstyle_opts=opts.ItemStyleOpts(
            # 柱条颜色,渐变色
            color=JsCode("new echarts.graphic.LinearGradient(0,1,1,0,[{offset:0,color:'yellow'},"
                         "{offset:0.5,color:'orange'},{offset:1,color:'red'}])"),
            border_color='#ff7600',
            border_width=1
        )
    )
).render('bar1.html')

bar2 = (
    Bar(
        # 初始配置，宽度、高度、背景色、网页标题
        init_opts=opts.InitOpts(
            width='100%',
            height='600px',
            bg_color=JsCode(bg_color),
            page_title="最低温频数统计"
        )
    )
    .add_xaxis(low_tem)
    .add_yaxis(
        '低温频数',
        low_num,
        # 条宽度
        bar_width='60%',
        # 标题颜色设置
        label_opts=opts.LabelOpts(color='black')
    )
    .set_global_opts(
        # 标题设置
        title_opts=opts.TitleOpts(
            title='最低温频数统计',
            # 左右居中
            pos_left='center',
            pos_top='1%',
            # 标题文本设置
            title_textstyle_opts=opts.TextStyleOpts(color='#fff', font_weight='bold')
        ),
        # 图例设置，不显示
        legend_opts=opts.LegendOpts(is_show=False),
        # 区域缩放配置
        datazoom_opts=[opts.DataZoomOpts(range_start=0, range_end=20), opts.DataZoomOpts(type_='inside', range_start=0, range_end=20)]
    )
    .set_series_opts(
        # 图元样式设置
        itemstyle_opts=opts.ItemStyleOpts(
            # 柱条颜色,渐变色
            color=JsCode("new echarts.graphic.LinearGradient(0,1,1,0,[{offset:0,color:'blue'},"
                         "{offset:0.5,color:'dodgerblue'},{offset:1,color:'cyan'}])"),
            border_color='#ff7600',
            border_width=1
        )
    )
).render('bar2.html')
