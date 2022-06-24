import matplotlib.pyplot as mp

# 2022.6.23

# 设置支持中文字体,字体样式为黑体
mp.rcParams['font.sans-serif'] = ['SimHei']

# 读取us评论数据
with open('data/US_video_data_numbers.csv') as f:
    us_comments = []
    # 迭代读取
    for line in f:
        line_split = line.strip().split(',')
        us_comments.append(int(line_split[-1]))
print(us_comments)
# 读取uk评论数据
with open('data/GB_video_data_numbers.csv') as f:
    uk_comments = []
    # 迭代读取
    for line in f:
        line_split = line.strip().split(',')
        uk_comments.append(int(line_split[-1]))
print(uk_comments)
mp.figure("美国评论")
mp.title("美国评论", fontsize=18)
mp.xlabel("评论数量", fontsize=12)
mp.ylabel("频数", fontsize=12)
# 直方图条形数目
bins = list(range(0, 5001, 250))
mp.hist(us_comments, bins=bins, facecolor='orangered', edgecolor='black')
mp.xticks(bins)
mp.tick_params(labelsize=8)

# 英国评论直方图
mp.figure("英国评论")
mp.title("英国评论", fontsize=18)
mp.xlabel("评论数量", fontsize=12)
mp.ylabel("频数", fontsize=12)
# 直方图条形数目
bins = list(range(0, 5001, 250))
mp.hist(uk_comments, bins=bins, facecolor='dodgerblue', edgecolor='black')
mp.xticks(bins)
mp.tick_params(labelsize=8)
mp.show()
