import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from readfromexcel import data
import matplotlib.pyplot as mp

# 1. 统计最受欢迎的菜的前十名，去除米饭的影响
# 按照菜品id分组
step1 = data.groupby('dishes_id').groups

# 统计菜品的总数
# step2=data.groupby('dishes_name').agg('count') #不用名称，因为有一些回车符号等
step2 = data.groupby('dishes_id').agg('count')
print(step2)
# 剔除米饭
# step3=step2.drop(['白饭/小碗','白饭/大碗'])
step3 = step2.drop(['610011', '610010'])
# 根据菜品总数排序
# 不剔除米饭
step4_1 = step2.sort_values('amounts', ascending=False)
print(step4_1[0:10])
# 剔除米饭
step4 = step3.sort_values('amounts', ascending=False)
print(step4[0:10])

# 2. 并将最受欢迎的菜品可视化，通过柱状图和折线图展现
step5 = step4[0:10].iloc[:, 1]
step6 = pd.merge(step5, data.iloc[:, [2, 3]], on='dishes_id', how='left')
print(step5)
print(step6)
print(type(step6))
print("ok6")
step7 = step6.loc[:, ['order_id', 'dishes_name']]
# step7 = step6.drop_duplicates(subset=['dishes_id'], keep='first', inplace=True)
print(step7)
print("ok7")
print(type(step7))
print("ok77")
step8 = step7.drop_duplicates(subset=None, keep='first', inplace=False)
print(step8)
# print(step7.drop_duplicates())
print("ok7none")
print(type(step8))
print("oknone")
step9 = step8.iloc[0:10, ]
print(step9)
print("okk")
print(type(step9))
print(step9.dtypes)
print("okkk")
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']
xs = pd.Series(step9.dishes_name, dtype="string")
step9.dishes_name.type = "string"
print(step9.dtypes)
print(xs)
print("xsok")
# step9.plot.pie(subplots=True)
print(step9.iloc[:, 2:3])
print("xsssss")
step9.index = step9.dishes_name
step9.columns=['购买次数','菜品名称']
print(step9)
# df = pd.DataFrame(step9, columns=['购买次数'])
df = pd.DataFrame(step9)
# df.xticks=step9.columns['dishes_name']
df.plot.bar()

mp.show()
# 3. 统计最受欢迎的菜品前十名的价格区间分布
# 4. 统计最受欢迎的菜品前十名的平均价格，中位数，四分位数
