import pandas as pd
import numpy as np
import datetime as dt
# reviewed:2022.9.30

def deal_tem(df, col_name):
    """传入DataFrame和列名，处理温度"""
    # 将C去掉，这里需要判断数据是否为nan
    df[col_name] = df[col_name].apply(lambda x: x[:-1] if x is not np.nan else x)
    # 将切掉C之后的空串替换为nan
    df[col_name] = df[col_name].replace('', np.nan)
    # 将类型转换为浮点型
    df[col_name] = df[col_name].astype(float)


def get_wind_direct_and_level(winds):
    """传入风力得到风向和风力等级"""
    # 定义2个空列表存储风向和风力等级
    wind_directs, wind_levels = [], []
    # 遍历得到每一个风力
    for wind in winds:
        # 使用异常处理try补货异常
        try:
            # 原有风力按空格进行切分
            wind_split = wind.split()
            # 风向
            wind_direct = wind_split[0]
            # 风力等级
            wind_level = wind_split[1]
        except Exception:
            # 一旦报错，则风向和风力等级都返回nan
            wind_direct = np.nan
            wind_level = np.nan
        # 追加到列表中
        wind_directs.append(wind_direct)
        wind_levels.append(wind_level)
    # 返回
    return wind_directs, wind_levels


def gen_full_df(origin_df, full_date, left_on, right_on, sort_field, drop_col=None):
    """生成日期完整的DataFrame"""
    # 获取所有的城市
    citys = pd.unique(origin_df['city'])
    # 定义城市DataFrame的空列表
    df_list = []
    # 遍历得到每一个城市
    for city in citys:
        # 拿到城市的DataFrame
        city_df = origin_df.loc[origin_df['city'] == city]
        # 将城市的DataFrame和完整日期进行merge，以完整日期为准
        merge_df = pd.merge(city_df, full_date, left_on=left_on, right_on=right_on, how='right')
        # 保证城市列没有空值
        merge_df['city'] = city
        # 如果传入了要删除的列，则将其删除
        if drop_col:
            merge_df = merge_df.drop(labels=drop_col, axis=1)
        # 排序
        merge_df = merge_df.sort_values(by=sort_field, ascending=False)
        # 追加到列表中
        df_list.append(merge_df)
    # 将所有的DataFrame进行堆叠合并
    full_df = pd.concat(df_list)
    return full_df


def get_mode(x):
    """求众数"""
    try:
        return x.mode().values[0]
    except Exception:
        return np.nan


def fill_null_value(wait_fill_df, to_fill_df, col_name, idx1, idx2):
    # 找到某列缺失值的DataFrame
    null_v_df = wait_fill_df.loc[wait_fill_df[col_name].isnull()]
    # 定义空列表去存储应填充的缺失值
    null_list = []
    for row in null_v_df.values:
        # 找到该行应该填充的缺失值
        null_v = to_fill_df.loc[(row[idx1], row[idx2]), col_name]
        null_list.append(null_v)
    # 将应填充的值赋值到原来的地方
    wait_fill_df.loc[wait_fill_df[col_name].isnull(), col_name] = null_list
    print("填充%s成功" % col_name)


def clean_day_data():
    """清洗日表数据"""
    # 1.读取日表数据
    day_df = pd.read_csv('./data/day.csv')
    # 将id设置为索引
    day_df = day_df.set_index('id')
    # print(day_df.info())
    # 2.处理date_week
    day_df['date_week'] = day_df['date_week'].apply(lambda x: x[:10])
    # 3.处理最高温和最低温
    # 查看温度都有哪些取值类型,基本上是数字+C这种形式，注意有一个只有C的数据
    v_c = day_df['hightest_tem'].value_counts()
    # print(v_c)
    # 调用函数处理高温
    deal_tem(day_df, 'hightest_tem')
    # 调用函数处理低温
    deal_tem(day_df, 'lowest_tem')
    # 4.按城市和日期去重
    day_df = day_df.drop_duplicates(subset=['city', 'date_week'])
    print(day_df.info())
    # 5.从风力中得到风向和风力等级
    direct_levels = get_wind_direct_and_level(day_df['wind'].values)
    day_df['wind_direct'] = direct_levels[0]
    day_df['wind_level'] = direct_levels[1]
    # 将原来的wind删掉
    day_df = day_df.drop(labels='wind', axis=1)
    # print(day_df)
    # 6.为每个城市生成日期完整的DataFrame
    # 生成完整的日期
    full_day = pd.date_range(start='2011-01-01', end='2022-04-30').to_frame(name='date').astype({"date": "str"})
    # print(full_day)
    full_df = gen_full_df(day_df, full_day, left_on='date_week', right_on='date', sort_field='date',drop_col='date_week')
    print(full_df.info())
    # 7.填充缺失值
    # 生成一列，月日
    full_df['month_day'] = full_df['date'].apply(lambda x: x[5:])
    print(full_df)
    # 按照城市和月日分组，对数值型求平均值，类别型求众数
    month_day_g = full_df.groupby(by=['city', 'month_day']).agg({"hightest_tem": 'mean', 'lowest_tem': 'mean',
                                                                 "weather": get_mode, 'wind_direct': get_mode,
                                                                 'wind_level': get_mode})
    print(month_day_g)
    # 填充缺失值，0表示城市，-1表示月日
    fill_null_value(full_df, month_day_g, 'hightest_tem', 0, -1)
    fill_null_value(full_df, month_day_g, 'lowest_tem', 0, -1)
    fill_null_value(full_df, month_day_g, 'weather', 0, -1)
    fill_null_value(full_df, month_day_g, 'wind_direct', 0, -1)
    fill_null_value(full_df, month_day_g, 'wind_level', 0, -1)
    print(full_df.info())
    # 8.处理高温比低温还低的情况
    diff = full_df['hightest_tem'] - full_df['lowest_tem']
    diff[diff < 0] = 5
    full_df['hightest_tem'] = full_df['lowest_tem'] + diff
    # 9.数值型保留2位浮点数
    full_df['hightest_tem'] = full_df['hightest_tem'].apply(lambda x: round(x, 2))
    full_df['lowest_tem'] = full_df['lowest_tem'].apply(lambda x: round(x, 2))
    # 10.通过日期重新生成星期
    week_dic = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
    full_df['week_day'] = full_df['date'].apply(lambda x: week_dic[dt.datetime.strptime(x, '%Y-%m-%d').weekday()])
    # 11.数据清洗后进行保存
    full_df.to_csv('./data/clean_day.csv', index=False)


