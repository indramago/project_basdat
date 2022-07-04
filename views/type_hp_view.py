import mysql.connector
from Models import type_hp_model

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="si_penjualan"
)


class TypeHpView:
    def __init__(self):
        self.connection = connection
        self.model = type_hp_model.TypeHpModel()
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
        nama_type_hp = input("Nama Type Hp: ")
        data = (nama_type_hp)
        self.model.insert(data)

    def _update(self):
        id_type_hp = int(input("ID Type Hp: "))
        nama_type_hp = input("Nama Type Hp: ")
        data = (id_type_hp, nama_type_hp)
        self.model.update(data)

    def _delete(self):
        id_type_hp = int(input("ID Type Hp: "))
        self.model.delete(id_type_hp)

    def _show(self):
        for data in self.model.get_data():
            print("|{}.| {} |".format(data[0], data[1],))