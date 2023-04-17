# 3.频数统计，最受欢迎的菜
# 3. 统计最受欢迎的菜品前十名的价格区间分布

from problem1 import data
from problem3_1 import step9

import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

mp.rcParams["font.sans-serif"] = 'SimHei'
mp.rcParams['axes.unicode_minus'] = False

# data.amounts.plot.hist(bins=10)

# 所有菜品对应的价格——（菜名-价格）的表
step2 = data.loc[:, ['dishes_name', 'amounts']]
# 重复行需要剔除
step2_2 = step2.drop_duplicates(subset='dishes_name', keep='first', inplace=False)

# 将（前十个菜名）的表和（菜名-价格）的表进行左外连接得到新的表3
step3 = pd.merge(step9, step2_2, on='dishes_name', how='left')

# 表3将菜名-购买量联系起来了，保留需要的列
step4 = step3.loc[:, ['dishes_name', 'amounts']]

print("最受欢迎前十名的价格：")
print(step4)

step2 = step2.drop_duplicates(subset='dishes_name', keep='first', inplace=False)

# 频率分布直方图
step2.amounts.plot.hist(bins=10,edgecolor='black')

# 折线图
# for i in[0,1,2,3,4,5,6,7,8,9]:
# # for i in [0]:
#     mp.axhline(y=50-5*i)
#     mp.plot(x[i],50-5*i, '*r', markersize=15)
#     show_max = 'No.'+str(int(y[i]/5)) +str(ylabels[i]) + str(x[i]) +'元'
#     mp.annotate(show_max, xytext=(x[i]+1.5, 50.5-5*i), xy=(x[i], 50-5*i))
# mp.show()

x = np.array(step4.amounts).ravel()
y=[5,10,15,20,25,30,35,40,45,50]
ylabels = np.array(step4.dishes_name)
yticks=['89',10,15,20,30,35,40,45,50,55]
print(x)
print(y)

###########################################################3
# 标记文字
# 1
mp.plot(x[0], 50 , '*r', markersize=15)
show_max = 'No.' + str(int(y[0] / 5)) + str(ylabels[0]) + str(x[0]) + '元'
mp.annotate(show_max, xytext=(x[0]-5, 51.5), xy=(x[0], 50 - 5 * 0))
# 2
mp.plot(x[1], 20, '*r', markersize=15)
show_max = 'No.' + str(int(y[1] / 5)) + str(ylabels[1]) + str(x[1]) + '元'
mp.annotate(show_max, xytext=(x[1]-1.5, 21.5), xy=(x[1], 20))
# 3
mp.plot(x[2], 3, '*r', markersize=15)
show_max = 'No.' + str(int(y[2] / 5)) + str(ylabels[2]) + str(x[2]) + '元'
mp.annotate(show_max, xytext=(x[2] - 1.5, 3), xy=(x[2], 3))
# 4
mp.plot(x[3], 50, '*r', markersize=15)
show_max = 'No.' + str(int(y[3] / 5)) + str(ylabels[3]) + str(x[3]) + '元'
mp.annotate(show_max, xytext=(x[3] + 1.5, 49), xy=(x[3], 50))
# 5
mp.plot(x[4], 36, '*r', markersize=15)
show_max = 'No.' + str(int(y[4] / 5)) + str(ylabels[4]) + str(x[4]) + '元'
mp.annotate(show_max, xytext=(x[4] + 1.5, 36), xy=(x[4], 36))
# 6
mp.plot(x[5], 4, '*r', markersize=15)
show_max = 'No.' + str(int(y[5] / 5)) + str(ylabels[5]) + str(x[5]) + '元'
mp.annotate(show_max, xytext=(x[5] - 31, 5), xy=(x[5], 4))
# 7
mp.plot(x[6], 20, '*r', markersize=15)
show_max = 'No.' + str(int(y[6] / 5)) + str(ylabels[6]) + str(x[6]) + '元'
mp.annotate(show_max, xytext=(x[6] - 1.5, 17), xy=(x[6], 20))
# 8
mp.plot(x[7], 6, '*r', markersize=15)
show_max = 'No.' + str(int(y[7] / 5)) + str(ylabels[7]) + str(x[7]) + '元'
mp.annotate(show_max, xytext=(x[7] - 1.5, 6), xy=(x[7], 6))
# 9
mp.plot(x[8], 20, '*r', markersize=15)
show_max = 'No.' + str(int(y[8] / 5)) + str(ylabels[8]) + str(x[8]) + '元'
mp.annotate(show_max, xytext=(x[8] - 1.5, 15), xy=(x[8], 20))
# 10
mp.plot(x[9], 20, '*r', markersize=15)
show_max = 'No.' + str(int(y[9] / 5)) + str(ylabels[9]) + str(x[9]) + '元'
mp.annotate(show_max, xytext=(x[9] + 3, 19.5), xy=(x[9], 20))

mp.title('前十名的价格区间分布')
mp.show()
