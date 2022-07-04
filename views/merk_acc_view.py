import mysql.connector
from Models import merk_acc_model

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="si_penjualan"
)


class MerkAccView:
    def __init__(self):
        self.connection = connection
        self.model = merk_acc_model.MerkAccModel()
        pass

    def display(self):
        while True:
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Show")
            print("5. Back")
            match(int(input("Pilih menu: "))):
                case 1:
                    self._insert()
                case 2:
                    self._update()
                case 3:
                    self._delete()
                case 4:
                    self._show()
                case 5:
                    return
                case _:
                    print("Menu tidak tersedia")

    def _insert(self):
        nama_merk = input("Nama Merk: ")
        data = (nama_merk)
        self.model.insert(data)

    def _update(self):
        id_merk_acc = int(input("Id Merk Acc: "))
        nama_merk = input("Nama Merk: ")
        data = (id_merk_acc, nama_merk)
        self.model.update(data)

    def _delete(self):
        id_acc_hp = int(input("ID Merk Acc: "))
        self.model.delete(id_merk_acc)

    def _show(self):
        for data in self.model.get_data():
            print("|{}.| {} |".format(data[0], data[1]))