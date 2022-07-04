import mysql.connector

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="si_penjualan"
)


class JenisAccModel:
    def __init__(self):
        self.connection = connection
        pass

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM jenis_acc"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO jenis_acc (id_merk_acc, nama_jenis_acc) VALUES ('{}', '{}')".format(data[0], data[1])
        cursor.execute(query)
        self.connection.commit()

    def update(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE jenis_acc SET ID_MERK_ACC='{]', NAMA_JENIS_ACC='{}' WHERE ID_JENIS_ACC={}".format(data[1], data[2], data[0])
        cursor.execute(query)
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        query = "DELETE FROM jenis_acc WHERE ID_JENIS_ACC={}".format(id)
        cursor.execute(query)
        self.connection.commit()

