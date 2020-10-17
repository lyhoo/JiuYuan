"""
@software: PyCharm
@file: DataProcessing_1.py
@time: 2020年10月16日21:57:16
@Desc：统计所有航线数量并绘制航线图
"""
import pymysql
from pyecharts import GeoLines, Style, Page
#航线图
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
# 查询数据库中所有内容
sql = 'select scity,ecity from flight'
cursor.execute(sql)
line_list = []
alldata = cursor.fetchall()
for s in alldata:
    x = list(s)
    line_list.append(x)
print(line_list)
#删除重复元素
line_list.sort()
t = line_list[-1]
for i in range(len(line_list)-2,-1,-1):
	if t == line_list[i]:
		# del line_list[i]
		line_list.remove(line_list[i])
	else:
		t = line_list[i]
print(line_list)

hefei = []
haikou = []

beijing = []
shanghai = []
guangzhou = []
chongqing = []
zhengzhou = []
wuhan = []
haerbin = []
for s in line_list:
    if s[0] == '合肥':
        hefei.append(s)
    if s[0] == '海口':
        haikou.append(s)

    if s[0] == '北京':
        beijing.append(s)
    if s[0] == '上海':
        shanghai.append(s)
    if s[0] == '广州':
        guangzhou.append(s)
    if s[0] == '重庆':
        chongqing.append(s)
    if s[0] == '郑州':
        zhengzhou.append(s)
    if s[0] == '武汉':
        wuhan.append(s)
    if s[0] == '哈尔滨':
        haerbin.append(s)
print(hefei)
print(haerbin)
print(haikou)
# 插入分割后内容
# sql = 'insert into userinfo(user,pwd) values(%s,%s);'
# data = [
#     ('july', '147'),
#     ('june', '258'),
#     ('marin', '369')
# ]
# 拼接并执行sql语句
# cursor.executemany(sql, data)

# 涉及写操作要注意提交
conn.commit()

# 关闭连接
cursor.close()
conn.close()

#绘制航线图
style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1410,
    height=640,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,                                 #轨迹线的弯曲度，0-1
    line_opacity=0.6,                               #轨迹线的透明度，0-1
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",                      #特效的图形，有circle,plane,pin等等
    geo_effect_symbolsize=15,                       #特效图形的大小
    geo_effect_color='#ffffff',                     # 特效的颜色
    # geo_effect_traillength=0.1,                     # 特效图形的拖尾效果，0-1
    label_color=['#a6c84c', '#ffa022', '#46bee9','#FFEBCD','#FF4500','#9F79EE','#9BCD9B',],  #轨迹线的颜色，标签点的颜色
    label_pos="right",
    label_formatter="{b}",                          #标签格式
    label_text_color="#eee",
    border_color='#97FFFF',                         #边界的颜色
    geo_normal_color='#36648B',                     #地图的颜色

)

def create_charts():
    page = Page()

    # data_guangzhou = [
    #     ["广州", "上海"],
    #     ["广州", "北京"],
    #     ["广州", "南京"],
    #     ["广州", "重庆"],
    #     ["广州", "兰州"],
    #     ["广州", "杭州"]
    # ]
    # data_beijing = [
    #     ["北京", "上海"],
    #     ["北京", "广州"],
    #     ["北京", "南京"],
    #     ["北京", "重庆"],
    #     ["北京", "兰州"],
    #     ["北京", "杭州"]
    # ]

    # charts = GeoLines("GeoLines-默认示例", **style.init_style)
    # charts.add("从广州出发", data_guangzhou, is_legend_show=False)
    # page.add(charts)
    #
    # charts = GeoLines("GeoLines-稍加配置", **style.init_style)
    # charts.add("从广州出发", data_guangzhou, **style_geo)
    # page.add(charts)
    #
    charts = GeoLines("", **style.init_style)
    # charts.add("从合肥出发", hefei, **style_geo)
    # charts.add("从哈尔滨出发", haerbin, **style_geo)
    # charts.add("从海口出发", haikou, **style_geo)
    # charts.add("全部", line_list, **style_geo)

    charts.add("从北京出发", beijing, **style_geo)
    charts.add("从上海出发", shanghai, **style_geo)
    charts.add("从广州出发", guangzhou, **style_geo)
    charts.add("从重庆出发", chongqing, **style_geo)
    charts.add("从郑州出发", zhengzhou, **style_geo)
    charts.add("从武汉出发", wuhan, **style_geo)
    charts.add("从哈尔滨出发", haerbin, **style_geo)
    page.add(charts)

    # charts = GeoLines("全国航线图", **style.init_style)
    # # charts.add("从广州出发", data_guangzhou, **style_geo)
    # charts.add("航线", line_list,
    #            legend_selectedmode="single", **style_geo)
    # page.add(charts)

    return page

create_charts().render()


