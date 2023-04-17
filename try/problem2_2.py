import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
from problem1 import data
mp.rcParams["font.sans-serif"] = 'SimHei'
mp.rcParams['axes.unicode_minus'] = False
# %config InlineBackend.figure_format='svg'

data.counts.plot.hist(bins=10)
mp.show()
