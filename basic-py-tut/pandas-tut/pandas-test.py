import pandas as pd
import matplotlib.pyplot as plt

'''
根据某一列进行groupby,然后画图,工作中画图的需求达到。
'''
path = r'/pandas-tut/data/student.csv'
df = pd.read_csv(path, sep=',')
gp = df.groupby(df['name'])

plt.clf()
for name, value in gp:
    df_sep = value
    x = df_sep['x']
    y = df_sep['y']
    plt.plot(x, y)
plt.show()


