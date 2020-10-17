"""
@software: PyCharm
@file: app.py
@time: 2020年10月16日21:46:56
@Desc：实现平台中的具体功能
"""
from DAP import Ui_MainWindow
from airline_information import Ui_Dialog
import sys
import xlrd
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication,QHBoxLayout,QAction,QTableWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QColor, QFont
import pandas as pd
import numpy as np
import DataProcessing_3 as air_line
# import qtawesome

peopleList = ['重要客户','重要保持客户','季节性客户','重点挽留客户','低价值客户']
airlineList1 = []
airlineList2 = []

# 用户表格数据的显示
def people_list(self,type):
    ###===========读取表格，转换表格，===========================================
    if 1:
        input_table = pd.read_excel('./people/'+type+'.xlsx')
        input_table_rows = input_table.shape[0]
        input_table_colunms = input_table.shape[1]
        input_table_header = input_table.columns.values.tolist()

        ###===========读取表格，转换表格，============================================
        ###======================给tablewidget设置行列表头============================

        self.setColumnCount(input_table_colunms)
        self.setRowCount(input_table_rows)
        self.setHorizontalHeaderLabels(input_table_header)

        ###======================给tablewidget设置行列表头============================

        ###================遍历表格每个元素，同时添加到tablewidget中========================
        for i in range(input_table_rows):
            input_table_rows_values = input_table.iloc[[i]]
            input_table_rows_values_array = np.array(input_table_rows_values)
            input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            for j in range(input_table_colunms):
                input_table_items_list = input_table_rows_values_list[j]

                ###==============将遍历的元素添加到tablewidget中并显示=======================

                input_table_items = str(input_table_items_list)
                newItem = QTableWidgetItem(input_table_items)
                newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.setItem(i, j, newItem)
                self.setColumnWidth(0, 150)
                self.setColumnWidth(1, 150)
                self.setColumnWidth(2, 150)
                self.setColumnWidth(3, 150)
                self.setColumnWidth(4, 200)
                self.setColumnWidth(5, 150)
                self.setColumnWidth(6, 200)
                self.setColumnWidth(7, 178)

    ###================遍历表格每个元素，同时添加到tablewidget中========================
    else:
        self.centralWidget.show()



