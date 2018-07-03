'''
Created on 02.07.2018

@author: gmmar
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
from mysql.connector import Error


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        #Fenster options
        self.adjustSize()
        self.layout = QVBoxLayout(self)
          
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()    
        self.tab2 = QWidget()
        #self.tabs.resize(300,200) 
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Login")
        self.tabs.addTab(self.tab2,"Registrieren")
        
        ###########
        #Tab Login#
        ###########
        self.txtName = QLineEdit(self)
        self.txtPass = QLineEdit(self)
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.username = QLabel("Benutzername")
        self.pw = QLabel("Passwort")
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        
        
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.username)
        self.tab1.layout.addWidget(self.txtName)
        self.tab1.layout.addWidget(self.pw)
        self.tab1.layout.addWidget(self.txtPass)
        self.tab1.layout.addWidget(self.buttonLogin)
        #self.pushButton1 = QPushButton("PyQt5 button")
        #self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        
        ##################
        #Tab Registrieren#
        ##################
        #Combobox
        self.comboBox = QComboBox()
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem("test")
        
        #Combobox fuellen
        cnx = mysql.connector.connect(host='62.108.32.183',
                                      port=3306,
                                      database='aumcfuom_allgemein',
                                      user='aumcf_info2',
                                      password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')

        cursor = cnx.cursor()  
        query= "SELECT rights from members_rights"
        cursor.execute(query)
        
        for i in cursor:
            self.comboBox.addItem(str(i))
        cnx.close()
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')
        
        
        self.rUsername = QLabel("Benutzername")
        self.rPw = QLabel("Passwort")
        self.rPwBe = QLabel("Passwort bestaetigen")
        self.txtRname = QLineEdit(self)
        self.txtRpass = QLineEdit(self)
        self.txtRpassBe = QLineEdit(self)
        self.buttonRegistration = QPushButton('Registration', self)
        self.buttonRegistration.clicked.connect(self.regmember)
        
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.rUsername)
        self.tab2.layout.addWidget(self.txtRname)
        self.tab2.layout.addWidget(self.rPw)
        self.tab2.layout.addWidget(self.txtRpass)
        self.tab2.layout.addWidget(self.rPwBe)
        self.tab2.layout.addWidget(self.txtRpassBe)
        self.tab2.layout.addWidget(self.comboBox)
        self.tab2.layout.addWidget(self.buttonRegistration)
        self.tab2.setLayout(self.tab2.layout)
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)        
        
        @pyqtSlot()
        def on_click(self):
            print("\n")
            for currentQTableWidgetItem in self.tableWidget.selectedItems():
                print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        
        '''
        layout = QVBoxLayout(self)
        layout.addWidget(self.username)
        layout.addWidget(self.txtName)
        layout.addWidget(self.pw)
        layout.addWidget(self.txtPass)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonRegistration)
        '''
    @pyqtSlot()
    def regmember(self):
        print("Registrierung clicked")
        entry=[]

        for xi in range(0,len(self.headerlist)):
            entry.append(self.tablelist[0].item(0,xi).text())
        print(entry)   
        
    def change(self, index):
        print("Change Entry")
        rowlist=[]
        row = index
        #print(row)
        
        for xj in range(0,len(self.headerlist)):
            print(self.tablelist[1].item(row,xj).text())
            if(self.tablelist[1].item(row,xj).text() == None):
                rowlist.append("")
            else:
                rowlist.append(self.tablelist[1].item(row,xj).text())
        print(rowlist)
    
    def handleLogin(self):
        
        if (self.txtName.text() == 'foo' and self.txtPass.text() == 'bar'):
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')




class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self.setMinimumSize(1400, 700)
        tablist = []
        tablabellist = []
        tablabellistname = ['New','Show','Change','Delete']
        #
        
        layoutlist=[]
        self.tablelist = []
        Tab = QTabWidget()
        self.headerlist = [ 'ID','Brand','Sort','Weight','Price','Rating','Taste','Place','Date Added','Added By','Date Modified', 'Change']
        
        
        num_tab_widgets = len(tablabellistname)
        
        for i in range(num_tab_widgets):
            tablist.append(QWidget())
            Tab.addTab(tablist[i], (tablabellistname[i]))
            tablabellist.append(QLabel('title'))
            self.tablelist.append(QTableWidget())
            setattr(self,'Table%d'%i,self.tablelist[i])
            layoutlist.append(QVBoxLayout())
        
            self.tablelist[i].setColumnCount(len(self.headerlist))
            self.tablelist[i].setHorizontalHeaderLabels(self.headerlist)
            self.tablelist[i].setSortingEnabled(True)
            
            #self.tablelist[i].setEditTriggers(QTableWidget.NoEditTriggers)
            self.tablelist[i].setSelectionBehavior(QTableWidget.SelectRows)
            self.tablelist[i].setSelectionMode(QTableWidget.SingleSelection)
            
            
            #self.tablelist
        
            layoutlist[i].addWidget(tablabellist[i])
            layoutlist[i].addWidget(self.tablelist[i])
            tablist[i].setLayout(layoutlist[i])
        
        #Button new item        
        self.tablelist[0].setRowCount(1)
        
        
        #combobox Lists     
        brandList =['Al Waha','Al Fakher','7 Days']
        weightList = ['100','200','500','1000']
        priceList = ['14.90','15.90','54.90']
        ratingList=['1','2','3','4','5','6','7','8','9','10']
        placeList=['Lager1','Lager2']
        
        
        #str to int
        ratingliststr = list(map(int, ratingList))
        
        #combobox
        self.comboboxBrand = QComboBox(self)
        self.comboboxBrand.addItems(brandList)
        self.comboboxBrand.setEditable(True)
        self.tablelist[0].setCellWidget(0,1,self.comboboxBrand)
        
        self.comboboxWeight = QComboBox(self)
        self.comboboxWeight.addItems(weightList)
        self.tablelist[0].setCellWidget(0,3,self.comboboxWeight)
        
        self.comboboxPrice = QComboBox(self)
        self.comboboxPrice.addItems(priceList)
        self.tablelist[0].setCellWidget(0,4,self.comboboxPrice)
        
        self.comboboxRating = QComboBox(self)
        self.comboboxRating.addItems(ratingList)
        self.tablelist[0].setCellWidget(0,5,self.comboboxRating)
        
        self.comboboxPlace = QComboBox(self)
        self.comboboxPlace.addItems(placeList)
        self.tablelist[0].setCellWidget(0,7,self.comboboxPlace)

        item = self.tablelist[0].item (0, 0)
        #print (item)
        
        self.pushButton1 = QPushButton("Add Entry")
        self.pushButton1.clicked.connect(self.addEntry)
        layoutlist[0].addWidget(self.pushButton1)
        tablist[0].setLayout(layoutlist[0])
        
        self.pushButton2 = QPushButton("Load")
        self.pushButton2.clicked.connect(self.load)
        layoutlist[1].addWidget(self.pushButton2)
        tablist[1].setLayout(layoutlist[1])
        
        #self.tablelist[0].doubleClicked.connect(self.addEntry)
        
        CLayout = QVBoxLayout()
        CLayout.addWidget(Tab)
        
        Cwidget = QWidget()
        Cwidget.setLayout(CLayout)    
        self.setCentralWidget(Cwidget)
        
    
    def load(self):  
        cnx = mysql.connector.connect(host='62.108.32.183',
                                      port=3306,
                                      database='aumcfuom_allgemein',
                                      user='aumcf_info2',
                                      password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')
    
        cursor = cnx.cursor()  
        query= "SELECT * FROM brand"
        cursor.execute(query)
        result = []
           
        for i in cursor:
            result.append(i)
        print(result)
            
        self.tablelist[1].setRowCount(0)
        btnlist = []
        #btn = QPushButton(self.tablelist[1])
        #btn.setText('Change')
        
        for row_number, row_data in enumerate(result):
            
            self.tablelist[1].insertRow(row_number)
            for column_number, data in enumerate (row_data):
                self.tablelist[1].setItem(row_number, column_number,QTableWidgetItem(str(data)))
                
            btnlist.append(QPushButton(self.tablelist[1]))
            btnlist[row_number].setText('Change')
            
            self.tablelist[1].setCellWidget(row_number, (len(self.headerlist))-1, btnlist[row_number])
            index = row_number
            btnlist[row_number].clicked.connect(lambda *args, index=index: self.change(index))
            '''
            index = QPersistentModelIndex(
                self.tablelist[1].model().index(row_number, column))
            button.clicked.connect(
                lambda *args, index=index: self.handleButton(index))
            '''
        cnx.close()
        if (not cnx.is_connected()):
                print('Disconnected from MySQL database')  
        
        self.tablelist[1].setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablelist[1].resizeColumnsToContents()
        
    @pyqtSlot()
    def addEntry(self):
        print("Add Entry clicked")
        entry=[]

        for xi in range(0,len(self.headerlist)):
            entry.append(self.tablelist[0].item(0,xi).text())
        print(entry)   
        
    def change(self, index):
        print("Change Entry")
        rowlist=[]
        row = index
        #print(row)
        
        for xj in range(0,len(self.headerlist)):
            print(self.tablelist[1].item(row,xj).text())
            if(self.tablelist[1].item(row,xj).text() == None):
                rowlist.append("")
            else:
                rowlist.append(self.tablelist[1].item(row,xj).text())
        print(rowlist)
        
        #for yi in range(0,10):
         #   rowlist.append(self.tablelist[1].selectedItems().item(0,yi).text())
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
'''
    else:
        registration= Registration()
        registration.show()
        sys.exit(app.exec_())

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    '''