import pyodbc


class Database:
    def __init__(self):
        self.cnxn = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-D3C3R5R\SQLEXPRESS;Database=Forbes;Trusted_Connection=yes;')

    def querySelectAllCountries(self):
        companiesList = []
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.SelectAllCountriesNames;')
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                companiesList.append(row.name)
            cursor.close()

        except Exception:
            print('Error in query SelectAllCountries')

        return companiesList

    def querySelectAllTypes(self):
        typesList = []
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.SelectAllTypesNames;')
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                typesList.append(row.name)
            cursor.close()

        except Exception:
            print('Error in query SelectAllTypes')

        return typesList

    def querySelectAllCompanies(self):
        companiesList = []
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.SelectCompaniesWithCountriesAndType;')
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                companiesList.append(
                    [row.company_name, row.country_name, row.type_name])
            cursor.close()

        except Exception:
            print('Error in query SelectAllCompanies')

        return companiesList

    def querySelectAllForbes(self):
        forbesList = []
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.SelectAllForbes;')
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                forbesList.append([row.company_name, row.country_name, row.type_name, row.sales,
                                   row.profits, row.assets, row.market_value, row.ryear, row.ranking])
            cursor.close()

        except Exception:
            print('Error in query SelectAllForbes')

        return forbesList

    def queryDeleteCountry(self, country_name):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.DeleteCountry ?', country_name)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query DeleteCountry')

    def queryDeleteType(self, type_name):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.DeleteType ?', type_name)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query DeleteType')

    def queryDeleteCompany(self, company_name):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.DeleteCompany ?', company_name)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query DeleteCompany')

    def queryDeleteForbes(self, company_name, year):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.DeleteForbes ?, ?', company_name, year)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query DeleteForbes')

    def queryAddCountry(self, country_name):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.InsertCountry ?', country_name)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query InsertCountry')

    def queryAddType(self, type_name):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.InsertType ?', type_name)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query InsertType')

    def queryAddCompany(self, company_name, country_name, type_name):
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.InsertCompany ?, ?, ?',
                           company_name, country_name, type_name)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query InsertCompany')

    def queryAddForbes(self, company_name, country_name, type_name, sales, profits, assets, market_value, year, ranking):
        try:
            if sales == 0:
                sales = 'NULL'

            if profits == 0:
                profits = 'NULL'

            if assets == 0:
                assets = 'NULL'

            if market_value == 0:
                market_value = 'NULL'

            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.InsertForbes ?, ?, ?, ?, ?, ?, ?, ?, ?', company_name, country_name, type_name, sales,
                           profits, assets, market_value, '01.01.' + str(year), ranking)

            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query InsertForbes')

    def queryInsertUser(self, login, password, access):
        success = 0
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.InsertUser ?, ?, ?',
                           login, password, access)
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query InsertUser')

        return success

    def querySelectUser(self, login, password):
        access = 0
        try:
            cursor = self.cnxn.cursor()
            cursor.execute('EXEC dbo.SelectUser ?, ?', login, password)
            row = cursor.fetchone()
            access = row[0]
            cursor.commit()
            cursor.close()

        except Exception:
            print('Error in query SelectUser')

        return access

    def queryUpdateCountry(self, last_name, next_name):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute('EXEC dbo.UpdateCountry ?, ?', last_name, next_name)
            cursor.commit()
            cursor.close()

        except Exception:
            cursor.close()
            print('Error in query UpdateCountry')

    def queryUpdateType(self, last_name, next_name):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute('EXEC dbo.UpdateType ?, ?', last_name, next_name)
            cursor.commit()
            cursor.close()

        except Exception:
            cursor.close()
            print('Error in query UpdateType')

    def queryUpdateCompany(self, last_company, next_company, next_country, next_type):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute('EXEC dbo.UpdateCompany ?, ?, ?, ?', last_company, next_company,
                            next_country, next_type)
            cursor.commit()
            cursor.close()

        except Exception:
            cursor.close()
            print('Error in query UpdateType')
