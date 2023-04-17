# coding:utf-8
import pandas as pd

# 读取指定文件的指定sheet
df1 = pd.read_excel(r'C:\Users\user\Desktop\py\exam1\meal_order_detail.xlsx', header=0, sheet_name=0)
df2 = pd.read_excel(r'C:\Users\user\Desktop\py\exam1\meal_order_detail.xlsx', header=0, sheet_name='meal_order_detail2')
df3 = pd.read_excel(r'C:\Users\user\Desktop\py\exam1\meal_order_detail.xlsx', header=0, sheet_name='meal_order_detail3')


# 按行拼接
data = pd.concat([df1, df2, df3], sort=False, ignore_index=True)

# 选择需要的列
header = ['detail_id','order_id','dishes_id','dishes_name','counts','amounts','place_order_time','emp_id']
data = data.loc[:, header]
print(data.dtypes)

# 去除na
data=data.drop_duplicates()

# # 去除单元格的空格
# data = data.applymap(lambda x: str(x).strip())

print(data.dtypes)

