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
            match(int(input("Pilih menu: "))):
                case 1:
                    self._insert()
                case 2:
                    self._show()
                case 3:
                    return
                case _:
                    print("Menu tidak tersedia")

    def _insert(self):
        id_acc_hp = int(input("ID Acc Hp: "))
        jumlah = int(input("Jumlah: "))
        harga = int(input("Harga: "))
        total_harga = jumlah * harga
        data = (id_acc_hp, jumlah, harga, total_harga)
        self.transaction_model.insert(data)
        self.transaction_model.reduce_stock(data)

    def _show(self):
        for data in self.transaction_model.get_data():
            print("|{}.| {} | {} | {} | {} | {} | {} | {} | {} |".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))