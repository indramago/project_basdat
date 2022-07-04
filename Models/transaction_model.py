import mysql.connector


class TransModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="si_penjualan"
        )

    def get_data(self):
        cursor = self.connection.cursor()
        query = "select id_transaksi, t.tgl_transaksi,	ah.NAMA_ACC, ja.NAMA_JENIS_ACC, ma.NAMA_MERK, th.NAMA_TYPE_HP, t.jumlah, t.harga, t.total_harga from transaksi t left join acc_hp ah on t.id_acc_hp = ah.ID_ACC_HP left join jenis_acc ja on ah.id_jenis_acc = ja.ID_JENIS_ACC left join merk_acc ma on ja.id_merk_acc = ma.ID_MERK_ACC left join type_hp th on ma.id_type_hp = th.ID_TYPE_HP"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def reduce_stock(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE acc_hp SET stok_acc = stok_acc - '{}' WHERE id_acc_hp = '{}'".format(data[1], data[0])
        cursor.execute(query)
        self.connection.commit()

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO transaksi (nama_acc_hp, tgl_transaksi, jumlah, harga, total_harga) " \
                "VALUES ('{}', NOW(), '{}', '{}', '{}')".format(data[0], data[1], data[2], data[3])
        cursor.execute(query)
        self.connection.commit()


