# 3.频数统计，最受欢迎的菜
# 1. 统计最受欢迎的菜的前十名，去除米饭的影响

from problem1 import data

import pandas as pd
import matplotlib.pyplot as mp

# 画图中显示中文不出错
mp.rcParams['font.sans-serif'] = ['KaiTi']
mp.rcParams['font.serif'] = ['KaiTi']

# problem2只需要对菜名（dishes_id、dishes_name）、受欢迎程度（counts）、价格（amounts）进行分析
step0 = data.loc[:, ['dishes_id', 'counts', 'amounts']]

# 去除单元格中的空格
step0.replace('\s+', '', regex=True, inplace=True)

####################################################################################
# 1. 统计最受欢迎的菜的前十名，去除米饭的影响
# 按照菜品id分组
step1 = step0.groupby('dishes_id').groups

# 统计菜品的总数
# step2=data.groupby('dishes_name').agg('count') #不用名称，因为有一些回车符号等
step2 = step0.groupby('dishes_id').agg({'counts': 'sum', 'amounts': 'sum'})

# 剔除米饭
# step3 = step2.drop(index=['610011', '610010'])

# 根据菜品总数排序
step4 = step2.sort_values(by='counts', ascending=False)

# 2. 并将最受欢迎的菜品可视化，通过柱状图和折线图展现
# 按照找前10个的菜品id（同一个id可能对应多个name）——（前十个id-购买量）的表
step5 = step4.iloc[2:12, :]

# 所有菜品对应的id——（id-菜名）的表
step5_2 = data.loc[:, ['dishes_id', 'dishes_name']]

# 将（前十个id-购买量-总金额）的表和（id-菜名）的表进行左外连接/内连得到新的表6
step6 = pd.merge(step5, step5_2, on='dishes_id', how='left')

# 表6将菜名-购买量联系起来了，此时中间量菜品id无用，需要剔除
step7 = step6.loc[:, ['dishes_name', 'counts', 'amounts']]

# 左外连接产生了重复行，需要剔除
step8 = step7.drop_duplicates(subset='dishes_name', keep='first', inplace=False)

# 设置DataFrame的序号为dishes_name，方便后面作图的时候可以将索引设置为x坐标轴
step8.index = step8.dishes_name

# 由于序号为菜名了，那么DataFrame列名中的菜名就冗余了，剔除
step9 = step8.loc[:, ['counts', 'amounts']]

# 重新设置DataFrame的列名称，方便自己查看，方便展示在图上的图例
step9.columns = ['all_counts', 'all_amounts']
# print("1.统计最受欢迎的菜的前十名，去除米饭的影响，结果如下：")
# print(step9)
