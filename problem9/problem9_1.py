# 9.统计一个月中销售最佳日期
# 1. 通过天进行分组，计算每天的总体销售量

from problem1 import data

# 取天
data['place_order_day'] = data.place_order_time.dt.day

# 取有用的列
step1 = data.loc[:, ['order_id', 'place_order_day']]

# 先按日期排序，再按order_id排序
step2 = step1.sort_values(by=['place_order_day', 'order_id'])

# 去重
step3 = step2.drop_duplicates(subset=None, keep='first', inplace=False)

# 1.通过小时分组统计小时内订单总额
ans9_1 = step3.groupby('place_order_day').agg({'order_id': 'count'})

# 结果排序（每天的每小时）
ans9_1 = ans9_1.sort_values(by=['order_id'], ascending=False)

