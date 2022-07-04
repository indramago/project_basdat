import mysql.connector

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="si_penjualan"
)


class TypeHpModel:
    def __init__(self):
        self.connection = connection
        pass

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM type_hp"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO type_hp (nama_type_hp) VALUES ('{}')".format(data)
        cursor.execute(query)
        self.connection.commit()

    def update(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE type_hp SET NAMA_TYPE_HP='{}' WHERE ID_TYPE_HP={}".format(data[1], data[0])
        cursor.execute(query)
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        query = "DELETE FROM type_hp WHERE ID_TYPE_HP={}".format(id)
        cursor.execute(query)
        self.connection.commit()

