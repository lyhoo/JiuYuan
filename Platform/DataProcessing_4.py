"""
@software: PyCharm
@file: DataProcessing_4.py
@time: 2020年10月16日22:04:07
@Desc：计算用户各种数据的平均值
"""
import pandas as pd
import numpy as np
import pymysql

data1 = pd.read_excel(r'C:\\Users\\lyhoo\\Desktop\\重要客户.xlsx')
data2 = pd.read_excel(r'C:\\Users\\lyhoo\\Desktop\\重要保持客户.xlsx')
data3 = pd.read_excel(r'C:\\Users\\lyhoo\\Desktop\\季节性客户.xlsx')
data4 = pd.read_excel(r'C:\\Users\\lyhoo\\Desktop\\重点挽留客户.xlsx')
data5 = pd.read_excel(r'C:\\Users\\lyhoo\\Desktop\\低价值客户.xlsx')
#
all_km_mean = []
all_km_mean1 = data1['总里程'].mean()
all_km_mean2 = data2['总里程'].mean()
all_km_mean3 = data3['总里程'].mean()
all_km_mean4 = data4['总里程'].mean()
all_km_mean5 = data5['总里程'].mean()

all_km_mean1 = float('%.2f'%all_km_mean1)
all_km_mean2 = float('%.2f'%all_km_mean2)
all_km_mean3 = float('%.2f'%all_km_mean3)
all_km_mean4 = float('%.2f'%all_km_mean4)
all_km_mean5 = float('%.2f'%all_km_mean5)
all_km_mean.append(all_km_mean1)
all_km_mean.append(all_km_mean2)
all_km_mean.append(all_km_mean3)
all_km_mean.append(all_km_mean4)
all_km_mean.append(all_km_mean5)
print(all_km_mean)
#
flight_time_mean = []
flight_time_mean1 = data1['飞行次数'].mean()
flight_time_mean2 = data2['飞行次数'].mean()
flight_time_mean3 = data3['飞行次数'].mean()
flight_time_mean4 = data4['飞行次数'].mean()
flight_time_mean5 = data5['飞行次数'].mean()

flight_time_mean1 = int(flight_time_mean1)
flight_time_mean2 = int(flight_time_mean2)
flight_time_mean3 = int(flight_time_mean3)
flight_time_mean4 = int(flight_time_mean4)
flight_time_mean5 = int(flight_time_mean5)
flight_time_mean.append(flight_time_mean1)
flight_time_mean.append(flight_time_mean2)
flight_time_mean.append(flight_time_mean3)
flight_time_mean.append(flight_time_mean4)
flight_time_mean.append(flight_time_mean5)
print(flight_time_mean)
#
price_mean = []
price_mean1 = data1['平均每公里票价'].mean()
price_mean2 = data2['平均每公里票价'].mean()
price_mean3 = data3['平均每公里票价'].mean()
price_mean4 = data4['平均每公里票价'].mean()
price_mean5 = data5['平均每公里票价'].mean()

price_mean1 = float('%.2f'%price_mean1)
price_mean2 = float('%.2f'%price_mean2)
price_mean3 = float('%.2f'%price_mean3)
price_mean4 = float('%.2f'%price_mean4)
price_mean5 = float('%.2f'%price_mean5)
price_mean.append(price_mean1)
price_mean.append(price_mean2)
price_mean.append(price_mean3)
price_mean.append(price_mean4)
price_mean.append(price_mean5)
print(price_mean)
#
discount_mean = []
discount_mean1 = data1['平均折扣率'].mean()
discount_mean2 = data2['平均折扣率'].mean()
discount_mean3 = data3['平均折扣率'].mean()
discount_mean4 = data4['平均折扣率'].mean()
discount_mean5 = data5['平均折扣率'].mean()
discount_mean1 = float('%.2f'%discount_mean1)
discount_mean2 = float('%.2f'%discount_mean2)
discount_mean3 = float('%.2f'%discount_mean3)
discount_mean4 = float('%.2f'%discount_mean4)
discount_mean5 = float('%.2f'%discount_mean5)
discount_mean.append(discount_mean1)
discount_mean.append(discount_mean2)
discount_mean.append(discount_mean3)
discount_mean.append(discount_mean4)
discount_mean.append(discount_mean5)
print(discount_mean)