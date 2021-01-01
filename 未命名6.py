# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:41:01 2020

@author: zhangyonghuihui
"""
import pandas as pd
df = pd.read_excel('studentscore.xlsx', dtype={'code': 'str'}) 
df["总分"]=df.语文+df.数学+df.英语+df.体育+df.美术
df["均分"]=df.总分/5
df.to_csv("studenscore.csv")
df1=df[df.均分>90]
df1=df1[["学号","姓名"]]
print("平均成绩超过90分")
print("--------------")
print(df1)
print("--------------")
m=df.数学.mean()
print("数学成绩不足平均分")
df3=df[df.数学>m]
df3=df3[["学号","姓名"]]
print("--------------")
print(df3)
print("--------------")
df=df.sort_values("总分",ascending=False)
print("--------------")
print(df)
print("--------------")