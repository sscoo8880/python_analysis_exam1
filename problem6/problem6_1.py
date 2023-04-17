# 6.分析订单金额TOP10
# 1. 分组统计订单消费金额排序

from problem1 import data

# sum(counts*amounts)by order_id
data['purchase']=data['amounts']*data['counts']

# 分组统计
step1 = data.groupby('order_id').agg({'purchase': 'sum'})

# 排序
step2=step1.sort_values(by='purchase',ascending=False)

# 取前10
step3 = step2.iloc[0:10, :]
