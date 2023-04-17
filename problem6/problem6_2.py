# 6.分析订单金额TOP10
# 2. 将统计的结果可视化

from problem6_1 import step3, step2

import numpy as np
import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']

# 点图
mp.scatter(step3.index, step3.purchase)
mp.xlabel('订单id')
mp.ylabel('订单金额计数')
mp.show()

# 条形图
mp.bar(range(10), step3.purchase)
mp.xticks(range(10), step3.index)
mp.ylabel('订单金额计数')
mp.xlabel('订单id')
mp.show()

# 条形图
step4 = step3.sort_values(by='purchase', ascending=True)
mp.barh(range(10), step4.purchase)
mp.yticks(range(10), step4.index)
mp.xlabel('订单金额计数')
mp.ylabel('订单id')
mp.show()


#########################################################
# 饼图
# 饼图1
mp.figure(figsize=(10, 6))
mp.subplot(221)
mp.pie(step3.purchase, autopct='%.2f%%')
mp.title('饼图')

# 饼图2
mp.subplot(222)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(step3.purchase, explode=explodes, autopct='%.2f%%')
mp.title('突出点餐最多的订单id的饼图')

# 饼图3（空心环）
mp.subplot(223)
step3['purchase_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(step3.purchase, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(step3.purchase_0, radius=0.6, colors='w')
mp.legend(step3.index, loc='center right', bbox_to_anchor=(0 / 10, 5 / 10), borderaxespad=0)
mp.title('空心环的饼图')

# 多重饼图
mp.subplot(224)
# y2展示菜品总收入
y2 = np.array(step3.purchase).ravel()
pie_1 = mp.pie(step3.purchase, startangle=90, autopct='%.2f%%', radius=1.3, pctdistance=0.9)
pie_2 = mp.pie(step3.purchase, startangle=90, autopct='%.2f%%', radius=0.8, pctdistance=0.6)
# 添加多重饼图的分割线
for pie_wedge in pie_1[0]:
    pie_wedge.set_edgecolor('black')
for pie_wedge in pie_2[0]:
    pie_wedge.set_edgecolor('black')
# bbox_to_anchor
mp.title("订单的菜品总金额数(外)和订单的菜品总金额数(内)双重饼图")
mp.show()

###################################################
# 画图 所有订单id做批量分布直方图
# 批量分布直方图
mp.hist(step2.purchase, bins=10, edgecolor='black')
mp.title('频率分布直方图')
mp.show()

# 密度图
step2.purchase.plot.kde()
step3.purchase.plot.kde()
mp.legend(['所有', '前10'])
mp.title('密度图')
mp.show()
