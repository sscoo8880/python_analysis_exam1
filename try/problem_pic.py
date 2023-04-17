# 方法二 numpy
# 展成numpy一维数组
import numpy as np
import matplotlib.pyplot as mp

from problem3_3 import step9

# 只要最受欢迎参数(all_counts)
step10 = step9.loc[:, ['all_counts']]

y = np.array(step10).ravel()
x = np.array(step10.index)

# 折线图
mp.plot(x, y)
mp.plot(x[1:9], y[1:9], 'oc')
mp.plot(x[0], y[0], '*r', markersize=15)
show_max = '[' + str(x[0]) + ' ' + str(y[0]) + ']'
mp.annotate(show_max, xytext=(x[0], y[0]), xy=(x[0], y[0]))
mp.plot(x[9], y[9], '*g', markersize=15)
show_min = '[' + str(x[9]) + ' ' + str(y[9]) + ']'
mp.annotate(show_min, xytext=(x[9], y[9]), xy=(x[9], y[9]))
mp.xticks(rotation=45)
mp.title('菜品受欢迎程度折线图')
mp.show()

# 柱状图
mp.bar(x, y)
mp.xticks(rotation=45)
mp.show()

# 饼图
# 饼图1
mp.figure(figsize=(10,6))
mp.subplot(221)
mp.pie(y, autopct='%.2f%%')
# mp.legend(x, loc='center left', bbox_to_anchor=(9 / 10, 9 / 10), borderaxespad=0)
mp.title('饼图')
# mp.show()

# 饼图2
mp.subplot(222)
explodes = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0)
mp.pie(y, explode=explodes, autopct='%.2f%%')
# mp.legend(x, loc='center left', bbox_to_anchor=(9 / 10, 9 / 10), borderaxespad=0)
mp.title('突出最受欢迎的的菜品的饼图')
# mp.show()

# 饼图3（空心环）
mp.subplot(223)
y_0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mp.pie(y, radius=1.0, pctdistance=0.8,  autopct='%.2f%%')
mp.pie(y_0, radius=0.6, colors='w')
mp.legend(x, loc='center right', bbox_to_anchor=(0 / 10, 3 / 10), borderaxespad=0)
mp.title('空心环的饼图')
# mp.show()

# 多重饼图
mp.subplot(224)
# y2展示菜品总收入
y2 = np.array(step9.all_amounts).ravel()
pie_1 = mp.pie(y, startangle=90, autopct='%.2f%%', radius=1.3, pctdistance=0.9)
pie_2 = mp.pie(y2, startangle=90, autopct='%.2f%%', radius=0.8, pctdistance=0.6)
# 添加多重饼图的分割线
for pie_wedge in pie_1[0]:
    pie_wedge.set_edgecolor('black')
for pie_wedge in pie_2[0]:
    pie_wedge.set_edgecolor('black')
# bbox_to_anchor
# mp.legend(x, loc='center left', bbox_to_anchor=(9 / 10, 9 / 10), borderaxespad=0)
mp.title("受欢迎程度(外)和价格(内)双重饼图")
mp.show()  # 显示图表

