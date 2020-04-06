from PyQt5 import QtWidgets
from PyQt5 import QtCore
from auth import Ui_Form  # импорт сгенерированного файла
import sys
from database import Database
import random
from post_email import send_notification

# pyuic5 auth.ui -o auth.py

class regwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(regwindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Registration')
        self.login = ''
        self.database = Database()

        self.ui.enterButton.setText('Registration')
        self.ui.enterButton.clicked.connect(self.enterClick)

    def enterClick(self):
        login = self.ui.loginEdit.text().strip()
        password = self.ui.passwordEdit.text()
        if not (login and password):
            self.ui.errorLabel.setText('*Enter login and password')
            return

        key = int(random.random() * 10**5)
        try:
            send_notification(self.ui.loginEdit.text().strip(), str(key))
        except Exception:
            self.ui.errorLabel.setText('*You enter incorrect email')
            return 

        num, ok = QtWidgets.QInputDialog().getInt(self, "Verifications",
                                     "We post key on your email. Please enter it:", QtWidgets.QLineEdit.Normal)
        if ok:
            if key == num:
                self.database.queryInsertUser(login, password, 2)
                self.ui.errorLabel.setText('You succesfully registration')
            else:
                self.ui.errorLabel.setText('*You enter incorrect key')