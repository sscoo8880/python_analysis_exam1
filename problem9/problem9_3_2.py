# 9.统计一个月中销售最佳日期
# 2. 通过周进行分组，对一周的每天进行统计统计点菜量和星期的关系

# 3. 将上述两种图形化展示

from problem9_2 import ans9_2

import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']
print(ans9_2)

########################################################3
# 星期x-星期x点菜量（条形图+点图）
step1 = ans9_2.sort_values(by='weekday', ascending=True)

# 条形图
mp.bar(step1.index, step1.orders_weekday)
# 点图
mp.scatter(step1.index, step1.orders_weekday)

mp.xticks(step1.index, step1.index+1)
mp.ylabel('星期x点菜量')
mp.xlabel('星期x')
mp.show()

#######################################################
# barh条形图（反映星期x点菜量排行）
step2 = ans9_2.sort_values(by='orders_weekday', ascending=True)
mp.barh(range(7), step2.orders_weekday)
mp.yticks(range(7), step2.index+1)
mp.xlabel('星期x点菜量')
mp.ylabel('星期x')
mp.show()

########################################################
# 总星期x点菜量饼图
# 饼图1
mp.figure(figsize=(11, 6))
mp.subplot(131)
mp.pie(ans9_2.orders_weekday, autopct='%.2f%%')
mp.title('饼图')
mp.legend(ans9_2.index+1, loc='center right', bbox_to_anchor=(0 / 11, 5 / 11), borderaxespad=0)

# 饼图2
mp.subplot(132)
explodes = (0.15, 0.08, 0, 0, 0, 0, 0)
mp.pie(ans9_2.orders_weekday, explode=explodes, autopct='%.2f%%')
mp.title('突出星期x点菜量最高的星期x的饼图')

# 饼图3（空心环）
mp.subplot(133)
ans9_2['orders_weekday_0'] = [1, 0, 0, 0, 0, 0, 0]
mp.pie(ans9_2.orders_weekday, radius=1.0, pctdistance=0.8, autopct='%.2f%%')
mp.pie(ans9_2.orders_weekday_0, radius=0.6, colors='w')
mp.title('空心环的饼图')
mp.show()

#############################################################
# 画图 所有订单id做批量分布直方图
# 批量分布直方图
mp.hist(ans9_2.orders_weekday, bins=3, edgecolor='black')
mp.title('频率分布直方图')
mp.show()

# 密度图
ans9_2.orders_weekday.plot.kde()
mp.title('密度图')
mp.show()
