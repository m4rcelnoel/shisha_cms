'''
@author: gmmar
'''
#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from pyside2uic.Compiler.qtproxies import QtGui
from _ctypes import alignment
# from mainwindow import Ui_MainWindow



     



class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        #Fenster options
        self.adjustSize()
        
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
        self.layout = QVBoxLayout(self)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()    
        self.tab2 = QWidget()
        self.tab3 = QWidget()    
        self.tab4 = QWidget()
        self.tabs.resize(700,700) 
        
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Neu")
        self.tabs.addTab(self.tab2,"Anzeigen")
        self.tabs.addTab(self.tab3,"Bearbeiten")
        self.tabs.addTab(self.tab4,"Loeschen")
        
        
 
        table_querying = Table(self)
        
        
        self.tab1.layout = QHBoxLayout(self)
        self.tab1.layout.setStretch(0,1)
        self.tab1.layout.addWidget(table_querying)
        self.tab1.setLayout(self.tab1.layout)
        
        self.tab2.layout = QHBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab2.layout.addWidget(self.pushButton1)
        self.tab2.setLayout(self.tab2.layout)
        
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        
        
        

class Table(QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        
        table_querying = QTableWidget(12, 5, self)

       

        
        #header = table_querying.horizontalHeader()    
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
        self.setMinimumSize(700,500)
        
        
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
'''