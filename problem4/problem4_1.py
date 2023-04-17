# 4.订单点菜种类统计
# 1. 统计订单点菜种类前十名

from problem1 import data

# 取有用的列
step1 = data.loc[:, ['order_id', 'counts']]

# groupby order_id，count counts
step2 = step1.groupby('order_id').agg({'counts': 'count'})

# 排序
step3 = step2.sort_values(by='counts',ascending=False)

# 前10
# 10-14同名次
step4 = step3.iloc[0:14, :]
