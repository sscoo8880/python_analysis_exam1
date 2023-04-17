# 5.分析订单点菜量的TOP10
# 1. 通过订单的id分组统计点菜数量TOP10

from problem1 import data

# 取有用的列
step1 = data.loc[:, ['order_id', 'counts']]

# groupby order_id，count counts
step2 = step1.groupby('order_id').agg({'counts': 'sum'})

# 排序
step3 = step2.sort_values(by='counts',ascending=False)

# 前10
# 10-14同名次
step4 = step3.iloc[0:11, :]
