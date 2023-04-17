# 4.订单点菜种类统计
# 2. 将统计的结果可视化

from problem4_1 import step4, step3

import numpy as np
import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']
print(step4)

# 点图
mp.scatter(step4.index, step4.counts)
mp.xlabel('订单id')
mp.ylabel('点菜种类计数')
mp.show()

# 条形图
mp.bar(range(14), step4.counts)
mp.xticks(range(14), step4.index)
mp.ylabel('点菜种类计数')
mp.xlabel('订单id')
mp.show()

# 条形图
step5 = step4.sort_values(by='counts', ascending=True)
mp.barh(range(14), step5.counts)
mp.yticks(range(14), step5.index)
mp.xlabel('点菜种类计数')
mp.ylabel('订单id')
mp.show()

#########################################33
# 饼图
# 饼图1
mp.figure(figsize=(10, 6))
mp.subplot(221)
mp.pie(step4.counts, autopct='%.2f%%')
mp.title('饼图')

# 饼图2
mp.subplot(222)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(step4.counts, explode=explodes, autopct='%.2f%%')
mp.title('突出点餐最多的订单id的饼图')

# 饼图3（空心环）
mp.subplot(223)
step4['counts_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(step4.counts, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(step4.counts_0, radius=0.6, colors='w')
mp.legend(step4.index, loc='center right', bbox_to_anchor=(0 / 10, 5 / 10), borderaxespad=0)
mp.title('空心环的饼图')

# 多重饼图
mp.subplot(224)
# y2展示菜品总收入
y2 = np.array(step4.counts).ravel()
pie_1 = mp.pie(step4.counts, startangle=90, autopct='%.2f%%', radius=1.3, pctdistance=0.9)
pie_2 = mp.pie(step4.counts, startangle=90, autopct='%.2f%%', radius=0.8, pctdistance=0.6)
# 添加多重饼图的分割线
for pie_wedge in pie_1[0]:
    pie_wedge.set_edgecolor('black')
for pie_wedge in pie_2[0]:
    pie_wedge.set_edgecolor('black')
# bbox_to_anchor
mp.title("订单的菜品种类数(外)和订单的菜品种类数(内)双重饼图")
mp.show()

# 画图 所有订单id做批量分布直方图
# 批量分布直方图
mp.hist(step3.counts, bins=10, edgecolor='black')
mp.title('频率分布直方图')
mp.show()

# 密度图
step3.counts.plot.kde()
step4.counts.plot.kde()
mp.legend(['所有', '前10'])
mp.title('密度图')
mp.show()
