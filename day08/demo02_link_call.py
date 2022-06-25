from pyecharts.charts import Bar

# 2022.6.25

bar = (
    Bar()
    .add_xaxis(['衬衫', '羊毛衫', '西服', '鞋子', '帽子'])
    .add_yaxis('商家', [20, 98, 76, 53, 29])
    .render('link.html')
)
