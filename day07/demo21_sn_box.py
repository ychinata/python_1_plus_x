
import seaborn as sn
import matplotlib.pyplot as mp

mp.rcParams['font.sans-serif'] = ['SimHei']


with open('../data/house.csv') as f:
    districts, prices, floors = [], [], []

    for i, line in enumerate(f):
        if i == 0:
            continue
        line_split = line.strip().split(',')
        district = line_split[7]
        price = float(line_split[0])
        floor = line_split[4]
        districts.append(district)
        prices.append(price)
        floors.append(floor)

_, ax1 = mp.subplots(1, 1, figsize=(15, 10))
# sn.boxplot(x=districts, y=prices, ax=ax1, palette='Set1', linewidth=1.5)
# sn.boxplot(x=districts, y=prices, ax=ax1, palette='Set1', linewidth=1.5, whis=10)
sn.boxplot(x=districts, y=prices, ax=ax1, palette='Set1', linewidth=1.5, whis=10, hue=floors)

mp.show()
