import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector
from mysql.connector import Error
from msilib.schema import ComboBox


'''
@author: Michael Stych, Marcel Gruber
'''

user_name=""
user_rights=""
user_id=""

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
        self.txtRpass.setEchoMode(QLineEdit.Password)
        self.txtRpassBe = QLineEdit(self)
        self.txtRpassBe.setEchoMode(QLineEdit.Password)
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
                error_q=QMessageBox()
                error_q.setIcon(QMessageBox.Warning)
                error_q.setText("Benutzername schon vorhanden")
                error_q.exec()
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
            error_q=QMessageBox()
            error_q.setIcon(QMessageBox.Warning)
            error_q.setText("Passwoerter stimmen nicht ueberein")
            error_q.exec()
        entry=[]
        
        print(entry)
        
        cnx.close()
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')   
    
    def handleLogin(self):
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
            
            global user_name
            user_name=user_login[0][1]
            print(user_name)
            global user_rights
            user_rights=user_login[0][3]
            global user_id
            user_id=user_login[0][0]
            
            self.accept()
        else:
            error_q=QMessageBox()
            error_q.setIcon(QMessageBox.Warning)
            error_q.setText("Benutzername und Passwort stimmen nicht ueberein")
            error_q.exec()

        print(user_login)
        cnx.close()
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')



