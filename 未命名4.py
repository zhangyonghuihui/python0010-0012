# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:36:53 2020

@author: zhangyonghuihui
"""
import pandas as pd
import numpy as np
np.random.seed(7)
dates = pd.date_range('2019-1-1', '2019-12-31', freq='B')
df = pd.DataFrame(np.random.uniform(-0.1, 0.1, len(dates)), index=dates,columns=['rate'])
for x in ['2019-1-1', '2019-5-1', '2019-10-1']:
    if x in df.index:
        df.drop(pd.to_datetime(x), inplace=True)
df['percent'] = df['rate'] + 1
yearrate = df['percent'].prod()
print('全年涨跌幅为:{:.2%}'.format(yearrate - 1))
mrate = df.resample('1m')['percent'].prod()
print('全年按月份涨跌幅如下:\n', (mrate - 1).apply(lambda x: format(x, '.2%')))
s = (mrate - 1).sort_values()
print('跌幅最大的月份是:', str(s.index[0])[:7])
print('涨幅最大的月份是:', str(s.index[-1])[:7])

