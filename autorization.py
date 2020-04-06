from PyQt5 import QtWidgets
from PyQt5 import QtCore
from auth import Ui_Form  # импорт сгенерированного файла
import sys
from database import Database

# pyuic5 auth.ui -o auth.py

class Communicate(QtCore.QObject):
    AuthOk = QtCore.pyqtSignal()

class authwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(authwindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Autorization')
        self.login = ''
        self.C = Communicate()
        self.database = Database()

        self.ui.enterButton.clicked.connect(self.enterClick)

    def enterClick(self):
        login = self.ui.loginEdit.text()
        password = self.ui.passwordEdit.text()

        if not (login and password):
            self.ui.errorLabel.setText('*Enter login and password')
            return

        access = self.database.querySelectUser(login, password)
        print(access)
        if access == 2:
            self.login = login
            self.C.AuthOk.emit()
            self.close()
        elif access == 1:
            self.ui.errorLabel.setText('*You havent enought right to enter')
        else:
            self.ui.errorLabel.setText('*You enter incorrect login or password')