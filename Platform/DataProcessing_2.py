"""
@software: PyCharm
@file: DataProcessing_2.py
@time: 2020年10月16日21:57:58
@Desc：将分类后的客户信息进行整理
"""
import pandas as pd
import numpy as np
import RandomName as RName
data = pd.read_csv(r'.\\people_no_name\\people_5_1.csv')
print(data.columns)#获取列索引值
print(data.columns.size)
print(data.iloc[:,0].size)#行数
row = data.iloc[:,0].size
data1 = data['飞行次数']#获取列名为flow的数据作为新列的数据
print(type(data1))
name = []
while row>0:
    new_name = RName.random_name()
    name.append(new_name)
    row = row - 1
data['姓名'] = name
data['入会时间'] = data['入会时间'].map(lambda x:int(x))
data['飞行次数'] = data['飞行次数'].map(lambda x:int(x))
data['平均每公里票价'] = data['平均每公里票价'].map(lambda x:float('%.2f'%x))
data['总里程'] = data['总里程'].map(lambda x:int(x))
data['时间间隔差值'] = data['时间间隔差值'].map(lambda x:int(x))
data['平均折扣率'] = data['平均折扣率'].map(lambda x:float('%.2f'%x))
data.rename(columns={'Unnamed: 0':'编号','入会时间':'入会时间(天)','时间间隔差值':'时间间隔差值(天)'},inplace=True)
print(data.columns)#获取列索引值
print(data[0:10])
print(type(data))
name = data['姓名']
data.drop(labels=['姓名'],axis=1,inplace=True)
data.insert(1,'姓名',name)
print(data[0:10])
data.to_excel('.\\people_name\\people_5_2.xlsx',index=False)