from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
from os import path
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"signup1.ui"))

class App_Window(QMainWindow , FORM_CLASS):
    def __init__(self, parent = None):
        super(App_Window,self). __init__(parent)
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.Handle_Ui()
        self.Handle_buttons()
   
    def Handle_Ui(self) :
        self.setWindowTitle('SIGN UP')   
        
    def Handle_buttons(self) :
        self.pushButton.clicked.connect(self.checkpass)    


    def checkpass(self) :
        rightpass=self.lineEdit_3.text() 
        checkedpass=self.lineEdit_4.text()
        if (rightpass != checkedpass) :
            QMessageBox.warning(self ,"Password is wrong" ,"passwrod is wrong please enter your pass again")
            self.lineEdit_4.setText('')
            




def main():
    app = QApplication(sys.argv)
    window = App_Window()
    window.show()
    app.exec_()
   
if __name__ == "__main__":
    main()