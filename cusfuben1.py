import pandas as pd
from datetime import date

input_file = 'D:\桌面\py\进阶\customer\customer.csv'
output_file = 'D:\桌面\py\进阶\customer\cus1.csv'

df = pd.read_csv(input_file)
today = pd.to_datetime(date.today())
names = df['Customer'].unique()
caters = []
cat = ['Bronze','Silver','Gold']
df = df.set_index(['Customer','Category'])

for name in names:
    caters.append(df.loc[name].index[-1])

date_min = pd.to_datetime((df.groupby(['Customer','Category'],sort=False).min()['Date']))
date_frame1 = today - date_min

for i,j in df.index:
    biggest = zip(names, caters)
    if list(df.index).count((i,j)) == 1 and (i,j) not in biggest:
        x = cat.index(j) + 1
        y = cat[x]
        date_frame1.loc[(i, j)] = date_min.loc[(i,y)] - date_min.loc[(i,j)]
    elif list(df.index).count((i,j)) > 1 and (i,j) not in biggest:
        x = cat.index(j) + 1
        y = cat[x]
        date_frame1.loc[(i, j)] = date_min.loc[(i, y)] - date_min.loc[(i, j)]

df1 = date_frame1.reset_index()
df1.columns = ['Customer','Category','Total Time']

print(df1)
# df1.to_csv(output_file,index=False)