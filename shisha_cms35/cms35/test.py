import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
from mysql.connector import Error
from msilib.schema import ComboBox
 

 

'''
Created on 30.06.2018

@author: Michi
'''
global user_name
global user_rights
global user_id


'''
class user():
    def __init__(self, username=0, rights=0, id=0):
        self._username = username
        self._rights = rights
        self._id = id
    def get_username(self):
        return self._username
    def set_username(self, username):
        self._username = username   
        
    def get_rights(self):
        return self._rights
    def set_rights(self, rights):
        self._rights = rights
        
    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id
'''
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
        result = cursor.fetchall()
        for i in result:
            self.comboBox.addItem(str(i[0]))
            
        cnx.close()
        print(result)
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')
        
        
        self.rUsername = QLabel("Benutzername")
        self.rMail = QLabel("E-Mail")
        self.rPw = QLabel("Passwort")
        self.rPwBe = QLabel("Passwort bestaetigen")
        self.txtRname = QLineEdit(self)
        self.txtRmail = QLineEdit(self)
        self.txtRpass = QLineEdit(self)
        self.txtRpassBe = QLineEdit(self)
        self.buttonRegistration = QPushButton('Registration', self)
        self.buttonRegistration.clicked.connect(self.regmember)
        
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.rUsername)
        self.tab2.layout.addWidget(self.txtRname)
        self.tab2.layout.addWidget(self.rMail)
        self.tab2.layout.addWidget(self.txtRmail)
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
        cnx = mysql.connector.connect(host='62.108.32.183',
                              port=3306,
                              database='aumcfuom_allgemein',
                              user='aumcf_info2',
                              password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')

        cursor = cnx.cursor()  
            
        if(self.txtRpass.text() == self.txtRpassBe.text()):
            print("gleich")
            query= "SELECT username from members"
            cursor.execute(query)
            result = cursor.fetchall()
            user=[]
            for i in result:
                user.append(i[0])
                
            if(self.txtRname.text()in user):
                print("vorhanden")
            else:
                try:
                    data = []
                    data.append(str(self.txtRname.text()))
                    data.append(str(self.txtRmail.text()))
                    data.append(str(self.comboBox.currentText()))
                    data.append(str(self.txtRpass.text()))
                    print(data)
                    query_user="INSERT INTO members (id, username, email, rights_ID, password) VALUES(NULL,%s,%s,(SELECT id from members_rights WHERE rights=%s),%s)"
                    cursor.execute(query_user,data)
                    cnx.commit()
                except:
                    cnx.rollback()
        else:
            pass   
            
        entry=[]
        
        print(entry)
        
        cnx.close()
        #print(result)
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')   
    
    def handleLogin(self):
        '''
        if (self.txtName.text() == 'foo' and self.txtPass.text() == 'bar'):
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')
        
        '''
        print("Login Clicked")
        cnx = mysql.connector.connect(host='62.108.32.183',
                              port=3306,
                              database='aumcfuom_allgemein',
                              user='aumcf_info2',
                              password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')

        cursor = cnx.cursor()
        #Login Daten in Array
        data_login=[]
        data_login.append(self.txtName.text())
        #data_login.append(self.txtPass.text())
        print(data_login)
        
        query_login="Select members.id, members.username, members.password, members_rights.rights from members INNER JOIN members_rights on members_rights.id = members.rights_ID Where members.username=%s"
        cursor.execute(query_login,data_login)
        result = cursor.fetchall()
        print(result)
        user_login=[]
        for i in result:
            user_login.append(i)
        
        data_login.append(self.txtPass.text())
        print(data_login[0],data_login[1])
        print("user_login:",user_login[0][1],user_login[0][2])
        if(data_login[0] == user_login[0][1] and data_login[1] == user_login[0][2]):
            
            #Uebergabe an Globale Variable
            '''
            global user_name
            user_name=user_login[0][1]
            global user_rights
            user_rights=login[0][3]
            global user_id
            user_id=user_login[0][0]
            '''
            self.accept()
        else:
            QMessageBox.Warning(
                self, 'Error', 'Benutzername und Passwort stimmen nicht ueberein')
        #print(user_login)
        print(user_login)
        #if(self.txtRname.text()in user):
        #   print("vorhanden")
        cnx.close()
        #print(result)
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')



class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        global user_name
        print("INFO:",user_name)
        
        self.setMinimumSize(1400, 700)
        self.tablist = []
        self.tablabellist = []
        self.tablabellistname = ['New','Show','Change','Delete']
        #
        
        layoutlist=[]
        self.tablelist = []
        self.Tab = QTabWidget()
        self.headerlist = [ 'ID','Brand','Sort','Taste','Rating','Weight','Price','Place','Added By','Date Added','Date Modified', 'Change','Delete']
        self.headerlistNew = ['Brand','Sort','Taste','Rating','Weight','Price','Place']
        
        
        num_tab_widgets = len(self.tablabellistname)
        
        for i in range(num_tab_widgets):
            self.tablist.append(QWidget())
            self.Tab.addTab(self.tablist[i], (self.tablabellistname[i]))
            self.tablabellist.append(QLabel('title'))
            self.tablelist.append(QTableWidget())
            setattr(self,'Table%d'%i,self.tablelist[i])
            layoutlist.append(QVBoxLayout())
        
            self.tablelist[i].setColumnCount(len(self.headerlistNew))
            self.tablelist[i].setHorizontalHeaderLabels(self.headerlistNew)
            self.tablelist[i].setSortingEnabled(True)
            
            #self.tablelist[i].setEditTriggers(QTableWidget.NoEditTriggers)
            self.tablelist[i].setSelectionBehavior(QTableWidget.SelectRows)
            self.tablelist[i].setSelectionMode(QTableWidget.SingleSelection)
            
            
            #self.tablelist
        
            layoutlist[i].addWidget(self.tablabellist[i])
            layoutlist[i].addWidget(self.tablelist[i])
            self.tablist[i].setLayout(layoutlist[i])
        
        #Button new item        
        #Tab.setTabEnabled(3,False)
        self.Tab.removeTab(2)
        self.Tab.removeTab(2)
        #Tab.addTab(tablist[3], (tablabellistname[3]))
        #Tab.insertTab(self,tablist[3],(tablabellistname[3]))
        
        #Tablelist[0]--> New set right headerfiles
        self.tablelist[1].setColumnCount(len(self.headerlist))
        self.tablelist[1].setHorizontalHeaderLabels(self.headerlist)
        
        self.tablelist[0].setRowCount(1)
        
        #self.tablelist[1].setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
        
        #combobox Lists    SELECT Befehle
        
        self.brandList =[]
        self.weightList = []
        self.priceList = []
        self.ratingList=[]
        self.placeList=[]

        cnx = mysql.connector.connect(host='62.108.32.183',
                                      port=3306,
                                      database='aumcfuom_allgemein',
                                      user='aumcf_info2',
                                      password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')
    
        cursor = cnx.cursor()  
        queryWeight = ("SELECT weight FROM weight ")
        queryBrand = ("SELECT brand FROM brand ")
        queryPrice =("SELECT price FROM price")
        queryRating = ("SELECT rating FROM rating")
        queryPlace =("SELECT place FROM place")
        
        cursor.execute(queryWeight)
        print("Query executed!")
        for i in cursor:
            print(i[0])
            self.weightList.append(str(i[0]))
        print(self.weightList)
        
        cursor.execute(queryBrand)        
        print("Query executed!")        
        for i in cursor:
            print(i[0])
            self.brandList.append(str(i[0]))
        print(self.brandList)
        
        cursor.execute(queryPrice)        
        print("Query executed!")        
        for i in cursor:
            print(i[0])
            self.priceList.append(str(i[0]))
        print(self.priceList)
        
        cursor.execute(queryRating)        
        print("Query executed!")       
        for i in cursor:
            print(i[0])
            self.ratingList.append(str(i[0]))
        print(self.ratingList)
        
        cursor.execute(queryPlace)        
        print("Query executed!")        
        for i in cursor:
            print(i[0])
            self.placeList.append(str(i[0]))
        print(self.placeList)
            
        
        #btn = QPushButton(self.tablelist[1])
        #btn.setText('Change')
        
        cnx.close()
        if (not cnx.is_connected()):
                print('Disconnected from MySQL database')

        
        
        
        
        
        
        #str to int
        #ratingliststr = list(map(int, self.ratingList))
        
        #combobox
        self.comboboxBrand = QComboBox(self)
        self.comboboxBrand.addItems(self.brandList)
        self.comboboxBrand.setEditable(True)
        self.tablelist[0].setCellWidget(0,0,self.comboboxBrand)
        
        
        self.comboboxWeight = QComboBox(self)
        self.comboboxWeight.addItems(self.weightList)
        self.tablelist[0].setCellWidget(0,4,self.comboboxWeight)
        
        
        self.comboboxPrice = QComboBox(self)
        self.comboboxPrice.addItems(self.priceList)
        self.tablelist[0].setCellWidget(0,5,self.comboboxPrice)
        
        self.comboboxRating = QComboBox(self)
        self.comboboxRating.addItems(self.ratingList)
        self.tablelist[0].setCellWidget(0,3,self.comboboxRating)

        
        self.comboboxPlace = QComboBox(self)
        self.comboboxPlace.addItems(self.placeList)
        self.tablelist[0].setCellWidget(0,6,self.comboboxPlace)


        item = self.tablelist[0].item (0, 0)
        #print (item)
        
        self.pushButton1 = QPushButton("Add Entry")
        self.pushButton1.clicked.connect(self.addEntry)
        layoutlist[0].addWidget(self.pushButton1)
        self.tablist[0].setLayout(layoutlist[0])
        
        self.pushButton2 = QPushButton("Load")
        self.pushButton2.clicked.connect(self.load)
        layoutlist[1].addWidget(self.pushButton2)
        self.tablist[1].setLayout(layoutlist[1])
        
        #self.tablelist[0].doubleClicked.connect(self.addEntry)
        
        CLayout = QVBoxLayout()
        CLayout.addWidget(self.Tab)
        
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
        query= ('''
                SELECT tobacco.tobacco_ID,brand.brand, sort.sort, sort.other, rating.rating, weight.weight, price.price, place.place, members.username, tobacco.date_added, tobacco.date_modified
                from place
                inner join tobacco on tobacco.place_ID = place.place_ID
                inner join price on price.price_ID = tobacco.price_ID
                inner join weight on weight.weight_ID = tobacco.weight_ID 
                inner join sort on sort.sort_ID = tobacco.sort_ID
                inner join members on members.id = tobacco.members_ID
                inner join brand on brand.brand_ID = sort.brand_ID
                inner join rating on rating.rating_ID = sort.rating_ID
                ''')
        
        cursor.execute(query)
        result = []
        
        print("Query executed!")
        
        for i in cursor:
            result.append(i)
        print(result)
            
        self.tablelist[1].setRowCount(0)
        btnChangeList = []
        btnDeleteList = []
        #btn = QPushButton(self.tablelist[1])
        #btn.setText('Change')
        
        for row_number, row_data in enumerate(result):
            
            self.tablelist[1].insertRow(row_number)
            for column_number, data in enumerate (row_data):
                self.tablelist[1].setItem(row_number, column_number,QTableWidgetItem(str(data)))
            
            #insert btnChange in row
            btnChangeList.append(QPushButton(self.tablelist[1]))
            btnChangeList[row_number].setText('Change')
            
            self.tablelist[1].setCellWidget(row_number, (len(self.headerlist))-2, btnChangeList[row_number])
            index = row_number
            btnChangeList[row_number].clicked.connect(lambda *args, index=index: self.change(index))
            
            #insert btnDelete in row
            btnDeleteList.append(QPushButton(self.tablelist[1]))
            btnDeleteList[row_number].setText('Delete')
            
            self.tablelist[1].setCellWidget(row_number, (len(self.headerlist))-1, btnDeleteList[row_number])
            index = row_number
            btnDeleteList[row_number].clicked.connect(lambda *args, index=index: self.delete(index))
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

        #entry.append(self.tablelist[0].item(0,0).text())        
        print(entry)
        entry.append(str(self.comboboxBrand.currentText()))
        entry.append(self.tablelist[0].item(0,1).text())
        entry.append(self.tablelist[0].item(0,2).text())
        entry.append(str(self.comboboxRating.currentText()))
        entry.append(str(self.comboboxWeight.currentText()))
        entry.append(str(self.comboboxPrice.currentText()))
        entry.append(str(self.comboboxPlace.currentText()))
        print("Entry: ",entry)   
        
    def change(self, index):
        print("Change Entry")
        rowChangeList=[]
        row = index
        #print(row)
        self.Tab.addTab(self.tablist[2], (self.tablabellistname[2]))
        self.tablelist[2].setRowCount(1)
        
        for xj in range(0,(len(self.headerlist))-2):
            print(str(self.tablelist[1].item(row,xj).text()))
            #if(self.tablelist[1].item(row,xj).text().isEmpty()):
            #    rowlist.append("")
            #else:
            rowChangeList.append(str(self.tablelist[1].item(row,xj).text()))
            
        print(rowChangeList)
        
        for i in range(len(rowChangeList)):
            self.tablelist[2].setItem(0, i,QTableWidgetItem(str(rowChangeList[i])))
        self.Tab.setCurrentIndex(2)
        
        #self.comboBoxBrand.setindex()
        #combobox
        self.comboboxBrandCh = QComboBox(self)
        self.comboboxBrandCh.addItems(self.brandList)
        self.comboboxBrandCh.setCurrentText(rowChangeList[1])
        self.comboboxBrandCh.setEditable(True)
        self.tablelist[2].setCellWidget(0,0,self.comboboxBrandCh)
        
        
        self.comboboxWeightCh = QComboBox(self)
        self.comboboxWeightCh.addItems(self.weightList)
        self.comboboxWeightCh.setCurrentText(rowChangeList[5])
        self.tablelist[2].setCellWidget(0,4,self.comboboxWeightCh)
        
        
        self.comboboxPrice = QComboBox(self)
        self.comboboxPriceCh.addItems(self.priceList)
        self.comboboxPriceCh.setCurrentText(rowChangeList[3])
        self.tablelist[2].setCellWidget(0,5,self.comboboxPriceCh)
        
        self.comboboxRatingCh = QComboBox(self)
        self.comboboxRatingCh.addItems(self.ratingList)
        self.comboboxRatingCh.setCurrentText(rowChangeList[4])
        self.tablelist[2].setCellWidget(0,3,self.comboboxRatingCh)

        
        self.comboboxPlaceCh = QComboBox(self)
        self.comboboxPlaceCh.addItems(self.placeList)
        self.comboboxPlaceCh.setCurrentText(rowChangeList[5])
        self.tablelist[2].setCellWidget(0,6,self.comboboxPlaceCh)
        
        '''
        self.comboboxBrand.setCurrentText(rowChangeList[1])
        self.tablelist[2].setCellWidget(0,0,self.comboboxBrand)#
        print(rowChangeList[1])
        self.tablelist[2].setCellWidget(0,1,secomboboxPriceChght)
        self.tablelist[2].setCellWidget(0,2,self.comboboxPrice)
        self.tablelist[2].setCellWidget(0,3,self.comboboxRating)
        self.tablelist[2].setCellWidget(0,4,self.comboboxPlace)        
        '''
        
        #for yi in range(0,10):
         #   rowlist.append(self.tablelist[1].selectedItems().item(0,yi).text())
         
    def delete(self, index):
        print("Delete Entry")
        rowDeleteList=[]
        row = index
        #print(row)
        self.Tab.addTab(self.tablist[3], (self.tablabellistname[3]))
        self.tablelist[3].setRowCount(1)
        for xj in range(0,len(self.headerlist)-2):
            print(str(self.tablelist[1].item(row,xj).text()))
            #if(self.tablelist[1].item(row,xj).text().isEmpty()):
            #    rowlist.append("")
                #else:
            rowDeleteList.append(str(self.tablelist[1].item(row,xj).text()))
        print(rowDeleteList)
        
        #Insert rowDeleteList into tablelist[3]
        for i in range(len(rowDeleteList)):
            self.tablelist[3].setItem(0, i,QTableWidgetItem(str(rowDeleteList[i])))
        self.Tab.setCurrentIndex(3)
        
        
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