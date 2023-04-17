# 9.统计一个月中销售最佳日期
# 2. 通过周进行分组，对一周的每天进行统计统计点菜量和星期的关系

from problem1 import data

# 取dayofweek找出本日对应星期x
data['weekday']=data.place_order_time.dt.dayofweek

# 取本日日期，便于排序，去重
data['place_order_day'] = data.place_order_time.dt.day

# 取有用的列
step1 = data.loc[:, ['order_id', 'weekday','place_order_day']]

# 去重
step2 = step1.drop_duplicates(subset=None, keep='first', inplace=False)

# 先按日期排序，再按order_id排序
step3 = step2.sort_values(by=['weekday', 'place_order_day','order_id'])

# 去重
step3 = step3.drop_duplicates(subset=None, keep='first', inplace=False)

# 1.通过小时分组统计小时内订单总额
step4 = step3.groupby('weekday').agg({'order_id': 'count'})

step4['orders_weekday']=step4['order_id']/[5,5,5,4,4,4,4]

# 结果排序（每天的每小时）
step5 = step4.sort_values(by=['orders_weekday'], ascending=False)

# 保留有用的列
ans9_2=step5.loc[:,['orders_weekday']]
