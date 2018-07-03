import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
#!/usr/bin/python
# -'''- coding: utf-8 -'''-
 



     



class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        #Fenster options
        
        
        self.txtName = QLineEdit(self)
        self.txtPass = QLineEdit(self)
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.username = QLabel("Benutzername")
        self.pw = QLabel("Passwort")
        
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonRegistration = QPushButton('Registration', self)
        #self.buttonRegistration.clicked.connect(self.handleRegistration)
        
        
                
        
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.username)
        layout.addWidget(self.txtName)
        layout.addWidget(self.pw)
        layout.addWidget(self.txtPass)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonRegistration)



    def handleLogin(self):
        if (self.txtName.text() == 'foo' and self.txtPass.text() == 'bar'):
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')
            
    '''def handleRegistration(self):
        windowRegistration = Registration()
        windowRegistration.show()
    '''
            
class MyTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(MyTableWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()    
        self.tab2 = QWidget()
        self.tab3 = QWidget()    
        self.tab4 = QWidget()
        
        
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Neu")
        self.tabs.addTab(self.tab2,"Anzeigen")
        self.tabs.addTab(self.tab3,"Bearbeiten")
        self.tabs.addTab(self.tab4,"Loeschen")
        
        
 
        self.table_querying = Table(self)
        self.header = self.table_querying.verticalHeader()  
        #self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        
        
        self.table_querying2 = Table(self)
        self.header = self.table_querying.horizontalHeader()  
        self.header.stretchLastSection()

        
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.table_querying)
        self.tab1.setLayout(self.tab1.layout)
        
        self.tab2.layout = QHBoxLayout(self)
        self.tab2.layout.addWidget(self.table_querying2)
        self.tab2.setLayout(self.tab2.layout)
        #self.pushButton1 = QPushButton("PyQt5 button")
        #self.tab2.layout.addWidget(self.pushButton1)
        
        
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        
        
        

class Table(QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        
        self.table_querying = QTableWidget(12, 5, self)
        self.header = self.table_querying.horizontalHeader()  
        self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header.stretchLastSection()
        #table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        
        '''
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        vertical = table_querying.verticalHeader()
        vertical.setSectionResizeMode(0, QHeaderView.Stretch)
        vertical.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        vertical.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        '''


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        #Allgemein
        
        
        self.setGeometry(0, 0, 600, 800)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        
        '''
        #Menubar
        self._menu = QMenuBar(self)
        self._menu.setNativeMenuBar(False)
        
        
        fileMenu = self._menu.addMenu("Datei")
        fileMenu.addAction("Neu")
        fileMenu.addAction("Bearbeiten")
        fileMenu.addSeparator()
        fileMenu.addAction("Loeschen")
        fileMenu.addAction("Beenden")
        
        nodeMenu = self._menu.addMenu("Extra")
        nodeMenu.addAction("Bla")
        nodeMenu.addAction("Bla")
        nodeMenu.addAction("bla")
        nodeMenu.addAction("bla")
        '''
        
                
        
    
    pass
'''
class Registration(QMainWindow):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
'''    

 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 800
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
 
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
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