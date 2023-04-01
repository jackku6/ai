import pandas as pd
import numpy as np

df1 = pd.read_excel('283地级市GDP.xlsx',sheet_name='地区生产总值（万元）')
df2 = pd.read_excel('283地级市的欧氏距离.xlsx',sheet_name='283地级市欧式直线距离（千米）')
df3 = pd.read_excel('283地级市的欧氏距离.xlsx',sheet_name='283地级市行政区域面积（平方公里）')

df_2 = df2.pivot_table('d',index='city0',columns='city')
df2 = df2.set_index('city0')
x = df2.index.unique()
df_2 = df_2.reindex(index=x,columns=x)
# print(df_2)

df_area = df3.loc[:,'area']
df5 = df1.loc[:,'gdp'] / ((2.0/3.0) * np.sqrt(df_area/np.pi))
data = []
df_1 = df1.set_index(['year'])
# # print(df_1.index)
# # print(df1.loc[:,'gdp'] / ((2.0/3.0) * np.sqrt(df_area/np.pi)))
for i in range(len(df1.index)):
    j = i % 283
    h = i // 283
    sr = df_2.iloc[j,:]
    df_3 = df_1.loc[(h+2003),:]
    df_3 = df_3[df_3['id1'] != j]
    # df_3 = df_3.reset_index()
    # print(sr[sr.values != 0])
    df4 = df_3.reset_index()['gdp'] / sr[sr.values != 0].reset_index().iloc[:,1]
    # print(df_3['gdp'].reset_index())
    mpi = df4.sum() + df5[i]
    data.append(mpi)

mpi_sr = pd.Series(data=data)
df1['mpi'] = mpi_sr

file_writer = pd.ExcelWriter('mpi.xlsx')
df1.to_excel(file_writer,index=False)
file_writer.close()
