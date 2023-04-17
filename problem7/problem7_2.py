# 7.订单平均消费统计
# 2. 将统计数据图形化展示

from problem7_1 import ans7

import numpy as np
import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']
# print(ans7)
step1 = ans7.sort_values(by='purchase_per_counts', ascending=False)
step2 = step1.iloc[0:10, :]
# print(step2)

# 点图
mp.scatter(step2.index, step2.purchase_per_counts)
mp.xlabel('订单id')
mp.ylabel('订单平均消费')
mp.show()

# 条形图
step4 = step2.sort_values(by='purchase_per_counts', ascending=True)
mp.barh(range(10), step4.purchase_per_counts)
mp.yticks(range(10), step4.index)
mp.xlabel('订单平均消费')
mp.ylabel('订单id')
mp.show()

# 条形图
mp.bar(range(10), step2.purchase_per_counts)
mp.xticks(range(10), step2.index)
mp.ylabel('订单平均消费')
mp.xlabel('订单id')
mp.show()

# 饼图
# 饼图1
mp.figure(figsize=(10, 6))
mp.subplot(221)
mp.pie(step2.purchase_per_counts, autopct='%.2f%%')
mp.title('饼图')

# 饼图2
mp.subplot(222)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(step2.purchase_per_counts, explode=explodes, autopct='%.2f%%')
mp.title('突出平均消费最高的订单id的饼图')

# 饼图3（空心环）
mp.subplot(223)
step2['purchase_per_counts_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(step2.purchase_per_counts, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(step2.purchase_per_counts_0, radius=0.6, colors='w')
mp.legend(step2.index, loc='center right', bbox_to_anchor=(0 / 10, 5 / 10), borderaxespad=0)
mp.title('空心环的饼图')

# 多重饼图
mp.subplot(224)
# y2展示菜品总收入
y2 = np.array(step2.purchase_per_counts).ravel()
pie_1 = mp.pie(step2.purchase_per_counts, startangle=90, autopct='%.2f%%', radius=1.3, pctdistance=0.9)
pie_2 = mp.pie(step2.purchase_per_counts, startangle=90, autopct='%.2f%%', radius=0.8, pctdistance=0.6)
# 添加多重饼图的分割线
for pie_wedge in pie_1[0]:
    pie_wedge.set_edgecolor('black')
for pie_wedge in pie_2[0]:
    pie_wedge.set_edgecolor('black')
# bbox_to_anchor
mp.title("订单的菜品总平均消费(外)和订单的菜品总平均消费(内)双重饼图")
mp.show()

#############################################################
# 画图 所有订单id做批量分布直方图
# 点图
mp.scatter(ans7.index, ans7.purchase_per_counts)
mp.xlabel('订单id')
mp.ylabel('订单平均消费点图')
mp.title('频率分布直方图')
mp.show()

# 批量分布直方图
mp.hist(ans7.purchase_per_counts, bins=10, edgecolor='black')
mp.title('频率分布直方图')
mp.show()

# 密度图
ans7.purchase_per_counts.plot.kde()
step2.purchase_per_counts.plot.kde()
mp.legend(['所有', '前10'])
mp.title('密度图')
mp.show()
