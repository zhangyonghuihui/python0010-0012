import pandas as pd
df = pd.read_csv('2018世界杯球队数据.csv',encoding='GBK')
df["净胜球"]=df.进球-df.失球
df_i=df[df.净胜球>0]
df_i=df_i[["球队","净胜球"]]
print(df_i)
print('-----------------')
df_j=df[df.红牌>0]
df_j=df_j[["球队","红牌"]]
print(df_j)
print('-----------------')
df["进球成功率"]=df.进球/df.射门
df_k=df[df.进球成功率>0.1]
df_k=df_k[["球队","进球成功率"]]
print(df_k)
print('-----------------')
l=df.进球.mean()
df_l=df[df.进球>l]
df_l=df[df.黄牌<5]
df_l=df_l[["球队","进球","黄牌"]]
print(df_l)
print('-----------------')
df_m=df.sort_values(by="进球" ,ascending=False)
df_m=df_m[["球队","进球"]]
print(df_m)
print('-----------------')
df_n=df.groupby('所属洲')['进球'].sum()
df_n=df_n.sort_values()
print(df_n)
print('-----------------')



