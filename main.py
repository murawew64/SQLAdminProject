from PyQt5 import QtWidgets
from admin import Ui_MainWindow  # импорт сгенерированного файла
import sys
from database import Database
from autorization import authwindow
from registration import regwindow

# pyuic5 admin.ui -o admin.py


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Admin application')
        self.database = Database()
        self.authForm = authwindow()
        self.regForm = regwindow()
        self.login = ''

        self.country = ''
        self.type = ''
        self.company = ''

        self.ui.groupBox.setEnabled(False)
        self.ui.groupBox_2.setEnabled(False)
        #self.ui.economicLayout.setVisible(False)

        # соединяю сигналы и слоты
        self.ui.tableBox.currentTextChanged.connect(self.chooseNewTable)
        self.ui.tableWidget.cellDoubleClicked.connect(self.chooseRowsInTable)
        self.ui.addButton.clicked.connect(self.addRecord)
        self.ui.deleteButton.clicked.connect(self.deleteRecord)
        self.ui.updateButton.clicked.connect(self.updateRecord)
        self.authForm.C.AuthOk.connect(self.autorizashionPass)
        self.ui.actionAutorization.triggered.connect(self.authForm.show)
        self.ui.actionExit.triggered.connect(self.exitAction)
        self.ui.actionRegistration.triggered.connect(self.regForm.show)

        self.authForm.show()

    def exitAction(self):
        self.authForm.close()
        self.close()

    # отображаю данные из таблиц для последующего редактирования
    def displayTable(self):
        tableName = self.ui.tableBox.currentText()

        if(tableName == 'Country'):
            countriesList = self.database.querySelectAllCountries()
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(1)
            self.ui.tableWidget.setRowCount(len(countriesList))
            self.ui.tableWidget.setHorizontalHeaderLabels(['Country'])
            for index in range(len(countriesList)):
                self.ui.tableWidget.setItem(
                    index, 0, QtWidgets.QTableWidgetItem(countriesList[index]))

        if(tableName == 'Type'):
            typesList = self.database.querySelectAllTypes()
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(1)
            self.ui.tableWidget.setRowCount(len(typesList))
            self.ui.tableWidget.setHorizontalHeaderLabels(['Type'])
            for index in range(len(typesList)):
                self.ui.tableWidget.setItem(
                    index, 0, QtWidgets.QTableWidgetItem(typesList[index]))

        if(tableName == 'Company'):
            companiesList = self.database.querySelectAllCompanies()
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setRowCount(len(companiesList))
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ['Company', 'Country', 'Type'])
            for index in range(len(companiesList)):
                self.ui.tableWidget.setItem(
                    index, 0, QtWidgets.QTableWidgetItem(companiesList[index][0]))
                self.ui.tableWidget.setItem(
                    index, 1, QtWidgets.QTableWidgetItem(companiesList[index][1]))
                self.ui.tableWidget.setItem(
                    index, 2, QtWidgets.QTableWidgetItem(companiesList[index][2]))

        if(tableName == 'Forbes'):
            forbesList = self.database.querySelectAllForbes()
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(9)
            self.ui.tableWidget.setRowCount(len(forbesList))
            self.ui.tableWidget.setHorizontalHeaderLabels(['Company', 'Country', 'Type', 'Sales', 'Profits', 'Assets',
                                                           'Market value', 'Year', 'Ranking'])
            for index in range(len(forbesList)):
                self.ui.tableWidget.setItem(
                    index, 0, QtWidgets.QTableWidgetItem(forbesList[index][0]))
                self.ui.tableWidget.setItem(
                    index, 1, QtWidgets.QTableWidgetItem(forbesList[index][1]))
                self.ui.tableWidget.setItem(
                    index, 2, QtWidgets.QTableWidgetItem(forbesList[index][2]))
                self.ui.tableWidget.setItem(
                    index, 3, QtWidgets.QTableWidgetItem(str(forbesList[index][3])))
                self.ui.tableWidget.setItem(
                    index, 4, QtWidgets.QTableWidgetItem(str(forbesList[index][4])))
                self.ui.tableWidget.setItem(
                    index, 5, QtWidgets.QTableWidgetItem(str(forbesList[index][5])))
                self.ui.tableWidget.setItem(
                    index, 6, QtWidgets.QTableWidgetItem(str(forbesList[index][6])))
                self.ui.tableWidget.setItem(
                    index, 7, QtWidgets.QTableWidgetItem(str(forbesList[index][7])))
                self.ui.tableWidget.setItem(
                    index, 8, QtWidgets.QTableWidgetItem(str(forbesList[index][8])))

    # ставлю строки заполнения активными / неактивными
    def chooseNewTable(self, arg1):
        # отображаю содержимое выбранной таблицы
        self.displayTable()

        if arg1 == 'Country':
            self.ui.companyEdit.setEnabled(False)
            self.ui.countryEdit.setEnabled(True)
            self.ui.typeEdit.setEnabled(False)
            self.ui.salesBox.setEnabled(False)
            self.ui.profitsBox.setEnabled(False)
            self.ui.assetsBox.setEnabled(False)
            self.ui.marketvalueBox.setEnabled(False)
            self.ui.yearBox.setEnabled(False)
            self.ui.rankingBox.setEnabled(False)

        if(arg1 == 'Type'):
            self.ui.companyEdit.setEnabled(False)
            self.ui.countryEdit.setEnabled(False)
            self.ui.typeEdit.setEnabled(True)
            self.ui.salesBox.setEnabled(False)
            self.ui.profitsBox.setEnabled(False)
            self.ui.assetsBox.setEnabled(False)
            self.ui.marketvalueBox.setEnabled(False)
            self.ui.yearBox.setEnabled(False)
            self.ui.rankingBox.setEnabled(False)

        if(arg1 == 'Company'):
            self.ui.companyEdit.setEnabled(True)
            self.ui.countryEdit.setEnabled(True)
            self.ui.typeEdit.setEnabled(True)
            self.ui.salesBox.setEnabled(False)
            self.ui.profitsBox.setEnabled(False)
            self.ui.assetsBox.setEnabled(False)
            self.ui.marketvalueBox.setEnabled(False)
            self.ui.yearBox.setEnabled(False)
            self.ui.rankingBox.setEnabled(False)

        if(arg1 == 'Forbes'):
            self.ui.companyEdit.setEnabled(True)
            self.ui.countryEdit.setEnabled(True)
            self.ui.typeEdit.setEnabled(True)
            self.ui.salesBox.setEnabled(True)
            self.ui.profitsBox.setEnabled(True)
            self.ui.assetsBox.setEnabled(True)
            self.ui.marketvalueBox.setEnabled(True)
            self.ui.yearBox.setEnabled(True)
            self.ui.rankingBox.setEnabled(True)

    def chooseRowsInTable(self, row, column):
        tableName = self.ui.tableBox.currentText()

        if tableName == 'Country':
            self.country = self.ui.tableWidget.item(row, 0).text()
            self.ui.countryEdit.setText(self.country)

        if tableName == 'Type':
            self.type = self.ui.tableWidget.item(row, 0).text()
            self.ui.typeEdit.setText(self.type)

        if tableName == 'Company':
            self.company = self.ui.tableWidget.item(row, 0).text()
            self.ui.companyEdit.setText(self.company)
            self.country = self.ui.tableWidget.item(row, 0).text()
            self.ui.countryEdit.setText(self.country)
            self.type = self.ui.tableWidget.item(row, 0).text()
            self.ui.typeEdit.setText(self.type)

        if tableName == 'Forbes':
            self.ui.companyEdit.setText(
                self.ui.tableWidget.item(row, 0).text())
            self.ui.countryEdit.setText(
                self.ui.tableWidget.item(row, 1).text())
            self.ui.typeEdit.setText(self.ui.tableWidget.item(row, 2).text())
            self.ui.salesBox.setValue(
                int(self.ui.tableWidget.item(row, 3).text().split('.')[0]))
            self.ui.profitsBox.setValue(
                int(self.ui.tableWidget.item(row, 4).text().split('.')[0]))
            self.ui.assetsBox.setValue(
                int(self.ui.tableWidget.item(row, 5).text().split('.')[0]))
            self.ui.marketvalueBox.setValue(
                int(self.ui.tableWidget.item(row, 6).text().split('.')[0]))
            self.ui.yearBox.setValue(
                int(self.ui.tableWidget.item(row, 7).text().split('.')[0]))
            self.ui.rankingBox.setValue(
                int(self.ui.tableWidget.item(row, 8).text().split('.')[0]))

    def addRecord(self):
        print('add')
        tableName = self.ui.tableBox.currentText()

        if(tableName == 'Country'):
            country_name = self.ui.countryEdit.text().strip()
            if country_name:
                self.database.queryAddCountry(country_name)

        if(tableName == 'Type'):
            type_name = self.ui.typeEdit.text().strip()
            if type_name:
                self.database.queryAddType(type_name)

        if(tableName == 'Company'):
            company_name = self.ui.companyEdit.text().strip()
            country_name = self.ui.countryEdit.text().strip()
            type_name = self.ui.typeEdit.text().strip()

            if company_name and country_name and type_name:
                self.database.queryAddCompany(
                    company_name, country_name, type_name)

        if(tableName == 'Forbes'):
            company_name = self.ui.companyEdit.text().strip()
            country_name = self.ui.countryEdit.text().strip()
            type_name = self.ui.typeEdit.text().strip()
            sales = self.ui.salesBox.value()
            profits = self.ui.profitsBox.value()
            assets = self.ui.assetsBox.value()
            market_value = self.ui.marketvalueBox.value()
            year = self.ui.yearBox.value()
            ranking = self.ui.rankingBox.value()

            if company_name and country_name and type_name:
                self.database.queryAddForbes(company_name, country_name, type_name, sales, profits, assets,
                                             market_value, year, ranking)

        # отображаю изменения
        self.displayTable()

    def updateRecord(self):
        tableName = self.ui.tableBox.currentText()

        if(tableName == 'Country'):
            self.database.queryUpdateCountry(
                self.country, self.ui.countryEdit.text().strip())

        if(tableName == 'Type'):
            self.database.queryUpdateType(
                self.type, self.ui.typeEdit.text().strip())

        if(tableName == 'Company'):
            self.database.queryUpdateCompany(self.company, self.ui.companyEdit.text().strip(),
                                             self.ui.countryEdit.text().strip(), self.ui.typeEdit.text().strip())

        # отображаю изменения
        self.displayTable()

    def deleteRecord(self):
        print('delete')
        tableName = self.ui.tableBox.currentText()

        if(tableName == 'Country'):
            country_name = self.ui.countryEdit.text().strip()
            if country_name:
                self.database.queryDeleteCountry(country_name)

        if(tableName == 'Type'):
            type_name = self.ui.typeEdit.text().strip()
            if type_name:
                self.database.queryDeleteType(type_name)

        if(tableName == 'Company'):
            company_name = self.ui.companyEdit.text().strip()
            if company_name:
                self.database.queryDeleteCompany(company_name)

        if(tableName == 'Forbes'):
            company_name = self.ui.companyEdit.text().strip()
            year = self.ui.yearBox.value()

            if company_name:
                self.database.queryDeleteForbes(company_name, year)

        # отображаю изменения
        self.displayTable()

    def autorizashionPass(self):
        self.login = self.authForm.login
        self.ui.userLabel.setText(self.login)

        # нельзя авторизироваться несколько раз
        self.ui.actionAutorization.setEnabled(False)
        self.ui.actionRegistration.setEnabled(False)

        # настраиваю внешний вид
        self.ui.tableBox.addItems(('Country', 'Type', 'Company', 'Forbes'))
        self.ui.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.groupBox.setEnabled(True)
        self.ui.groupBox_2.setEnabled(True)

        # перед началом работы
        self.chooseNewTable('Country')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
