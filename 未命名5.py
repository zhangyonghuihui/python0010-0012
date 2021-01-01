# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:53:38 2020

@author: zhangyonghuihui
"""
import pandas as pd
import  matplotlib.pyplot  as  plt
df = pd.read_excel('stock.xlsx', dtype={'code': 'str'}) 
df.set_index('code', inplace=True)
c=df.groupby('area').area.count().sort_values(ascending=False)
print(c)
year = df.timeToMarket.astype('str').str[:4]
yearnum = df.groupby(year).name.count()	
plt.rcParams['font.sans-serif'] = ['SimHei']
yearnum[yearnum.index!='0'].plot(fontsize=14, title='年IPO数量')
#---------------------------------------
'''
df=df.sort_values("code")
sz=df[[df.index[i][:2]=="00" for i in range (df.index.__len__())]]
hs=df[[df.index[i][:2]=="60" for i in range (df.index.__len__())]]
cy=df[[df.index[i][:2]=="30" for i in range (df.index.__len__())]]
kc=df[[df.index[i][:2]=="68" for i in range (df.index.__len__())]]
print("深圳主板pe值")
print(sz[sz.pe > 0].pe.mean())
print("------------------------")
print("沪市pe值")
print(sz[sz.pe > 0].pe.mean())
print("------------------------")
print("创业板pe值")
print(sz[sz.pe > 0].pe.mean())
print("------------------------")
print("科创板pe值")
print(sz[sz.pe > 0].pe.mean())
print("------------------------")
'''
df['board'] = df.index.str[:2]  
cc=df.groupby('board').pe.agg([('pe均值', 'mean'), ('股票数', 'count')])
print(cc)

