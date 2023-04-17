# 9.统计一个月中销售最佳日期
# 1. 通过天进行分组，计算每天的总体销售量

# 3. 将上述两种图形化展示

from problem9_1 import ans9_1

import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']

#######################################################
# 日期-日销售量（条形图+点图）
step1 = ans9_1.sort_values(by='place_order_day', ascending=True)

# 条形图
mp.bar(step1.index, step1.order_id)
# 点图
mp.scatter(step1.index, step1.order_id)

mp.xticks(step1.index, step1.index)
mp.ylabel('日销售量')
mp.xlabel('日期')
mp.show()

#######################################################
# barh条形图（反映日销售量排行）
step2 = ans9_1.sort_values(by='order_id', ascending=True)
mp.barh(step1.index, step2.order_id)
mp.yticks(step1.index, step2.index)
mp.xlabel('日销售量')
mp.ylabel('日期')
mp.show()

########################################################
# 总日销售量饼图
# 饼图1
mp.figure(figsize=(11, 6))
mp.subplot(131)
mp.pie(ans9_1.order_id, autopct='%.2f%%')
mp.title('饼图')
mp.legend(ans9_1.index, loc='center right', bbox_to_anchor=(0 / 11, 5 / 11), borderaxespad=0)

# 饼图2
mp.subplot(132)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(ans9_1.order_id, explode=explodes, autopct='%.2f%%')
mp.title('突出日销售量最高的日期的饼图')

# 饼图3（空心环）
mp.subplot(133)
ans9_1['order_id_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(ans9_1.order_id, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(ans9_1.order_id_0, radius=0.6, colors='w')
mp.title('空心环的饼图')
mp.show()

########################################################
# 前10日销售量饼图
step3 = ans9_1.iloc[0:11, :]
# 饼图1
mp.figure(figsize=(11, 6))
mp.subplot(131)
mp.pie(step3.order_id, autopct='%.2f%%')
mp.title('饼图')
mp.legend(step3.index, loc='center right', bbox_to_anchor=(0 / 11, 5 / 11), borderaxespad=0)

# 饼图2
mp.subplot(132)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(step3.order_id, explode=explodes, autopct='%.2f%%')
mp.title('突出日销售量最高的日期的饼图')

# 饼图3（空心环）
mp.subplot(133)
# 第54行已经添加了列，不用添加了
# ans9_1['order_id_0'] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(step3.order_id, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(step3.order_id_0, radius=0.6, colors='w')
mp.title('空心环的饼图')
mp.show()

#############################################################
# 画图 所有订单id做批量分布直方图
# 批量分布直方图
print(ans9_1)
mp.hist(ans9_1.order_id, bins=5, edgecolor='black')
mp.title('频率分布直方图')
mp.show()

# 密度图
ans9_1.order_id.plot.kde()
step3.order_id.plot.kde()
mp.legend(['所有', '前10'])
mp.title('密度图')
mp.show()
