"""
@software: PyCharm
@file: SpiderFlightline.py
@time: 2020年10月16日21:53:29
@Desc：实现全国所有航线的爬取
"""
import random
import requests
from bs4 import BeautifulSoup
import userAgents as uA
import pymysql
import time
# 航线爬取

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

# 得到所有地方航班及链接
def getAllFlights():
    flights = {}  # {'安庆航班': 'https://flights.ctrip.com/schedule/aqg..html', ...}
    url = 'https://flights.ctrip.com/schedule'
    headers = {
        'user-agent': random.choice(uA.UserAgents),
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'upgrade-insecure-requests': '1'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    letter_list = soup.find(attrs={'class': 'letter_list'}).find_all('li')
    for li in letter_list:
        for a in li.find_all('a'):
            flights[a.get_text()] = url + a['href'][9:]
    return flights

# 得到一个地方航班的所有线路
def getFlightLines(url):
       flightlines = {}   # {'安庆-北京': 'http://flights.ctrip.com/schedule/aqg.bjs.html', ...｝
       headers = {
           'Referer': 'https://flights.ctrip.com/schedule/',
           'user-agent':random.choice(uA.UserAgents)
       }
       response = requests.get(url, headers=headers)
       soup = BeautifulSoup(response.text, 'lxml')
       if soup.find(attrs={'id': 'ulD_Domestic'})!=None:
        letter_list = soup.find(attrs={'id': 'ulD_Domestic'}).find_all('li')
        for li in letter_list:
           for a in li.find_all('a'):
                # scity = a.get_text().split('-')[0]
                # ecity = a.get_text().split('-')[1]
                # fsql = 'insert into flight(flight_name,scity,ecity) values("%s","%s","%s")' % (a.get_text(),scity,ecity)
                # cursor.execute(fsql)
                # conn.commit()
                # print(a.get_text())
                # print("sql success!")
                flightlines[a.get_text()] = a['href']

       return flightlines

# 得到这条线路的所有航班信息
def getFlightInfo(url):
    flightInfos = []
    headers = {
        'Host': 'flights.ctrip.com',
        'user-agent': random.choice(uA.UserAgents)
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    flights_tr = soup.find(attrs={'id':'flt1'}).find_all('tr')
    for tr in flights_tr:        # 遍历每个一航班
        flightInfo = {}
        info_td = tr.find_all('td')
        # 航班编号
        flight_no = info_td[0].find('strong').get_text().strip()
        flightInfo['flight_no'] = flight_no
        # 起飞时间
        flight_stime = info_td[1].find('strong').get_text().strip()
        flightInfo['flight_stime'] = flight_stime
        # 起飞机场
        flight_sairport = info_td[1].find('div').get_text().strip()
        flightInfo['flight_sairport'] = flight_sairport
        # 降落时间
        flight_etime = info_td[3].find('strong').get_text().strip()
        flightInfo['flight_etime'] = flight_etime
        # 降落机场
        flight_eairport = info_td[3].find('div').get_text().strip()
        flightInfo['flight_eairport'] = flight_eairport
        # 班期
        flight_schedule = []
        for s in info_td[4].find(attrs={'class':'week'}).find_all(name='span', attrs={'class':'blue'}):
            flight_schedule.append(s.get_text().strip())
        flight_schedule = ' '.join( flight_schedule )
        flightInfo['flight_schedule'] = flight_schedule
        # 准点率
        flight_punrate = info_td[5].get_text().strip()
        flightInfo['flight_punrate'] = flight_punrate
        # 价格
        flight_price = info_td[6].get_text().strip()
        flightInfo['flight_price'] = flight_price

        flightInfos.append(flightInfo)
    return flightInfos

#返回最后插入数据的索引
def returnLastInsertId(self):
    sql = 'SELECT LAST_INSERT_ID()'
    self.cursor.execute(sql)
    index = self.cursor.fetchone()
    #self.conn.close()
    #print(type(index[0]))


if __name__ == '__main__':
    allFlights = getAllFlights()
    for flight in allFlights.keys():
        # fsql = 'insert into flight(flight_name) values("%s")' % flight
        # cursor.execute(fsql)
        #lastId = int(returnLastInsertId())
        flightLines = getFlightLines(allFlights[flight])
        # time.sleep(random.randint(1,3))
        for line in flightLines.keys():
            print('正在获取',flight,'的',line,'线路...')
            flight_scity = line.split('-')[0]
            flight_ecity = line.split('-')[1]
            flightInfos = getFlightInfo(flightLines[line])
            for flightInfo in flightInfos:
                fisql = 'insert into flight_info(flight_destination,flight_no,flight_stime,flight_etime,flight_sairport,'\
                        'flight_eairport,flight_schedule,flight_punrate,flight_price,flight_scity,flight_ecity)' \
                        'values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'\
                        % (line,flightInfo['flight_no'],flightInfo['flight_stime'],
                           flightInfo['flight_etime'],flightInfo['flight_sairport'],flightInfo['flight_eairport'],
                           flightInfo['flight_schedule'],flightInfo['flight_punrate'],flightInfo['flight_price'],flight_scity,flight_ecity)
                cursor.execute(fisql)
            conn.commit()
            print('获取成功！')
            # time.sleep(random.randint(15,25))
    conn.colse()
    print('全部获取成功！')

