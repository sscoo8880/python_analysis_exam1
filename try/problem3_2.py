import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from readfromexcel import data
import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']

data=data.loc[:,['dishes_id','counts','amounts']]
# pd.to_numeric(data.counts,errors='raise',downcast='signed')
# data.astype({'counts':'int64'})
print(data)
print(type(data))
print(data.dtypes)
print("ok")
# 1. 统计最受欢迎的菜的前十名，去除米饭的影响
# 按照菜品id分组
step1 = data.groupby('dishes_id').groups
print("step1")
print(step1)
# pd.to_numeric(step1.counts,downcast='signed')
print(data.dtypes)
# 统计菜品的总数
# step2=data.groupby('dishes_name').agg('count') #不用名称，因为有一些回车符号等
step2 = data.groupby('dishes_id').agg({'counts':'sum'})
print("step2")
print(step2)
# 剔除米饭
step3 = step2.drop(['610011', '610010'])

# 根据菜品总数排序
step4 = step3.sort_values('counts', ascending=False)

# 2. 并将最受欢迎的菜品可视化，通过柱状图和折线图展现
# 按照找前10个的菜品id（同一个id可能对应多个name）——（前十个id-购买量）的表
step5 = step4[0:10].iloc[:, 1]

# 所有菜品对应的id——（id-菜名）的表
step5_2=data.iloc[:,[2,3]]

# 将（前十个id-购买量）的表和（id-菜名）的表进行左外连接/内连得到新的表6
step6 = pd.merge(step5, step5_2, on='dishes_id', how='left')

# 表6将菜名-购买量联系起来了，此时中间量菜品id无用，需要剔除
step7 = step6.loc[:, ['order_id', 'dishes_name']]

# 左外连接产生了重复行，需要剔除
step8 = step7.drop_duplicates(subset=None, keep='first', inplace=False)

# 设置DataFrame的序号为dishes_name，方便后面作图的时候可以将索引设置为x坐标轴
step8.index = step8.dishes_name

# 重新设置DataFrame的列名称，方便自己查看，方便展示在图上的图例
step8.columns=['all_amounts','dishes_name']

# 发现第十名“蒙古烤羊腿”名字有误（回车没有剔除），则用iloc取前10行，loc取order_id列
print(step8)
step9 = step8.iloc[0:10, ].loc[:,'all_amounts']



print(step9)

# 画图
# 方法一
step9.plot.bar()

# 画图
# 方法二
# plt2 = pd.DataFrame(data=step9,index=list("1234567890"))
# plt2.plot.pie(subplots=True)
step9.plot.pie(subplots=True)

mp.legend()
mp.show()
# 3. 统计最受欢迎的菜品前十名的价格区间分布
# 4. 统计最受欢迎的菜品前十名的平均价格，中位数，四分位数