class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        print(user_name,"MaIN")
        
        self.setMinimumSize(1400, 700)#Fenstergroesse
        #Listen die in der for Schleife gefuellt werden
        self.tablist = []
        self.tablabellist = []
        self.tablabellistname = ['New','Show','Change']#Tabnamen
 
        layoutlist=[]
        self.tablelist = []
        #Tabwidget
        self.Tab = QTabWidget()
        #Headerlisten fuer die Tabellen der jeweiligen Tabs
        self.headerlist = [ 'ID','Brand','Sort','Taste','Rating','Weight','Price','Place','Added By','Date Added','Date Modified', 'Change','Delete']
        self.headerlistNew = ['Brand','Sort','Taste','Rating','Weight','Price','Place']
        
        #nummer der Tabwidgets
        num_tab_widgets = len(self.tablabellistname)
        
        #In der For-Schleife werden die verschiedenen Widgets, Tabs, TableWidets, layouts zugeordnet
        for i in range(num_tab_widgets):
            self.tablist.append(QWidget()) #Qwidget wird hinzugefuegt
            self.Tab.addTab(self.tablist[i], (self.tablabellistname[i]))#Tabs werden hinzugefueht
            self.tablabellist.append(QLabel('title'))
            self.tablelist.append(QTableWidget())
            setattr(self,'Table%d'%i,self.tablelist[i])
            layoutlist.append(QVBoxLayout())
        
            self.tablelist[i].setColumnCount(len(self.headerlistNew))
            self.tablelist[i].setHorizontalHeaderLabels(self.headerlistNew)
            self.tablelist[i].setSortingEnabled(True)
            
            self.tablelist[i].setSelectionBehavior(QTableWidget.SelectRows)
            self.tablelist[i].setSelectionMode(QTableWidget.SingleSelection)
            

        
            layoutlist[i].addWidget(self.tablabellist[i])
            layoutlist[i].addWidget(self.tablelist[i])
            self.tablist[i].setLayout(layoutlist[i])
        

        self.Tab.removeTab(2)

        self.tablelist[1].setColumnCount(len(self.headerlist))
        self.tablelist[1].setHorizontalHeaderLabels(self.headerlist)
        
        self.tablelist[0].setRowCount(1)
        
        
        
        
        #combobox Lists    SELECT Befehle
        
        self.brandList =[]
        self.weightList = []
        self.priceList = []
        self.ratingList=[]
        self.placeList=[]

        #sql abfrage fuer die auswahl der comboboxen
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
            
        
        cnx.close()
        if (not cnx.is_connected()):
                print('Disconnected from MySQL database')


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
        
        self.pushButton1 = QPushButton("Add Entry")
        self.pushButton1.clicked.connect(self.addEntry)
        layoutlist[0].addWidget(self.pushButton1)
        self.tablist[0].setLayout(layoutlist[0])
        
        self.pushButton2 = QPushButton("Load")
        self.pushButton2.clicked.connect(self.load)
        layoutlist[1].addWidget(self.pushButton2)
        self.tablist[1].setLayout(layoutlist[1])
        
        self.pushButton3 = QPushButton("Change Entry")
        self.pushButton3.clicked.connect(self.changeEntry)
        layoutlist[2].addWidget(self.pushButton3)
        self.tablist[2].setLayout(layoutlist[2])
        
        
        CLayout = QVBoxLayout()
        CLayout.addWidget(self.Tab)
        
        Cwidget = QWidget()
        Cwidget.setLayout(CLayout)    
        self.setCentralWidget(Cwidget)
        
    
    def load(self):  
        #laden der daten aus sql und fuellen der tabellen
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
        
        #tabelle fuellen mit allen daten
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
            
            if(user_rights!="Admin"):
                btnChangeList[row_number].setEnabled(False)
                btnDeleteList[row_number].setEnabled(False)

        cnx.close()
        if (not cnx.is_connected()):
                print('Disconnected from MySQL database')  
        
        self.tablelist[1].setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablelist[1].resizeColumnsToContents()
        
    @pyqtSlot()
    def addEntry(self):
        #eintraege erstellen
        print("Add Entry clicked")
        entry=[]
     
        print(entry)
        entry.append(str(self.comboboxBrand.currentText()))
        entry.append(self.tablelist[0].item(0,1).text())
        entry.append(self.tablelist[0].item(0,2).text())
        entry.append(str(self.comboboxRating.currentText()))
        entry.append(str(self.comboboxWeight.currentText()))
        entry.append(str(self.comboboxPrice.currentText()))
        entry.append(str(self.comboboxPlace.currentText()))
        print("Entry: ",entry)
        
        cnx = mysql.connector.connect(host='62.108.32.183',
                                      port=3306,
                                      database='aumcfuom_allgemein',
                                      user='aumcf_info2',
                                      password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')

        cursor = cnx.cursor()
        try:
            data_add=[]
            data_add.append(entry[0])
            data_add.append(entry[2])
            data_add.append(entry[3])
            data_add.append(entry[1])
            print(data_add)
            query_add=('''insert INTO
                        sort (brand_ID, other, rating_ID, sort, sort_ID)
                        VALUES((SELECT brand_ID FROM brand WHERE brand=%s), %s,
                               (SELECT rating_ID FROM rating WHERE rating=%s), %s,NULL)''')
            
            
    
            cursor.execute(query_add, data_add)
            cnx.commit()
            data_add.clear()
            data_add.append(entry[1])
            data_add.append(entry[4])
            data_add.append(entry[5])
            data_add.append(user_id)
            data_add.append(entry[6])
            print("data2####:",data_add)
            query_add2=('''INSERT INTO
                        tobacco (tobacco_ID, sort_ID, weight_ID, price_ID, members_ID, place_ID, date_added, date_modified)
                        VALUES(Null,(SELECT sort_ID FROM sort WHERE sort=%s),
                       (SELECT weight_ID from weight WHERE weight=%s),
                       (SELECT price_ID from price WHERE price=%s),
                       (SELECT id from members WHERE id=%s),
                       (SELECT place_ID from place WHERE place=%s), CURRENT_DATE,CURRENT_DATE)''')
            cursor.execute(query_add2, data_add)
            cnx.commit()
        except:
            print("rollback")
            cnx.rollback()

            
        cnx.close()
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')
         

        
    def changeEntry(self):
        #eintraege aendern
        print("changeEntry clicked")
        changeEntryList=[]
        
        changeEntryList.append(self.rowChangeList[0])
        changeEntryList.append(str(self.comboboxBrandCh.currentText()))
        changeEntryList.append(self.tablelist[2].item(0,1).text())
        changeEntryList.append(self.tablelist[2].item(0,2).text())
        changeEntryList.append(str(self.comboboxRatingCh.currentText()))
        changeEntryList.append(str(self.comboboxWeightCh.currentText()))
        changeEntryList.append(str(self.comboboxPriceCh.currentText()))
        changeEntryList.append(str(self.comboboxPlaceCh.currentText()))
        print("Entry: ",changeEntryList) 
        self.load() 
        self.Tab.setCurrentIndex(1)
        self.Tab.removeTab(2)
        
        cnx = mysql.connector.connect(host='62.108.32.183',
                                      port=3306,
                                      database='aumcfuom_allgemein',
                                      user='aumcf_info2',
                                      password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')

        cursor = cnx.cursor() 
        try: 
            data_r=[]
            data_sort=[]
            data_id=[]
            data_id.append(changeEntryList[4])
            print("data_id: ",data_id)
            query_rating="Select rating_ID from rating where rating=%s"
            cursor.execute(query_rating,data_id)
            for i in cursor:
                print("i:",str(i[0]))
                data_r.append(i[0])
            
            
            print("1")
            data_sort.append(changeEntryList[2])
            data_sort.append(changeEntryList[3])
            data_sort.append(data_r[0])
            print("data_sort:",data_sort)
            data_id.clear()
            data_id.append(changeEntryList[1])
            print("change marke: ",data_id)
            query_brand="Select brand_ID from brand where brand=%s"
            cursor.execute(query_brand,data_id)
            for i in cursor:
                data_sort.append(i[0])
            data_sort.append(self.rowChangeList[2])
            query_sort= "UPDATE sort SET sort=%s, other=%s, rating_ID=%s, brand_ID=%s WHERE sort=%s"
            cursor.execute(query_sort,data_sort)
            cnx.commit()
            print("commit 1 tut")
            
            data_sort.clear()
            data_id.clear()
            data_r.clear()

            print("data_ID: ",data_id)
            query_weight="Select weight_ID from weight where weight=%s"
            query_rating="Select price_ID from price where price=%s"
            query_place="Select place_ID from place where place=%s"
            data_id.append(changeEntryList[5])
            cursor.execute(query_weight,data_id)
            for i in cursor:
                data_r.append(i[0])
            data_id.clear()
            data_id.append(changeEntryList[6])
            cursor.execute(query_rating,data_id)
            for i in cursor:
                data_r.append(i[0])
            data_id.clear()
            data_id.append(changeEntryList[7])
            cursor.execute(query_place,data_id)
            for i in cursor:
                data_r.append(i[0])
            
            print("select 2 tut")
            
            data_r.append(changeEntryList[0])
            print("data_r: ",data_r)
            query_tobacco= "update tobacco SET weight_ID=%s, price_ID=%s, place_ID=%s WHERE tobacco_ID=%s;"
            cursor.execute(query_tobacco,data_r)
            cnx.commit()
        except:
            print("rollback")
            cnx.rollback()
            
            
        cnx.close()
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')
        
        self.load()
        
        
        
    def change(self, index):
        #oeffnet tab zum changen
        print("Change Entry")
        self.rowChangeList=[]
        row = index
        self.Tab.addTab(self.tablist[2], (self.tablabellistname[2]))
        self.tablelist[2].setRowCount(1)
        
        for xj in range(0,(len(self.headerlistNew)+1)):
            print(str(self.tablelist[1].item(row,xj).text()))
            self.rowChangeList.append(str(self.tablelist[1].item(row,xj).text()))
            
        print(self.rowChangeList)
        
        
        self.tablelist[2].setItem(0, 1,QTableWidgetItem(str(self.rowChangeList[2])))

        self.tablelist[2].setItem(0, 2,QTableWidgetItem(str(self.rowChangeList[3])))

        #combobox
        print(self.rowChangeList)
        self.comboboxBrandCh = QComboBox(self)
        self.comboboxBrandCh.addItems(self.brandList)
        self.comboboxBrandCh.setCurrentText(self.rowChangeList[1])
        self.comboboxBrandCh.setEditable(True)
        self.tablelist[2].setCellWidget(0,0,self.comboboxBrandCh)  
        
        self.comboboxWeightCh = QComboBox(self)
        self.comboboxWeightCh.addItems(self.weightList)
        self.comboboxWeightCh.setCurrentText(self.rowChangeList[5])
        self.tablelist[2].setCellWidget(0,4,self.comboboxWeightCh)
        
        self.comboboxPriceCh = QComboBox(self)
        self.comboboxPriceCh.addItems(self.priceList)
        self.comboboxPriceCh.setCurrentText(self.rowChangeList[6])
        self.tablelist[2].setCellWidget(0,5,self.comboboxPriceCh)
        
        self.comboboxRatingCh = QComboBox(self)
        self.comboboxRatingCh.addItems(self.ratingList)
        self.comboboxRatingCh.setCurrentText(self.rowChangeList[4])
        self.tablelist[2].setCellWidget(0,3,self.comboboxRatingCh)
        
        self.comboboxPlaceCh = QComboBox(self)
        self.comboboxPlaceCh.addItems(self.placeList)
        self.comboboxPlaceCh.setCurrentText(self.rowChangeList[7])
        self.tablelist[2].setCellWidget(0,6,self.comboboxPlaceCh)
        
        self.Tab.setCurrentIndex(2)
        
        #save new values of the row in list

         
    def delete(self, index):
        #loeschen von eintraegen
        print("Delete Entry")
        rowDeleteList=[]
        row = index
        rowDeleteList.append(str(self.tablelist[1].item(row,0).text()))
        
        cnx = mysql.connector.connect(host='62.108.32.183',
                                      port=3306,
                                      database='aumcfuom_allgemein',
                                      user='aumcf_info2',
                                      password='An4pu3$3')
        if cnx.is_connected():
            print('Connected to MySQL database')

        cursor = cnx.cursor() 
        try: 
            query_delete="DELETE FROM tobacco WHERE tobacco_ID=%s;"
            cursor.execute(query_delete,rowDeleteList)
            cnx.commit()
        except:
            print("rollback")
            cnx.rollback()
            

        cnx.close()
        if (not cnx.is_connected()):
            print('Disconnected from MySQL database')
        
        self.load()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