class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icon/flight.png'))
        # 显示航线图
        self.browser = QWebEngineView(self.airlineChart)
        self.browser.setGeometry(QtCore.QRect(0, 0, 1431, 661))
        self.browser.load(
            QUrl("file:///E:/code/python/JiuYuan/render.html"))
        # 用户类型下拉菜单初始化
        for i in peopleList:
            self.peopleBox.addItem(i)
        people_list(self.peopleList,'重要客户')
        # 查看不同类型客户
        self.pushButton.clicked.connect(self.choose_peopletype)
        # 航线查询下拉菜单初始化
        scityList = air_line.get_scity()
        ecityList = air_line.get_ecity()
        airportList = air_line.get_air()
        for i in scityList:
            self.scityBox.addItem(i)
        for i in ecityList:
            self.ecityBox.addItem(i)
        for i in airportList:
            self.comboBox_4.addItem(i)
        # 数据可视化显示
        # chart1
        label = QtWidgets.QLabel(self.chart1)
        label.setGeometry(QtCore.QRect(0, 0, 471, 321))
        png = QtGui.QPixmap('./chart/chart1.png').scaled(label.width(), label.height())
        label.setPixmap(png)
        # chart2
        self.browser = QWebEngineView(self.chart2)
        self.browser.load(
            QUrl("file:///./chart/1.html"))
        # chart3
        self.browser = QWebEngineView(self.chart3)
        self.browser.load(
            QUrl("file:///./chart/2.html"))
        # chart4
        self.browser = QWebEngineView(self.chart4)
        self.browser.load(
            QUrl("file:///./chart/3.html"))
        # chart5
        self.browser = QWebEngineView(self.chart5)
        self.browser.load(
            QUrl("file:///./chart/4.html"))
        # chart6
        self.browser = QWebEngineView(self.chart6)
        self.browser.load(
            QUrl("file:///./chart/5.html"))


        # 按照开始结束城市查找航线
        self.queryButton1.clicked.connect(self.query_airline)
        self.airLineWidget1.doubleClicked.connect(self.airline_table1_change)

        # 按照机场查找航线
        self.queryButton2.clicked.connect(self.query_airport)
        self.airLineWidget2.doubleClicked.connect(self.airline_table2_change)

    #选择显示不同类型的客户
    def choose_peopletype(self):
        type = self.peopleBox.currentText()
        people_list(self.peopleList,type)

    #按照城市进行查找
    def query_airline(self):
        scity = self.scityBox.currentText()
        ecity = self.ecityBox.currentText()
        global airlineList1
        airlineList1 = air_line.query_airline(scity,ecity)
        if len(airlineList1)==0:
            self.airLineWidget1.setColumnCount(1)
            self.airLineWidget1.setRowCount(1)
            self.airLineWidget1.setHorizontalHeaderLabels([''])
            self.airLineWidget1.setColumnWidth(0, 540)
            font = QtGui.QFont()
            font.setFamily("Adobe 黑体 Std R")
            font.setPointSize(12)
            self.airLineWidget1.setFont(font)
            newItem1 = QTableWidgetItem("无此类数据，请重新查询！")
            newItem1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            newItem1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.airLineWidget1.setItem(0, 0, newItem1)
        else:
            self.airLineWidget1.setColumnCount(3)
            self.airLineWidget1.setRowCount(len(airlineList1))
            self.airLineWidget1.setHorizontalHeaderLabels(['航班号', '起飞时间', '到达时间'])
            self.airLineWidget1.setColumnWidth(0, 180)
            self.airLineWidget1.setColumnWidth(1, 180)
            self.airLineWidget1.setColumnWidth(2, 180)
            font = QtGui.QFont()
            font.setFamily("Adobe 黑体 Std R")
            font.setPointSize(12)
            self.airLineWidget1.setFont(font)
            n = 0
            for i in airlineList1:
                newItem1 = QTableWidgetItem(i[2])
                newItem2 = QTableWidgetItem(i[3])
                newItem3 = QTableWidgetItem(i[4])
                newItem1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                newItem2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                newItem3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                newItem1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                newItem2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                newItem3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.airLineWidget1.setItem(n, 0, newItem1)
                self.airLineWidget1.setItem(n, 1, newItem2)
                self.airLineWidget1.setItem(n, 2, newItem3)
                n = n + 1
        print(airlineList1)

    #按照机场进行查询
    def query_airport(self):
        sairport = self.comboBox_4.currentText()
        global airlineList2
        airlineList2 = air_line.query_airport(sairport)
        self.airLineWidget2.setColumnCount(4)
        self.airLineWidget2.setRowCount(len(airlineList2))
        print(len(airlineList2))
        self.airLineWidget2.setHorizontalHeaderLabels(['航班号', '航班方向' ,'起飞时间', '到达时间'])
        self.airLineWidget2.setColumnWidth(0, 135)
        self.airLineWidget2.setColumnWidth(1, 135)
        self.airLineWidget2.setColumnWidth(2, 135)
        self.airLineWidget2.setColumnWidth(3, 135)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.airLineWidget2.setFont(font)
        n=0
        for i in airlineList2:
            newItem1 = QTableWidgetItem(i[2])
            newItem2 = QTableWidgetItem(i[3])
            newItem3 = QTableWidgetItem(i[4])
            newItem4 = QTableWidgetItem(i[1])
            newItem1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            newItem2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            newItem3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            newItem4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            newItem1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            newItem2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            newItem3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            newItem4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.airLineWidget2.setItem(n, 0, newItem1)
            self.airLineWidget2.setItem(n, 2, newItem2)
            self.airLineWidget2.setItem(n, 3, newItem3)
            self.airLineWidget2.setItem(n, 1, newItem4)
            n = n + 1
        print(airlineList2)

    #城市查询中显示详细信息
    def airline_table1_change(self, index):
        row = index.row()
        print(airlineList1[row])
        ui1.id.setText(str(airlineList1[row][0]))
        ui1.no.setText(airlineList1[row][2])
        ui1.stime.setText(airlineList1[row][3])
        ui1.etime.setText(airlineList1[row][4])
        ui1.scity.setText(airlineList1[row][10])
        ui1.ecity.setText(airlineList1[row][11])
        ui1.sairport.setText(airlineList1[row][5])
        ui1.eairport.setText(airlineList1[row][6])
        ui1.punrate.setText(airlineList1[row][8])
        if airlineList1[row][9]=='查看时价':
            ui1.price.setText('时价')
        else:
            ui1.price.setText(airlineList1[row][9])
        time = airlineList1[row][7].replace(' ','')
        time1 = ''
        time2 = ''
        for i in time:
            if i=='一':
                time1 = time1 + '一 '
            if i=='二':
                time1 = time1 + '二 '
            if i=='三':
                time1 = time1 + '三 '
            if i=='四':
                time1 = time1 + '四 '
            if i=='五':
                time2 = time2 + '五 '
            if i=='六':
                time2 = time2 + '六 '
            if i=='日':
                time2 = time2 + '日 '
        ui1.week1.setText(time1)
        ui1.week2.setText(time2)
        ui1.show()
        print(row)

    #航线查询中显示详细信息
    def airline_table2_change(self, index):
        row = index.row()
        print(airlineList2[row])
        ui2.id.setText(str(airlineList2[row][0]))
        ui2.no.setText(airlineList2[row][2])
        ui2.stime.setText(airlineList2[row][3])
        ui2.etime.setText(airlineList2[row][4])
        ui2.scity.setText(airlineList2[row][10])
        ui2.ecity.setText(airlineList2[row][11])
        ui2.sairport.setText(airlineList2[row][5])
        ui2.eairport.setText(airlineList2[row][6])
        ui2.punrate.setText(airlineList2[row][8])
        if airlineList2[row][9] == '查看时价':
            ui2.price.setText('时价')
        else:
            ui2.price.setText(airlineList2[row][9])
        time = airlineList2[row][7].replace(' ','')
        time1 = ''
        time2 = ''
        for i in time:
            if i=='一':
                time1 = time1 + '一 '
            if i=='二':
                time1 = time1 + '二 '
            if i=='三':
                time1 = time1 + '三 '
            if i=='四':
                time1 = time1 + '四 '
            if i=='五':
                time2 = time2 + '五 '
            if i=='六':
                time2 = time2 + '六 '
            if i=='日':
                time2 = time2 + '日 '
        ui2.week1.setText(time1)
        ui2.week2.setText(time2)
        ui2.show()
        print(row)

#按照城市显示的航线
class airline_info_1(QDialog,Ui_Dialog):

    def __init__(self,parent=None):
        super(airline_info_1,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icon/flight.png'))

#按照机场显示的航线
class airline_info_2(QDialog,Ui_Dialog):

    def __init__(self,parent=None):
        super(airline_info_2,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icon/flight.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./icon/flight.png'))
    ui = MainWindow()
    ui1 = airline_info_1()
    ui2 = airline_info_2()
    ui.show()
    sys.exit(app.exec_())
