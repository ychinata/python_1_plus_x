from pyecharts.charts import Bar

# 2022.6.25

bar = Bar()
bar.add_xaxis(['衬衫', '羊毛衫', '西服', '鞋子', '帽子'])
bar.add_yaxis('商家', [5, 20, 36, 90, 17])
bar.render()
