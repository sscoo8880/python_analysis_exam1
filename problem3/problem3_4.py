# 3.频数统计，最受欢迎的菜
# 4. 统计最受欢迎的菜品前十名的平均价格，中位数，四分位数
import pandas as pd

from problem1 import data
from problem3_1 import step9

# 所有菜品对应的价格——（菜名-价格）的表
step1 = data.loc[:, ['dishes_name', 'amounts']]

# 重复行需要剔除
step1_2 = step1.drop_duplicates(subset='dishes_name', keep='first', inplace=False)

# 将（前十个菜名）的表和（菜名-价格）的表进行左外连接得到新的表3
step2 = pd.merge(step9, step1_2, on='dishes_name', how='left')

# 表3将菜名-购买量联系起来了，保留需要的列
step3 = step2.loc[:, ['dishes_name', 'amounts']]
print(step3)
# 平均价格，中位数，四分位数
ans1 = step3.amounts.mean()
ans2 = step3.amounts.median()
ans3 = step3.quantile(q=0.25, axis=0, numeric_only=True, interpolation='linear')
print(ans1)
print(ans2)
print(ans3)
