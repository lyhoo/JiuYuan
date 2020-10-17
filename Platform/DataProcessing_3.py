"""
@software: PyCharm
@file: DataProcessing_3.py
@time: 2020年10月16日22:03:12
@Desc：从数据库读取航线信息
"""
import pandas as pd
import numpy as np
import pymysql
import ChineseSort as CSort

#数据库操作
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='lyhoo..',
    database='flight',
    charset='utf8'
)
# 获取一个光标
cursor = conn.cursor()
def get_scity():
    sql = 'select flight_scity from flight_info'
    cursor.execute(sql)
    scity = []
    alldata = cursor.fetchall()
    for s in alldata:
        x = list(s)
        scity.append(x[0])
    # print(scity)
    #删除重复元素
    scity.sort()
    t = scity[-1]
    for i in range(len(scity)-2,-1,-1):
    	if t == scity[i]:
    		# del line_list[i]
    		scity.remove(scity[i])
    	else:
    		t = scity[i]
    # print(scity)
    new_airline = CSort.cnsort(scity)
    return new_airline


def get_ecity():
    sql = 'select flight_ecity from flight_info'
    cursor.execute(sql)
    ecity = []
    alldata = cursor.fetchall()
    for s in alldata:
        x = list(s)
        ecity.append(x[0])
    # print(ecity)

    #删除重复元素
    ecity.sort()
    t = ecity[-1]
    for i in range(len(ecity)-2,-1,-1):
    	if t == ecity[i]:
    		# del line_list[i]
    		ecity.remove(ecity[i])
    	else:
    		t = ecity[i]
    # print(ecity)
    ecity = CSort.cnsort(ecity)
    return ecity

def get_air():
    sql = 'select flight_sairport from flight_info'
    cursor.execute(sql)
    sairport = []
    alldata = cursor.fetchall()
    for s in alldata:
        x = list(s)
        sairport.append(x[0])
    # print(sairport)
    # 删除重复元素
    sairport.sort()
    t = sairport[-1]
    for i in range(len(sairport) - 2, -1, -1):
        if t == sairport[i]:
            # del line_list[i]
            sairport.remove(sairport[i])
        else:
            t = sairport[i]
    # print(sairport)
    sairport = CSort.cnsort(sairport)
    return sairport

def query_airline(scity,ecity):
    sql = 'select * from flight_info where flight_scity="'+scity+'" and flight_ecity="'+ecity+'"'
    print(sql)
    cursor.execute(sql)
    airline = []
    alldata = cursor.fetchall()
    for s in alldata:
        x = list(s)
        airline.append(x)
    print(airline)
    return airline

def query_airport(airport):
    sql = 'select * from flight_info where flight_sairport="'+airport+'" '
    print(sql)
    cursor.execute(sql)
    airline = []
    alldata = cursor.fetchall()
    for s in alldata:
        x = list(s)
        airline.append(x)
    print(airline)
    return airline

