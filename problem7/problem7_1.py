# 7.订单平均消费统计
# 1. 分组统计订单消费总额/订单消费菜品数量

from problem5.problem5_1 import step2 as problem5_ans
from problem6.problem6_1 import step1 as problem6_ans

import pandas as pd

ans7 = pd.DataFrame()
ans7['purchase_per_counts'] = problem6_ans['purchase'] / problem5_ans['counts']