def clean_month_data():
    # 1.读取月表数据
    month_df = pd.read_csv('./data/month.csv')
    month_df = month_df.set_index('id')
    print(month_df.info())
    # 2.处理month
    month_df['month'] = month_df['month'].apply(lambda x: x[:7].replace('年', '-'))
    # 3.按城市和月份去重
    month_df = month_df.drop_duplicates(subset=['city', 'month'])
    print(month_df.info())
    # 4.处理温度
    deal_tem(month_df, 'avg_high_tem')
    deal_tem(month_df, 'avg_low_tem')
    deal_tem(month_df, 'extreme_high_tem')
    deal_tem(month_df, 'extreme_low_tem')
    # 5.处理最好和最坏日期样式
    month_df['best_air_date'] = month_df['best_air_date'].apply(lambda x: x.replace('/', '-') if x is not np.nan else x)
    month_df['worst_air_date'] = month_df['worst_air_date'].apply(lambda x: x.replace('/', '-') if x is not np.nan else x)
    print(month_df)
    # 6.为每个城市生成月份完整的DataFrame
    # 生成完整的月份
    full_month = pd.date_range(start='2011-01-01', end='2022-05-01', freq='M').to_frame(name='month').astype({"month": 'str'})
    # 对月份进行处理，只保留年-月
    full_month['month'] = full_month['month'].apply(lambda x: x[:7])
    full_df = gen_full_df(month_df, full_month, left_on='month', right_on='month', sort_field='month')
    print(full_df.info())
    # 7.读取日表数据并按年月分组，对最高温求最大和平均，得到该月的极端高温、平均高温，对最低温求最小和平均，得到该月的极端低温和平均低温
    # 读取日表数据
    day_df = pd.read_csv('./data/clean_day.csv')
    # 得到一列年月
    day_df['year_month'] = day_df['date'].apply(lambda x: x[:7])
    # print(day_df)
    # 分组
    day_g = day_df.groupby(by=['city', 'year_month']).agg({"hightest_tem": ['mean', 'max'],
                                                           "lowest_tem": ['mean', 'min']})
    day_g.columns = ['avg_high_tem', 'extreme_high_tem', 'avg_low_tem', 'extreme_low_tem']
    print(day_g)
    # 8.用日表计算出来的数据填充月表avg_high_tem、avg_low_tem、extreme_high_tem、extreme_low_tem
    # 调用函数进行填充，0表示城市，1表示年月
    fill_null_value(full_df, day_g, 'avg_high_tem', idx1=0, idx2=1)
    fill_null_value(full_df, day_g, 'avg_low_tem', idx1=0, idx2=1)
    fill_null_value(full_df, day_g, 'extreme_high_tem', idx1=0, idx2=1)
    fill_null_value(full_df, day_g, 'extreme_low_tem', idx1=0, idx2=1)
    print(full_df.info())
    # 9.月表按城市和月份分组，对平均空气质量、最好、最坏空气求平均，对最好、最坏日期求众数
    # 生成一列，只是月份
    full_df['only_month'] = full_df['month'].apply(lambda x: x[5:])
    print(full_df)
    month_g = full_df.groupby(by=['city', 'only_month']).agg({"avg_air_quality": 'mean', "best_air": 'mean',
                                                              "worst_air": 'mean', "best_air_date": get_mode,
                                                              "worst_air_date": get_mode})
    print(month_g)
    # 10.用上述计算出来的数据为平均空气质量、最好、最坏空气质量、最好、最坏空气日期进行填充
    # 调用函数进行填充，0表示城市，-1表示only_month
    fill_null_value(full_df, month_g, 'avg_air_quality', idx1=0, idx2=-1)
    fill_null_value(full_df, month_g, 'best_air', idx1=0, idx2=-1)
    fill_null_value(full_df, month_g, 'worst_air', idx1=0, idx2=-1)
    fill_null_value(full_df, month_g, 'best_air_date', idx1=0, idx2=-1)
    fill_null_value(full_df, month_g, 'worst_air_date', idx1=0, idx2=-1)
    print(full_df.info())
    # 11.浮点数保留2位浮点数
    full_df['avg_high_tem'] = full_df['avg_high_tem'].apply(lambda x: round(x, 2))
    full_df['avg_low_tem'] = full_df['avg_low_tem'].apply(lambda x: round(x, 2))
    full_df['extreme_high_tem'] = full_df['extreme_high_tem'].apply(lambda x: round(x, 2))
    full_df['extreme_low_tem'] = full_df['extreme_low_tem'].apply(lambda x: round(x, 2))
    full_df['avg_air_quality'] = full_df['avg_air_quality'].apply(lambda x: round(x, 2))
    full_df['best_air'] = full_df['best_air'].apply(lambda x: round(x, 2))
    full_df['worst_air'] = full_df['worst_air'].apply(lambda x: round(x, 2))
    # 12.清洗后数据存储
    full_df.to_csv('./data/clean_month.csv', index=False)


# clean_day_data()
clean_month_data()
