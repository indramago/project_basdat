import mysql.connector

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="crystal",
    database="si_penjualan"
)


class AccHpModel:
    def __init__(self):
        self.connection = connection
        pass

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM acc_hp"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO acc_hp (id_jenis_acc, id_type_hp, nama_acc, stok_acc) VALUES ('{}', '{}', '{}', '{}')".format(
            data[0], data[1], data[2], data[3])
        cursor.execute(query)
        self.connection.commit()

    def update(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE acc_hp SET id_jenis_acc='{}', id_type_hp='{}', NAMA_ACC='{}', stok_acc='{}' WHERE ID_ACC_hp={}".format(
            data[1], data[2], data[3], data[4], data[0])
        cursor.execute(query)
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        query = "DELETE FROM acc_hp WHERE ID_ACC_HP={}".format(id)
        cursor.execute(query)
        self.connection.commit()
