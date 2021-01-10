from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
from os import path
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"hotel.ui"))

class App_Window(QMainWindow , FORM_CLASS):
    def __init__(self):
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.Handle_Ui()

    def Handle_Ui(self) :
        self.setWindowTitle('LOGIN')   
        self.setWindowIcon(QIcon('logo2.png'))
        
        
def main():
    app = QApplication(sys.argv)
    window = App_Window()
    window.show()
    app.exec_()
   
if __name__ == "__main__":
    main()