import pandas as pd
from readfromexcel import data
# 将结果写到值得excel文件
data.to_excel(r'C:\Users\user\Desktop\py\exam1\result.xlsx', index=False)

# 读取表格
file = r'C:\Users\user\Desktop\py\exam1\result.xlsx'
data = pd.read_excel(file)
print(data)

