# 1.认识数据并预处理
# 1. 读取execl数据，execl表格存放了8月份整月的数据，分别存放在不同的sheet页中，将数据进行完整的整合。
# 2. 数据预处理，提取页面中需要的列数据，去除不需要的和NA的数据，保留下有用的数
# coding:utf-8
import pandas as pd

#####################################################################################################
# 1. 读取execl数据，execl表格存放了8月份整月的数据，分别存放在不同的sheet页中，将数据进行完整的整合。
# 读取指定文件的指定sheet
df1 = pd.read_excel(r'C:\Users\user\Desktop\py\exam1\meal_order_detail.xlsx', header=0, sheet_name='meal_order_detail1')
df2 = pd.read_excel(r'C:\Users\user\Desktop\py\exam1\meal_order_detail.xlsx', header=0, sheet_name='meal_order_detail2')
df3 = pd.read_excel(r'C:\Users\user\Desktop\py\exam1\meal_order_detail.xlsx', header=0, sheet_name='meal_order_detail3')

# 按行拼接
data = pd.concat([df1, df2, df3], sort=False, ignore_index=True)


#####################################################################################################
# 2. 数据预处理，提取页面中需要的列数据，去除不需要的和NA的数据，保留下有用的数据
# 选择需要的列(去除不需要的列)
header = ['detail_id', 'order_id', 'dishes_id', 'dishes_name', 'counts', 'amounts', 'place_order_time', 'emp_id']
data = data.loc[:, header]

# 去除NA
data.drop_duplicates()

# 去除单元格中的空格
data.replace('\s+', '', regex=True, inplace=True)

# 结果写入problem1.xlsx
# data.to_excel(r'C:\Users\user\Desktop\py\exam1\problem1.xlsx', index=False)
