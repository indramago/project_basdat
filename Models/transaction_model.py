import mysql.connector


class TransModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="crystal",
            database="si_penjualan"
        )

    def get_data(self):
        cursor = self.connection.cursor()
        query = """SELECT
            transaksi.tgl_transaksi,
            acc_hp.NAMA_ACC,
            jenis_acc.NAMA_JENIS_ACC,
            merk_acc.NAMA_MERK,
            type_hp.NAMA_TYPE_HP,
            transaksi.jumlah,
            transaksi.harga,
            transaksi.total_harga 
            FROM transaksi
            INNER JOIN acc_hp ON transaksi.id_acc_hp = acc_hp.ID_ACC_HP
            INNER JOIN jenis_acc ON acc_hp.id_jenis_acc = jenis_acc.ID_JENIS_ACC
            INNER JOIN merk_acc ON jenis_acc.id_merk_acc = merk_acc.ID_MERK_ACC
            INNER JOIN type_hp ON acc_hp.id_type_hp = type_hp.ID_TYPE_HP
            """
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
        query = "INSERT INTO transaksi (id_acc_hp, tgl_transaksi, jumlah, harga, total_harga) " \
                "VALUES ('{}', NOW(), '{}', '{}', '{}')".format(data[0], data[1], data[2], data[3])
        cursor.execute(query)
        self.connection.commit()
