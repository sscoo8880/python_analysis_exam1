# 2.统计平均价格，统计价格中位数，统计价格四分位数
# 1. 统计卖出菜品的平均价格
# 2. 统计卖出菜品的中位数
# 3. 统计卖出菜品的四分位数分析订单销售价格集中区间

from problem1 import data

# 1. 统计卖出菜品的平均价格
print(data.amounts.mean())

# 2. 统计卖出菜品的中位数
print(data.amounts.median())

# 3. 统计卖出菜品的四分位数分析订单销售价格集中区间
# 即把数值由小到大排列并分成四等份Z，处于三个分割点位置的数值就是四分位数
print(data.quantile(q=0.25, axis=0, numeric_only=True, interpolation='linear'))
# q : 数字或者是类列表，范围只能在0-1之间，默认是0.5，即中位数-第2四分位数
# axis :计算方向，可以是 {0, 1, ‘index’, ‘columns’}中之一，默认为 0
# interpolation（插值方法）:可以是 {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}之一，默认是linear。
