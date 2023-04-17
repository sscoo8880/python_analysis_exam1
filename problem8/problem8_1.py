# 8.一天当中点菜时间段
# 1. 通过小时分组统计小时内订单总额

from problem1 import data

data['place_order_hour'] = data.place_order_time.dt.hour
data['place_order_day'] = data.place_order_time.dt.day
data['place_order_day_hour'] = data.place_order_time.dt.day * 100 + data.place_order_time.dt.hour

#######################################################33
# ans8_1 步骤同下
# 取有用的列
step1 = data.loc[:, ['order_id', 'place_order_day_hour']]

# 先按日期排序，再按order_id排序
step2 = step1.sort_values(by=['place_order_day_hour', 'order_id'])

# 去重
step3 = step2.drop_duplicates(subset=None, keep='first', inplace=False)

# 1.通过小时分组统计小时内订单总额
ans8_1 = step3.groupby('place_order_day_hour').agg({'order_id': 'count'})

# 结果排序（每天的每小时）
ans8_1 = ans8_1.sort_values(by=['order_id'], ascending=False)


#######################################################33
# ans8_2 步骤同上
# 取有用的列
step4 = data.loc[:, ['order_id', 'place_order_hour']]

# 先按日期排序，再按order_id排序
step5 = step4.sort_values(by=['place_order_hour', 'order_id'])

# 去重
step6 = step5.drop_duplicates(subset=None, keep='first', inplace=False)

# 1.通过小时分组统计小时内订单总额
ans8_2 = step6.groupby('place_order_hour').agg({'order_id': 'count'})

# 结果排序（每天的每小时）
ans8_2 = ans8_2.sort_values(by=['order_id'], ascending=False)


#######################################################33
# ans8_3 步骤同上
# 算每列的金额
data['purchase']=data['amounts']*data['counts']

# 取有用的列
step7 = data.loc[:, ['place_order_hour','purchase']]

# 1.通过小时分组统计每小时的总消费
ans8_3 = step7.groupby('place_order_hour').agg({'purchase': 'sum'})
ans8_3 = ans8_3.sort_values(by=['purchase'], ascending=False)

#
# print(ans8_1)
# print(ans8_2)
# print(ans8_3)
