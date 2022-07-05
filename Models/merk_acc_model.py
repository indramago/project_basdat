import mysql.connector

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="crystal",
    database="si_penjualan"
)


class MerkAccModel:
    def __init__(self):
        self.connection = connection
        pass

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM merk_acc"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO merk_acc (nama_merk) VALUES ('{}')".format(data)
        cursor.execute(query)
        self.connection.commit()

    def update(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE merk_acc SET NAMA_MERK='{}' WHERE ID_MERK_ACC={}".format(data[1], data[0])
        cursor.execute(query)
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        query = "DELETE FROM MERK_ACC WHERE ID_MERK_ACC={}".format(id)
        cursor.execute(query)
        self.connection.commit()
