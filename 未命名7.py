import  matplotlib.pyplot  as  plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  
plt.rcParams['axes.unicode_minus'] = False 
df = pd.read_excel('studentscore.xlsx', dtype={'code': 'str'}) 
del df["学号"]
df.boxplot()



