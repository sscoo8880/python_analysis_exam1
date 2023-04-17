# 2.统计平均价格，统计价格中位数，统计价格四分位数
# 1. 统计卖出菜品的平均价格
# 2. 统计卖出菜品的中位数
# 3. 统计卖出菜品的四分位数分析订单销售价格集中区间

from problem1 import data

import matplotlib.pyplot as mp

mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['axes.unicode_minus'] = False

# 取菜品id、价格amounts
step1 = data.loc[:, ['dishes_id', 'counts', 'amounts']]

# 去重
step2 = step1.drop_duplicates(subset='dishes_id', keep='first', inplace=False)

######################################################################################3
# 1. 统计卖出菜品的平均价格
ans1 = step2.amounts.mean()

######################################################################################3
# 2. 统计卖出菜品的中位数
ans2 = step2.median()

######################################################################################3
# 3. 统计卖出菜品的四分位数分析订单销售价格集中区间
ans3 = step2.quantile(q=0.25, axis=0, numeric_only=True, interpolation='linear')
step2.amounts.plot.hist(bins=10,edgecolor='black')
mp.title('价格频率分布直方图')
mp.show()
# ans2.to_excel(r'C:\Users\user\Desktop\py\exam1\problem2.xlsx', index=False)
