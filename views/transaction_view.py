from prettytable import PrettyTable

from Models import transaction_model, acc_hp_model


class TransactionView:
    def __init__(self):
        self.transaction_model = transaction_model.TransModel()
        self.acc_hp_model = acc_hp_model.AccHpModel()

    def display(self):
        while True:
            print("1. Insert")
            print("2. Show")
            print("3. Back")
            match (int(input("Pilih menu: "))):
                case 1:
                    self._insert()
                case 2:
                    self._show()
                case 3:
                    return
                case _:
                    print("Menu tidak tersedia")

    def _insert(self):
        nama_acc_hp = input("Nama Acc HP: ")
        id_acc_hp = self.search_acc_hp(nama_acc_hp)
        if id_acc_hp is None:
            print("Acc HP tidak ditemukan")
            return
        jumlah = int(input("Jumlah: "))
        harga = int(input("Harga: "))
        total_harga = jumlah * harga
        data = (id_acc_hp, jumlah, harga, total_harga)
        self.transaction_model.insert(data)
        self.transaction_model.reduce_stock(data)

    def _show(self):
        x = PrettyTable()
        x.field_names = ["Tanggal Transaksi", "Nama Acc", "Nama Jenis Acc", "Nama Merk Acc", "Nama Type HP", "Jumlah",
                         "Harga", "Total Harga"]
        for data in self.transaction_model.get_data():
            x.add_row(data)
        print(x)

    def search_acc_hp(self, nama_acc_hp):
        for data in self.acc_hp_model.get_data():
            if data[3] == nama_acc_hp:
                return data[0]
        return None
