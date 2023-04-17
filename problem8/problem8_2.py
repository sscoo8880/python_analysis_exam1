# 8.一天当中点菜时间段
# 2.将统计数据图形化展示，分析一天最佳销售时间

from problem8_1 import ans8_2, ans8_3

import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']
ans8_2_hour = ans8_2.sort_values(by='place_order_hour', ascending=True)
ans8_3_hour = ans8_3.sort_values(by='place_order_hour', ascending=True)
# print(ans8_2)
# print(ans8_2_hour)
# print(ans8_3)
# print(ans8_3_hour)


########################################################3
# 小时-销售单order_id的总数
# 点图
mp.scatter(ans8_2_hour.index, ans8_2_hour.order_id)
mp.xlabel('小时')
mp.ylabel('订单总数')
mp.show()

# 条形图
step4 = ans8_2.sort_values(by='order_id', ascending=True)
mp.barh(range(10), step4.order_id)
mp.yticks(range(10), step4.index)
mp.xlabel('订单总数')
mp.ylabel('小时')
mp.show()

# 条形图
mp.bar(range(10), ans8_2_hour.order_id)
mp.xticks(range(10), ans8_2_hour.index)
mp.ylabel('订单总数')
mp.xlabel('小时')
mp.show()

# 饼图
# 饼图1
mp.figure(figsize=(11, 6))
mp.subplot(131)
mp.pie(ans8_2.order_id, autopct='%.2f%%')
mp.title('饼图')
mp.legend(ans8_2.index, loc='center right', bbox_to_anchor=(0 / 11, 5 / 11), borderaxespad=0)


# 饼图2
mp.subplot(132)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(ans8_2.order_id, explode=explodes, autopct='%.2f%%')
mp.title('突出订单总数最高的小时的饼图')

# 饼图3（空心环）
mp.subplot(133)
ans8_2['order_id_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(ans8_2.order_id, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(ans8_2.order_id_0, radius=0.6, colors='w')
mp.title('空心环的饼图')
mp.show()


####################################################
# 小时-销售总金额
# 点图
mp.scatter(ans8_3_hour.index, ans8_3_hour.purchase)
mp.xlabel('小时')
mp.ylabel('订单总金额')
mp.show()

# 条形图
step5 = ans8_3.sort_values(by='purchase', ascending=True)
mp.barh(range(10), step5.purchase)
mp.yticks(range(10), step5.index)
mp.xlabel('订单总金额')
mp.ylabel('小时')
mp.show()

# 条形图
mp.bar(range(10), ans8_3_hour.purchase)
mp.xticks(range(10), ans8_3_hour.index)
mp.ylabel('订单总金额')
mp.xlabel('小时')
mp.show()

# 饼图
# 饼图1
mp.figure(figsize=(11, 6))
mp.subplot(131)
mp.pie(ans8_3.purchase, autopct='%.2f%%')
mp.title('饼图')
mp.legend(ans8_3.index, loc='center right', bbox_to_anchor=(0 / 11, 5 / 11), borderaxespad=0)

# 饼图2
mp.subplot(132)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(ans8_3.purchase, explode=explodes, autopct='%.2f%%')
mp.title('突出订单总金额最高的小时的饼图')

# 饼图3（空心环）
mp.subplot(133)
ans8_3['purchase_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(ans8_3.purchase, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(ans8_3.purchase_0, radius=0.6, colors='w')
mp.title('空心环的饼图')
mp.show()

# 多重饼图
# y2展示菜品总收入
pie_1 = mp.pie(ans8_2.order_id, startangle=90, autopct='%.2f%%', radius=1.3, pctdistance=0.9)
pie_2 = mp.pie(ans8_3.purchase, startangle=90, autopct='%.2f%%', radius=0.8, pctdistance=0.6)
# 添加多重饼图的分割线
for pie_wedge in pie_1[0]:
    pie_wedge.set_edgecolor('black')
for pie_wedge in pie_2[0]:
    pie_wedge.set_edgecolor('black')
# bbox_to_anchor
mp.title("小时的订单总额(外)和小时的订单总金额(内)双重饼图")
mp.show()
