import cx_Oracle
class Doctor:
    def __init__(self):
        self.connection = cx_Oracle.connect(user='system', password='pythonoracle', dsn='localhost/XE')
    def listado(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select * from doctor")
        except self.connection.Error as e:
            print(e)
        return cursor

    def busca(self, name):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select * from doctor where apellido like '%"+name+"%'")
        except self.connection.Error as e:
            print(e)
        return cursor